from ctypes import CDLL, POINTER, c_int, c_double
import os

def cec17_test_func(x, f, nx, mx, func_num,
                    dll_path=CDLL(os.path.abspath('cec17_test_func.so'))):
    functions = dll_path
    x_pointer_type = POINTER(c_double * nx)
    f_pointer_type = POINTER(c_double * mx)
    nx_type = c_int
    mx_type = c_int
    func_num_type = c_int
    functions.cec17_test_func.argtypes = [x_pointer_type, f_pointer_type,
                                          nx_type, mx_type, func_num_type] 
    functions.cec17_test_func.restype = None
    x_ctype = (c_double * nx)()
    for i, value in enumerate(x):
        x_ctype[i] = value
    f_ctype = (c_double * mx)()
    for i in range(mx):
        f_ctype[i] = 0
    functions.cec17_test_func(x_pointer_type(x_ctype), f_pointer_type(f_ctype),
                              nx, mx, func_num)
    for i in range(len(f)):
        f[i] = f_ctype[i]
