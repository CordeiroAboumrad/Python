import numpy as np
import random
import matplotlib.pyplot as plt
import random

# ---------------------------------------- LEI DOS GRANDES NÚMEROS ------------------------------
print(f"\n Lei dos Grandes Números\n")
# Step 1
possible_outcomes = [0, 1]
distribution = [0.3, 0.7]


def pick_random_number():
    random_number = random.choices(possible_outcomes, distribution)
    return random_number


l = []
samplemeanlist = []

# set sample size (i) between 1 to 10000, step by 50
for i in range(0, 10001, 50):
    # set x-axis
    l.append(i)
    # list of mean of each sample
    meanlist = []
    # sample 50 time.
    sum_random_number = 0
    for n in range(0, i):
        # random pick from population with sample size = i
        sum_random_number += pick_random_number().pop(0)
        # print(sum_random_number)

    meanlist.append(float(sum_random_number / (i + 1)))

    # save the sample mean in samplemeanlist for box plots
    samplemeanlist.append(meanlist[0])

print(samplemeanlist)
print(l)
# Step 3
# set figure size
plots = plt.figure(figsize=(20, 10))
# plot box plots of each sample mean
plt.plot(l, samplemeanlist)

plt.axhline(y=0.7, color='r', linestyle='-')

plt.ylim([0, 1])
# plt.xlim([0,10000])
# show plot.
plt.show()

# print("sample with 100 sample size," + \
#       "mean:" + str(np.mean(samplemeanlist[0])) + \
#       ", standard deviation: " + str(np.std(samplemeanlist[0])))
# print("sample with 8100 sample size," + \
#       "mean:" + str(np.mean(samplemeanlist[16])) + \
#       ", standard deviation: " + str(np.std(samplemeanlist[16])))
#
# # last hist plot
# histplot = plt.figure(figsize=(20, 10))
# plt.hist(samplemeanlist[0], 10, density=True)
# plt.hist(samplemeanlist[16], 10, density=True)
# histplot.show()

input()
