# CEC 2017 - Benchmark Functions (Bound Constrained) in Python
Very simple Python wrapper function for the benchmark functions of the CEC 2017 Special Session and Competition on Single Objective Bound Constrained Real-Parameter Numerical Optimization, originally written in C.

## Instructions
First you have to compile the original file where the CEC17 functions are written in C. In my computer, running on a Ubuntu 18.04 and GCC 7.3.0, in the same directory as the .c file I enter the following command on terminal:
```
gcc -fPIC -shared -lm -o cec17_test_func.so cec17_test_func.c
```

This command is going to generate a file called cec17_test_func.so, which is going to be used by the wrapper function 'cec17_test_func' in the module 'cec17_functions'.

Since there is no pip installation, you'll have to manually include these files on your project so that you would have access to them. After doing that, you might be able to call 'cec17_test_func' function and compute the fitness value of a given solution vector. Don't forget to also copy 'input_data' to your project's directory.

In order to call the 'cec17_test_func' function, first you need to import it from 'cec17_functions'.
```python
from cec17_functions import cec17_test_func
```

The following lines is just me creating the arguments necessary to demonstrate how to call the function. 
```python
# x: Solution vector
x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# nx: Number of dimensions
nx = 10
# mx: Number of objective functions
mx = 1
# func_num: Function number
func_num = 1
# Pointer for the calculated fitness
f = [0]
```

This is how you call the function, just like in the original code in C (same order of the arguments): 
```python
cec17_test_func(x, f, nx, mx, func_num)
```

The result is stored in the vector 'f'. If mx==1, only the first element of ‘f’ is used. 
```python
# This line is going to print 29975432515.940056
print(f[0])
```
