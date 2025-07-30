def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: división por cero"
    
print(dividir(10, 0))
