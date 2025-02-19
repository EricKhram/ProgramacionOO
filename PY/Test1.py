#!/usr/bin/env python3

def Nombre(name):
    """function nombre"""
    nombre = input("ingrese su nombre:  ")
    output = f"hola {nombre}, ¿como estas?"
    return output

def run():
    print(Nombre(f"{Nombre}"))
    
if __name__ == "__main__":
    run()