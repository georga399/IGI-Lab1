from .MatrixOperator import MatrixOperator

def task5():
    mop = MatrixOperator()
    mop.generateMatrix(5,10)
    print("matrix:")
    print(mop.__str__())
    print(f"Elements that more than mean:{mop.countMoreThanMean()}")
    print(f"STD:{mop.calculateSTD()}")
    print(f"STD(numpy method):{mop.calculateSTDNumpy()}")
    print()