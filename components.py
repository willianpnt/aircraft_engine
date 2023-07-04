import numpy as np

class Nozzle():
    def __init__(self, nozzle_type, m, Pa, P0, T0, Cp, eta, R = 287.053):
        gamma = Cp*1000/(Cp*1000-R)
        if nozzle_type == 'Converging':
            Pstar = P0*(1+(1-gamma)/(eta*(1+gamma)))**(gamma/(gamma-1))   
            if Pstar > Pa:
                self.P = Pstar
                self.T = 2*T0/(1+gamma)
            else:
                self.P = Pa
                Ti = T0*(self.P/P0)**((gamma-1)/gamma)
                self.T = T0 - eta*(T0-Ti)       
            
        elif nozzle_type == 'Converging-diverging':
            self.P = Pa
            Ti = T0*(self.P/P0)**((gamma-1)/gamma)
            self.T = T0 - eta*(T0-Ti)
            
        self.u = np.sqrt(2000*Cp*abs(T0-self.T))
        self.a = np.sqrt(gamma*R*self.T)
        self.M = self.u/self.a
        self.rho = self.P*1000/(R*self.T)
        self.A = m/(self.rho*self.u)
            
        
