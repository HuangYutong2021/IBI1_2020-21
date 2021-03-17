import numpy as np
import matplotlib.pyplot as plt
# import the numpy and matplotlib.pyplot so that we can make the boxplot and do some numerical operations.
n = 10   # just a reminder, no substantive meaning
gene_length = [9410,394141,4442,105338,19149,76779,126550,36296,842,159]
exon_counts = [51,1142,42,216,25,650,32533,57,1,523]
# obviously list all data
a = np.array(gene_length)
b = np.array(exon_counts)
# put all data into array so that the data can be performed numerical operations
average = a / b
# do some division method to get the average
plt.boxplot(average, vert = True, whis = 1.5, patch_artist = True, meanline = True, boxprops= {'facecolor':'pink'})
# set some important values of the boxplot. One point is to change the facecolor from blue to pink, which is appealing.
plt.show()     #show the graph
