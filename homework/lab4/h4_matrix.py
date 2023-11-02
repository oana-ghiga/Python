class Matrix:
    def __init__(self, n, m): #init used here for the constructor
        self.matrix = [[0 for _ in range(m)] for _ in range(n)] #create a matrix with n rows and m columns

    def get(self, i, j):
        return self.matrix[i][j] #get the element at row i and column j

    def set(self, i, j, value):
        self.matrix[i][j] = value #set the element at row i and column j to value

    def transpose(self):
        return [[self.get(j, i) for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))] #transpose the matrix by switching the rows and columns

    def multiply(self, other):
        result = Matrix(len(self.matrix),
                        len(other.matrix[0]))  # first check for the dimensions
        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[0])):
                for k in range(len(other.matrix)):
                    result.set(i, j, result.get(i, j) + self.get(i, k) * other.get(k, j))
        return result

    def transform(self, func):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.set(i, j, func(self.get(i, j)))

#matrix initialization
m = Matrix(3, 3)
m.set(0, 0, 1)
m.set(1, 1, 2)
m.set(2, 2, 3)

# depending on i and j show an element
print(m.get(1, 1))  # Output: 2

#transpuse
t = m.transpose()
print(t)  # Output: [[1, 0, 0], [0, 2, 0], [0, 0, 3]]

# matrix no 2 for multiplication
m2 = Matrix(3, 3)
m2.set(0, 0, 4)
m2.set(1, 1, 5)
m2.set(2, 2, 6)
result = m.multiply(m2)
print(result.matrix)  # Output: [[4, 0, 0], [0, 10, 0], [0, 0, 18]]

#transformation
(m.transform(lambda x: x * x))
print(m.matrix)  # Output: [[1, 0, 0], [0, 4, 0], [0, 0, 9]]
