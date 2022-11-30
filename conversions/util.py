def C_to_F(celsius):
    try:
        celius >= -273.15
        return 32+((9/5)*celsius)
    except:
        ValueError('The temperature is less than absolute value')

def F_to_C(fahrenheit):
    try:
        fahrenheit >= -459.67
        return (fahrenheit-32)*(5/9)
    except:
        ValueError('The temperature is less than absolute value')
