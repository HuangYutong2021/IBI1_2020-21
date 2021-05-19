def helper(name, portfolio, poster, final):
    grade= float(portfolio)*0.4 + float(poster)*0.3 + float(final)*0.3
    return (name,grade)

print('please input your name')
a=input()
print('please input the portfolio grade of the student')
b=input()
print('please input the poster presentation grade of the student')
c=input()
print('please input the final exam grade of the student')
d=input()
ultimate=str(helper(a,b,c,d))
#remove some unnecessary symbols
ultimate=ultimate.replace("'", '')
ultimate=ultimate.replace("(", '')
ultimate=ultimate.replace(")", '')
ultimate=ultimate.replace(",", '')
print(ultimate)
