# WAP to convert Celcsius to Fahrenheit

def f_to_c(f):
    c = 5*(f-32)/9
    return c

f = int(input("enter temperature in F: "))
cel = f_to_c(f)
print(f"Temperature in c is = {round(cel, 2)}°C") # round( _, _) helps to round off the big number