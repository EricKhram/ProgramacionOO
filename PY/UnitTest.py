#!/usr/bin/env python3

import Test1

def test():
    """Unit test for test1"""
    # run the function to test and recover its output
    check_output = Test1.Nombre(f"{Test1.Nombre}")
    # verify the output
    if check_output == Test1.Nombre(f"hola {Test1.Nombre}, ¿como estas?"): 
        print("Test is OK")
    else: 
        print(f'"Test is not OK! expected a "algo"')
        print(f'.. but received {check_output}')

if __name__ == "__main__":
    test()