import numpy as np

def atmosisa(h, D_ISA = 0, unit='m'):
    '''
    Essa função calcula a atmosfera ISA
    Pode-se calcular as propriedades do ar quando existe um delta ISA 
   '''
    if unit == 'ft':
        h *= 0.3048
    c = -6.5e-3
    R = 287.053
    gamma = 1.4
    T_ssl = 288.15
    rho_ssl = 1.225
    g =  9.80665
    if h <= 11000:
        T = T_ssl + c*h
        rho = rho_ssl*(T/T_ssl)**(-g/(c*R)-1)
    else:
        T = T_ssl + c*11000
        rho = rho_ssl*(T/T_ssl)**(-g/(c*R)-1)\
            *np.exp(-g*(h-11000)/(R*T))
    p = rho*R*T
    T += D_ISA
    rho = p/(R*T)
    a = np.sqrt(gamma*R*T)
    return T, a, p, rho