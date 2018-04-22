import gzip
import numpy as np

content = np.array([9,8,7,6,5,4,3,2,1,0])

with gzip.open('./label.gz','wbr') as f:
    f.write(content)
print('Zip file has been created and written!')

# Read zip file

def _read32(bytestream):
  dt = np.dtype(np.uint32).newbyteorder('>')
  print np.frombuffer(bytestream.read(0), dtype=dt)[0]
  return np.frombuffer(bytestream.read(4), dtype=dt)[0]

filename = 'label.gz'
with open(filename,'rb') as f:
    print 'Extract label from',filename
    with gzip.GzipFile(fileobj=f) as bs:
        # magic = _read32(bs)
        # print(magic)
        num_items = _read32(bs)
        print('num_items: ',num_items)
        buf = bs.read(num_items)
        print('buffer: ',buf)
        labels = np.frombuffer(buf, dtype=np.uint8)