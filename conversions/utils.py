def C_to_F(celsius):
    if celsius < -273.15:
        raise ValueError('Invalid temperature: {} is less than absolute zero (-273.15 F).'.format(celsius))
    else:
        fahrenheit = ((9/5)*celsius) + 32
        return fahrenheit

def F_to_C(fahrenheit):
    if fahrenheit < -459.67:
        raise ValueError('Invalid temperature: {} is less than absolute zero (-459.67 F).'.format(fahrenheit))
    else:
        celsius = (5/9)*(fahrenheit - 32)
        return celsius
