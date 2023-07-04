import atmosisa as aisa
import components as comp

class engine():
    def __init__(self, eng):
        self.type = eng['type']
        self.m_ar = eng['m_ar']
        h = eng['h']
        M = eng['M']
        self.V = M*aisa.atmosisa(h, unit='ft')[1]
        self.Pa = aisa.atmosisa(h, unit='ft')[2]/1000
        self.Ta = aisa.atmosisa(h, unit='ft')[0]
        self.gamma = eng['gamma']
        self.Cp = eng['Cp']
        #
        #--- Diffuser
        #
        pi_d = eng['pi_d']
        self.P01 = self.Pa*(1+(self.gamma-1)/2 * M**2)**(self.gamma/(self.gamma-1))
        self.T01 = self.Ta*(1+(self.gamma-1)/2 * M**2)
        self.diffuser(pi_d)
        
        if self.type == 'Ramjet':
            self.T03 = self.T02
            self.P03 = self.P02
        else:
            #
            #--- Compressor
            #
            pi_c = eng['pi_c']
            eta_c = eng['eta_c']
            self.compressor(pi_c, eta_c)
        #
        #--- Primary combustor
        #
        self.m_ar = eng['m_ar']
        self.T04 = eng['T_cc']
        pi_cc = eng['pi_cc']
        eta_cc = eng['eta_cc']
        LVC = eng['LVC']
        self.m_f = self.m_ar*self.Cp*(self.T04-self.T03)/\
            (LVC*eta_cc-self.Cp*self.T04)
        self.m_fcc = self.m_f
        self.P04 = self.P03*pi_cc
        if self.type == 'Turbofan':
            #
            #--- Fan
            #
            alpha = eng['alpha']
            sigma = eng['sigma']
            pi_f = eng['pi_f']
            eta_f = eng['eta_f']
            self.fan(pi_f, eta_f, alpha)
            #
            #--- Bypass duct
            #
            pi_byp = eng['pi_byp']
            self.P075 = pi_byp*self.P07
            self.T075 = self.T07   
        elif self.type == 'Turboprop':
            Cwp = eng['Cwp']
            eta_prop = eng['eta_prop']
            self.propeller(Cwp, eta_prop)
        if self.type == 'Ramjet':
            self.T05 = self.T04
            self.P05 = self.P04
        else:
            #
            #--- Turbine
            #
            eta_t = eng['eta_t']
            eta_s = eng['eta_s']
            self.turbine(eta_s, eta_t)
        
        if self.type == 'Turbofan':
            #
            #--- Mixer
            #
            pi_mix = eng['pi_mix']
            self.mixer(pi_mix, alpha, sigma)
            #
            #--- Fan nozzle
            #
            FN_type = eng['FN_type']
            eta_FN = eng['eta_FN']
            self.m9 = alpha*(1-sigma)*self.m_ar
            FN = comp.Nozzle(FN_type, self.m9, self.Pa, self.P07, self.T07, self.Cp, eta_FN)
            self.P9 = FN.P
            self.T9 = FN.T
            self.u9 = FN.u
            self.M9 = FN.M
            self.A9 = FN.A
        else:
            self.P055 = self.P05
            self.T055 = self.T05
            
        if self.type == 'Turbofan':
            self.m8 = self.m_ar+self.m_f+alpha*sigma*self.m_ar
        else:
            self.m8 = self.m_ar+self.m_f
            
        try:
            #
            #--- Afterburn
            #
            pi_ab = eng['pi_ab']
            eta_ab = eng['eta_ab']
            self.P06 = self.P055*pi_ab
            self.T06 = eng['T_ab']
            self.m_fab = (self.m8)*self.Cp*(self.T06-self.T055)/\
                (eta_ab*LVC-self.Cp*self.T06)
            self.m_f += self.m_fab
        except:
            self.P06 = self.P055
            self.T06 = self.T055
            
        #
        #--- Primary nozzle
        #
        PN_type = eng['PN_type']
        eta_PN = eng['eta_PN']
        PN = comp.Nozzle(PN_type, self.m8, self.Pa, self.P06, self.T06, self.Cp, eta_PN)
        self.P8 = PN.P
        self.T8 = PN.T
        self.u8 = PN.u
        self.M8 = PN.M
        self.A8 = PN.A
        if self.type == 'Turbofan':
            self.m_in = alpha*self.m_ar+self.m_ar
        else:
            self.m_in = self.m_ar
        self.thrust()
        self.TSFC = self.m_f/self.F*3600
        self.Power = self.F*self.V
        
        if self.type == 'Turbofan':
            self.Ec = (self.m8)*self.u8**2/2 - self.m9*self.u9**2/2 - self.m_in*self.V**2/2
        else:
            self.Ec = (self.m8)*self.u8**2/2 - self.m_in*self.V**2/2
        self.Eq = self.m_f*LVC*1000
        
        self.n_prop = self.Power/self.Ec
        self.n_th = self.Ec/self.Eq
        self.n_o = self.n_prop*self.n_th
        
    def diffuser(self, pi_d):
        self.P02 = self.P01*pi_d
        self.T02 = self.T01
    
    def compressor(self, pi_c, eta_c):
        self.P03 = pi_c*self.P02
        self.T03i = self.T02*(pi_c)**((self.gamma-1)/self.gamma)
        self.T03 = self.T02 + (self.T03i-self.T02)/eta_c
        self.W_c = self.m_ar*self.Cp*(self.T03-self.T02)
        
    def fan(self, pi_f, eta_f, alpha):
        self.P07 = pi_f*self.P02
        self.T07i = self.T02*(pi_f)**((self.gamma-1)/self.gamma)
        self.T07 = self.T02 + (self.T07i-self.T02)/eta_f
        self.W_f = alpha*self.m_ar*self.Cp*(self.T07-self.T02)
        
    def propeller(self, Cwp, eta_prop):
        self.W_prop = Cwp*self.m_ar*self.Cp*self.Ta
        self.F_prop = Cwp*eta_prop*self.Cp*1000*self.Ta*self.m_ar/self.V
        
    def turbine(self, eta_s,eta_t):
        if self.type == 'Turbofan':
            self.T05 = self.T04 - (self.W_c + self.W_f)/(eta_s*(self.m_ar+self.m_f)*self.Cp)
        elif self.type == 'Turboprop':
            self.T05 = self.T04 - (self.W_c+self.W_prop)/(eta_s*(self.m_ar+self.m_f)*self.Cp)
        else:
            self.T05 = self.T04 - self.W_c/(eta_s*(self.m_ar+self.m_f)*self.Cp)
        self.T05i = self.T04 - (self.T04-self.T05)/eta_t
        self.P05 = self.P04*(self.T05i/self.T04)**(self.gamma/(self.gamma-1))
            
    def mixer(self, pi_mix, alpha, sigma):
        self.P055 = self.P05*pi_mix
        self.T055 = ((1+self.m_f/self.m_ar)*self.Cp*self.T05\
                    +sigma*alpha*self.Cp*self.T075)/((1+self.m_f/self.m_ar)\
                                                    *self.Cp+sigma*alpha*self.Cp)
                                                    
    def thrust(self):
        if self.type == 'Turbofan':
            self.F_mom = self.m8*self.u8 + self.m9*self.u9-self.m_in*self.V
            self.F_pres = self.A8*(self.P8-self.Pa)*1000 + self.A9*(self.P9-self.Pa)*1000
            self.F = self.F_mom + self.F_pres 
        else:
            self.F_mom = self.m8*self.u8 -self.m_in*self.V
            self.F_pres = self.A8*(self.P8-self.Pa)*1000
            
        if self.type == 'Turboprop':
            self.F = self.F_mom + self.F_pres + self.F_prop
        else:
            self.F = self.F_mom + self.F_pres 
            