import numpy as np
import math

class MatrixOperator:
    '''Class for operating with random matrix.'''
    def __init__(self):
        self.__matrix = np.ndarray([0,0])

    def generateMatrix(self, a:int, b:int):
        self.__matrix = np.random.rand(a,b)
    
    def __str__(self):
        for row in self.__matrix:
            print(row)

    def countMoreThanMean(self):
        shape = self.__matrix.shape
        mean = self.__matrix.mean()
        count = 0
        for row in self.__matrix:
            for el in row:
                if el > mean:
                    count+=1
        return count
    
    @property
    def matrix(self):
        return self.__matrix

    @matrix.setter
    def matrix(self, input):
        self.__matrix = input

    def calculateSTDNumpy(self):
        return self.__matrix.std()

    def calculateSTD(self):
        shape = self.__matrix.shape
        squareSum = 0
        mean = self.__matrix.mean()
        for i in range(shape[0]):
            for j in range(shape[1]):
                squareSum += (self.__matrix[i][j]-mean)**2
        std = math.sqrt(squareSum/(shape[0]*shape[1]))
        return std