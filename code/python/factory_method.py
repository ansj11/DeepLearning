# -*- coding: utf-8 -*-

import xml.etree.ElementTree as etree
import json
from IPython import embed

class JSONConnector:
    def __init__(self,filepath):
        self.data = dict()
        with open(filepath,mode='r',encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data

class XMLConnector:
    def __init__(self,filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree

def connection_factory(filepath):
    if filepath.endswith('json'):
        connctor = JSONConnector
    elif filepath.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError('Cannot connect to {}'.format(filepath))
    return connector(filepath)

def connect_to(filepath):
    factory = None
    try:
        factory = connection_factory(filepath)
    except ValueError as ve:
        print(ve)
    return factory

def main():
    sqlite_factory = connect_to('./test.sq3')
    print()

    xml_factory = connect_to('./test.xml')
    xml_data = xml_factory.parsed_data
    liars = xml_data.findall(".//{}[{}='{}']".format('person','lastname','Smith'))
    print("Found: {} persons".format(len(liars)))
    for liar in liars:
        print('firstname: {}'.format(liar.find('firstname').text))
        print('lastname: {}'.format(liar.find('lastname').text))
        #[print("phone number ({})".format(p.attrib['type']),p.text) for p in liar.find('phoneNumbers')]
    print()

    json_factory = connect_to('./test.json')
    json_data = json_factory.parsed_data
    print('found: {}'.format(len(json_data)))
    for donut in json_data:
        print('name: {}'.format(donut['name']))
        print('price: {}'.foramt(donut['ppu']))
        #[print('topping: {} {}'.format(t['id'],t['type'])) for t in donut['topping']]

if '__name__'=='__main__':
    main()

