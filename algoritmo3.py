def dividir(a,b):
    try:
        z = a/b
        print("la division es:", z)
    except ZeroDivisionError:
        print("la dividion es indeterminada")
    
dividir(17,0)
