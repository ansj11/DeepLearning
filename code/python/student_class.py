class SimpleGradebook(object):
	def __init__(self):
		self._grades={}
	def add_student(self,name):
		self._grades[name]=[]
	def report_grade(self,name,score):
		self._grades[name].append(score)
	def average_grade(self,name):
		grades=self._grades[name]
		return sum(grades)/len(grades)

book = SimpleGradebook()

book.add_student('ansj')

book.report_grade('ansj',90)

print(book.average_grade('ansj'))



import collections
Grade=collections.namedtuple('Grade',('score','weight'))
print(Grade)

class Subject(object):
    def __init__(self):
        self._grades=[]

    def report_grade(self,score,weight):
        self._grades.append(Grade(score,weight))

    def average_grade(self):
        total,total_weight=0,0
        for grade in self._grades:
            total+=grade.score*grade.weight
            total_weight+=grade.weight
        return total/total_weight

class Student(object):
    def __init__(self):
        self._subjects={}

    def subject(self,name):
        if name not in self._subjects:
            self._subjects[name]=Subject()
        return self._subjects[name]
