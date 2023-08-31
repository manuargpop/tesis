from matplotlib import pyplot as plt

x = ['2010', '2002', '2004', '2006', '2008']
y = [10, 25, 50, 15, 8]

plt.bar(x, y)

plt.savefig("output-1.jpg")