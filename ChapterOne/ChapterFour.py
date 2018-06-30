def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v, w)]

print(vector_add([1,2], [2,1]))

def vector_subtract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]

def vector_sum(vectors):
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result

print(vector_sum([[1,2], [2,1], [3,4]]))


from functools import reduce
def vector_sum2(vectors):
    return reduce(vector_add, vectors)

print(vector_sum2([[1,2], [2,1], [3,4]]))

from functools import partial
vector_sum3 = partial(reduce, vector_add)
print(vector_sum3([[1,2], [2,1], [3,4]]))

def scalar_multiply(c, v):
    return [c * v_i for v_i in v]

def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum2(vectors))

def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    return dot(v, v)

import math

def magnitude(v):
    return math.sqrt(sum_of_squares(v))

print(magnitude([1, 1]))

def squared_distance(v, w):
    return(sum_of_squares(vector_subtract(v, w)))

def distance(v, w):
    return math.sqrt(squared_distance(v, w))

def distance2(v, w):
    return magnitude(vector_subtract(v, w))


print(distance2([0,1], [1,1]))

#matrixes------

A = [[1,2,3],
     [4,5,6]]

def shape(A):
    num_rows = len(A);
    num_cols = len(A[0])
    return num_rows, num_cols

print(shape(A))

def get_row(A, i):
    return A[i]

def get_columns(A, j):
    return [A_i[j] for A_i in A]

def make_matrix(num_rows, num_cols, entry_fn):
    return [[entry_fn(i, j) 
             for j in range(num_cols)]
             for i in range(num_rows)]

def is_diagonal(i, j):
    return 1 if i == j else 0

identity_matrix = make_matrix(5,5,is_diagonal)
print(identity_matrix)