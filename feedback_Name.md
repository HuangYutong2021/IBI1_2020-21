Week4 I got full scores.

Week5
variables.py
I found there exsit some strange and invalid syntax which may be confusing, so I deleted them.

mystery_code.py 
I read the feadback and know that my comment answer is not complete. Therefore,  I have corrected the comment answer. Now it is: the program select a random number between 1 and 100 and only when the number less than or equal to 50, that number will be output.

There is no mistakes in other files.

Week6
Coronavirus_rates.py
After reading the feedback, I found I ignored the "input data" in the instructions. So, I added some codes as follows:
print('please input the number of cases in USA')
a = input()
others are quite like these two to store the input data.
And then, I transformed one code into:
sizes=[a,b,c,d,e]
In that case, the frequency distributions in pie chart can change with the input data.
Since the feedback says there is no title in the pie chart, so I add one code in the next to the last line:
plt.title("the total number of coronavirus infection cases for five countries ")

List_manipulation.py
I found that I ignored one requirement to sort the values. Therefore, I added codes:
list = sorted(average)
print(list)
