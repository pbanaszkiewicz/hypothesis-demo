# Hypothesis demo


## Prepare

1. Install depedencies: `poetry install`
2. Remove cache directory: `rm -r .hypothesis`

## Basic example: `test_1.py`

1. Show maths example
2. Show `poetry run pytest --hypothesis-show-statistics`
3. Remove cache directory: `rm -r .hypothesis`
4. Show `poetry run pytest --hypothesis-show-statistics`


## Advanced example: testing multidimensional vector

Vector class copied from / inspired by Fluent Python example.

1. Show `Vector` class
2. Define mathematical properties of a vector:

    1. Two identical vectors are equal
    2. Adding vectors `Vector(x1, x2, x3, ...)+Vector(y1, y2, y3, ...)` of
       equal length produces a new vector `Vector(x1+y1, x2+y2, x3+y3, ...)`
    3. Vector is true if any of it's components is != 0
    4. Vector is false if all of it's components are == 0
    5. Length (magnitude) of a unit vector (e.g. `(1, 0, 0, 0, ...)`) is always 1
    6. Length (magnitude) of a zero vector is always 0
    7. `Vector(x1, x2, x3, ...) * N` is `Vector(x1 * N, x2 * N, x3 * N, ...)`
    8. `Vector(x1, x2, x3, ...) * Vector(y1, y2, y3, ...)` is
       `Vector(x1 * y1, x2 * y2, x3 * y3, ...)`
    9. `Vector(x1, x2, x3, ...) @ Vector(y1, y2, y3, ...)` is
       `x1*y1 + x2*y2 + x3*y3 + ...`
    10. Slice `[:]` of a vector is equal to the vector
    11. Slice `[x:y]` of a vector is still a vector
    12. Slice `[n]` of a vector is a single value

3. Implement as many test cases as possible, explaining tips and tricks
