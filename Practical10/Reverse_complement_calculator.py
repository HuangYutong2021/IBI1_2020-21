
def transformation(i):
 code = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
 re = str(i)
#Convert all letters to uppercase
 record = re.upper()
 se = ''
#convert it to its complementary form
 for a in range(0,len(i)):
  one = record[a:a+1]
  se += str(code[one])
#reverse its order
 for a in range(0,len(i)):
  print(se[len(i)-1-a:len(i)-a],end='')


sequence = input()
transformation(sequence)
