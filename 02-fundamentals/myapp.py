EARTH_GRAVITY = 6.674e-11 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = (16.6*6.674e-11)/100 #? měsíční gravitace
SPEED_OF_LIGHT = 300000 #? rychlost světla ve vakuu
SPEED_OF_SOUND = 343 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu

def gravitational_force_on_earth():
    """ function for calculating gravitational influence of two bodies on earth"""
    m1 = float(input('Enter weight of first body (Kg): '))
    m2 = float(input('Enter weight of second body (Kg): '))
    r = float(input('Enter distance (m): '))
    F = EARTH_GRAVITY * m1 * m2 / r ** 2
    return print("the gravitational force between two objects ont earth is: ",round(F,2),"N")
def gravitational_force_on_moon():
    """ function for calculating gravitational influence of two bodies on moon"""
    m1 = float(input('Enter weight of first body (Kg): '))
    m2 = float(input('Enter weight of second body (Kg): '))
    r = float(input('Enter distance (m): '))
    Fm = MOON_GRAVITY * m1 * m2 / r ** 2
    return print("the gravitational force between two objects on the moon is: ", round(Fm, 2), "N")
def mce2():
    """ function for calculating energy needed to fuse a body of mass"""
    m = float(input('Enter weight of body (Kg): '))
    E = m * SPEED_OF_LIGHT ** 2
    return print("the energy required to make and object with a weight of", round(m, 2), "Kg is: ", round(E, 2), "J")
def frequency():
    """ function returning a wavelenght of sound with certain frequency"""
    f = float(input('Enter frequency of sound (Hz): '))
    λ = SPEED_OF_SOUND / f
    return print("the wavelenght of a sound with frequency of", round(f, 2), "Hz is: ", round(λ, 2), "m")
def wavelenght():
    """ function returning a frequency of sound with certain wavelenght"""
    λ = float(input('Enter wavelenght of sound (m): '))
    f = SPEED_OF_SOUND / λ
    return print("the frequency of a sound with wavelenght of", round(λ, 2), "m is: ", round(f, 2), "Hz")