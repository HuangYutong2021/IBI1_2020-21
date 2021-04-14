class Student (object):
    def __init__(self,first_name, family_name, programme):
         self.first_name = first_name
         self.family_name = family_name
         self.programme = programme
         print(first_name,family_name, programme)

print('please input the first name of the student')
a=input()
print('please input the family name of the student')
b=input()
print('please input the undergraduate programme of the student')
c=input()
i=Student(a,b,c)
