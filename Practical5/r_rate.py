# define the rate
r = 1.2
# define the numbder of the original infected prople
n = 84
# circulate 5 times
for i in range(1,6):
# every time each individual will infect 1.2 individuals, so we add the newly-infected people and previously infected prople together.
    n = n * r + n

print( " the r rate is ", r)
print( " the total number of individuals infected after 5 generations", n)
