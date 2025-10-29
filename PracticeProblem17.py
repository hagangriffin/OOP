import matplotlib.pyplot as plt
import numpy as np

x = np.array(["c1", "c2", "c3", "c4"])
y = np.array([80, 100, 62, 76])

print(np.mean(y))
print(np.median(y))
print(np.std(y))

plt.xlabel("Courses")
plt.ylabel("grades")
plt.plot(x, y)
plt.show()

mylabels = ["a1", "a2", "a3", "a4"]

plt.pie(y, labels=mylabels)
plt.show()

#x = [4, 5, 10, 4, 3, 11, 14 , 8, 10, 12]
x = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

plt.scatter(x,y)
plt.show()

with open("mycourse1.txt") as file_name:
    array = np.loadtxt(file_name, delimiter=",")

#for i in range(1,len(array)):
#data1 = i
print(array)
stu_list=["s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "s11", "s12", "s13", "s14", "s15", "s16", "s17", "s18", "s19", "s20"]
plt.pie(array, labels=stu_list)
plt.show()