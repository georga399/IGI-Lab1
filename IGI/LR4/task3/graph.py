import math
import matplotlib.pyplot as plt

def graph(x1, y1, x2, y2):
    '''Function for plot.'''
    plt.plot(x1, y1, label='math.asin')
    plt.plot(x2, y2, label='taylor')
    plt.xlabel("X-axis data")
    plt.ylabel("Y-axis data")
    plt.legend()
    plt.savefig('task3/graph.png')