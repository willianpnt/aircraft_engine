import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import engine as eg

f_title = 'Arial 12 bold'
f_normal = 'Arial 10'
f_results = 'Consolas 10'

class GUI_engine():
    def __init__(self, master): 
        self.frame1 = tk.Frame(master)
        self.frame1.pack(anchor= 'w', expand=True, padx =15, pady=10)
        
        self.label = tk.Label(self.frame1)
        self.label['text'] = 'SAA0117 - Propulsão de Aeronaves'
        self.label['font'] = 'Arial 12 bold'
        self.label.pack(anchor='w')
        
        self.label = tk.Label(self.frame1)
        self.label['text'] = 'Author: Willian Leandro dos Santos Pinto'
        self.label['font'] = 'Arial 12'
        self.label.pack(anchor='w')
        
        self.label = tk.Label(self.frame1)
        self.label['text'] = 'This codes suports 4 types of engines: Ramjet, Turbojet, Turbofan and Turboprop'
        self.label['font'] = 'Arial 12'
        self.label.pack(anchor='w')
        
        self.frame1 = tk.Frame(master)
        self.frame1['relief']='groove'
        self.frame1['borderwidth']=3
        self.frame1.pack(fill='both', expand=True, padx =15, pady=10)
        
        self.Label1 = tk.Label(self.frame1, text='Select the engine', font=f_title)
        self.Label1.grid(row=1, sticky='w')
        
        self.type_eng = tk.StringVar()
        self.option1 = tk.Radiobutton(self.frame1, text='Ramjet',\
                                      variable=self.type_eng, value='Ramjet',\
                                          font=f_normal)
        self.option1.grid(row=2, sticky='w')
        self.option2 = tk.Radiobutton(self.frame1, text='Turbojet',\
                                      variable=self.type_eng, value='Turbojet',\
                                          font=f_normal)
        self.option2.grid(row=3, sticky='w')
        self.option3 = tk.Radiobutton(self.frame1, text='Turbofan',\
                                      variable=self.type_eng, value='Turbofan',\
                                          font='Arial 10')
        self.option3.grid(row=4, sticky='w')
        self.option4 = tk.Radiobutton(self.frame1, text='Turboprop',\
                                      variable=self.type_eng, value='Turboprop',\
                                          font='Arial 10')
        self.option4.grid(row=5, sticky='w')
        
        self.frameb = tk.Frame(master)
        self.frameb.pack(fill = 'both', expand = True, padx = 10, pady = 10)
        
        self.button1 = tk.Button(self.frameb, text='Next', font=f_normal)
        self.button1.pack()
        self.button1['command'] = self.window1
        
    def window1(self):
        self.engine_info=dict()
        self.engine_info['type'] =self.type_eng.get()
        self.engine_info['ab'] = False
        self.w1 = tk.Tk()
        self.w1.title(self.engine_info['type'])
        self.w1.resizable(False, False)
        if self.engine_info['type'] == 'Ramjet':
            self.ramjet()
        else:
            self.engines()
            
    def ramjet(self):
        self.frame2 = tk.LabelFrame(self.w1, text='General informations', font = f_title)
        self.frame2.grid(row=0, column=0, padx = 10, pady = 10, stick='news')
        
        self.frame3 = tk.LabelFrame(self.w1, text='Diffuser', font = f_title)
        self.frame3.grid(row=1, column=0, padx = 10, pady = 10, sticky='news')
        
        self.frame4 = tk.LabelFrame(self.w1, text='Burner', font = f_title)
        self.frame4.grid(row=0, column=1, padx = 10, pady = 10, sticky='news')
        
        self.frame5 = tk.LabelFrame(self.w1, text='Nozzle', font = f_title)
        self.frame5.grid(row=1, column=1, padx = 10, pady = 10, sticky='news')
        
        self.frame6 = tk.Frame(self.w1)
        self.frame6.grid(row=3, column=0, columnspan=3, padx = 10, pady = 10, sticky='news')
        
        self.label=tk.Label(self.frame2, text='Altitude [ft]:', font=f_normal)
        self.label.grid(row=0,column=1, sticky='w')
        self.h=tk.Entry(self.frame2, width=10, font=f_normal)
        self.h.grid(row=0,column=2, sticky='e')
        
        self.label=tk.Label(self.frame2, text='Mach number [-]:', font=f_normal)
        self.label.grid(row=1,column=1, sticky='w')
        self.M=tk.Entry(self.frame2, width=10, font=f_normal)
        self.M.grid(row=1,column=2, sticky='e')
        
        self.label=tk.Label(self.frame2, text='Flux of air [kg/s]:', font=f_normal)
        self.label.grid(row=2,column=1, sticky='w')
        self.m_ar = tk.Entry(self.frame2, width=10, font=f_normal)
        self.m_ar.grid(row=2,column=2, sticky='e')
        
        self.label=tk.Label(self.frame2, text='Gamma [-]:', font=f_normal)
        self.label.grid(row=3,column=1, sticky='w')
        self.gamma=tk.Entry(self.frame2, width=10, font=f_normal)
        self.gamma.grid(row=3,column=2, sticky='e')
        
        self.label=tk.Label(self.frame2, text='Specific heat [kJ/kg.K]:', font=f_normal)
        self.label.grid(row=4,column=1, sticky='w')
        self.Cp=tk.Entry(self.frame2, width=10, font=f_normal)
        self.Cp.grid(row=4,column=2, sticky='e')
        
        self.label=tk.Label(self.frame3, text='Pressure ratio [-]:', font=f_normal)
        self.label.grid(row=0,column=1, sticky='w')
        self.pi_d=tk.Entry(self.frame3, width=10, font=f_normal)
        self.pi_d.grid(row=0,column=2, sticky='e')
        
        self.label=tk.Label(self.frame4, text='Temperature [K]:', font=f_normal)
        self.label.grid(row=0,column=1, sticky='w')
        self.T_cc=tk.Entry(self.frame4, width=10, font=f_normal)
        self.T_cc.grid(row=0,column=2, sticky='e')
        
        self.label=tk.Label(self.frame4, text='Pressure ratio [-]:', font=f_normal)
        self.label.grid(row=1,column=1, sticky='w')
        self.pi_cc=tk.Entry(self.frame4, width=10, font=f_normal)
        self.pi_cc.grid(row=1,column=2, sticky='e')
        
        self.label=tk.Label(self.frame4, text='LVC [kJ/kg]:', font=f_normal)
        self.label.grid(row=2,column=1, sticky='w')
        self.LVC=tk.Entry(self.frame4, width=10, font=f_normal)
        self.LVC.grid(row=2,column=2, sticky='e')
        
        self.label=tk.Label(self.frame4, text='Efficiency [-]:', font=f_normal)
        self.label.grid(row=3,column=1, sticky='w')
        self.eta_cc=tk.Entry(self.frame4, width=10, font=f_normal)
        self.eta_cc.grid(row=3,column=2, sticky='e')
        
        self.ab = tk.Checkbutton(self.frame4, text='Afterburn', command=self.afterburn, 
                                 font=f_normal)
        self.ab.grid(row=4,column=1, sticky='w')
        
        self.label=tk.Label(self.frame5, text='Nozzle type [-]:', font=f_normal)
        self.label.grid(row=0,column=1, sticky='w')
        self.PN_type = ttk.Combobox(self.frame5, width =20)
        self.PN_type['values'] = ['Converging', 'Converging-diverging']
        self.PN_type.grid(row=0, column=2, sticky='e')
        
        self.label=tk.Label(self.frame5, text='Efficiency [-]:', font=f_normal)
        self.label.grid(row=1,column=1, sticky='w')
        self.eta_PN=tk.Entry(self.frame5, width=20, font=f_normal)
        self.eta_PN.grid(row=1,column=2, sticky='e')
        
        self.button2 = tk.Button(self.frame6, text= 'Calculate', font=f_normal)
        self.button2.pack(side='right')
        self.button2['command'] = self.calculate
        self.button2 = tk.Button(self.frame6, text= 'Return', font=f_normal)
        self.button2.pack(side='right')
        self.button2['command'] = self.w1.destroy
    
    def engines(self):
        self.frame2 = tk.LabelFrame(self.w1, text='General informations', font = f_title)
        self.frame2.grid(row=0, column=0, padx = 10, pady = 10, stick='news')
        
        self.frame3 = tk.LabelFrame(self.w1, text='Diffuser', font = f_title)
        self.frame3.grid(row=1, column=0, rowspan=2, padx = 10, pady = 10, sticky='news')
        
        self.frame4 = tk.LabelFrame(self.w1, text='Compressor', font = f_title)
        self.frame4.grid(row=3, column=0, padx = 10, pady = 10, sticky='news')
        
        self.frame5 = tk.LabelFrame(self.w1, text='Burner', font = f_title)
        self.frame5.grid(row=0, column=1, padx = 10, pady = 10, sticky='news')
        
        self.frame6 = tk.LabelFrame(self.w1, text='Turbine and Shaft', font = f_title)
        self.frame6.grid(row=1, column=1, rowspan=2, padx = 10, pady = 10, sticky='news')
        
        self.frame7 = tk.LabelFrame(self.w1, text='Primary nozzle', font = f_title)
        self.frame7.grid(row=3, column=1, padx = 10, pady = 10, sticky='news')
        
        self.label=tk.Label(self.frame2, text='Altitude [ft]:', font=f_normal)
        self.label.grid(row=0,column=1, sticky='w')
        self.h=tk.Entry(self.frame2, width=10, font=f_normal)
        self.h.grid(row=0,column=2, sticky='e')
        
        self.label=tk.Label(self.frame2, text='Mach number [-]:', font=f_normal)
        self.label.grid(row=1,column=1, sticky='w')
        self.M=tk.Entry(self.frame2, width=10, font=f_normal)
        self.M.grid(row=1,column=2, sticky='e')
        
        self.label=tk.Label(self.frame2, text='Flux of air [kg/s]:', font=f_normal)
        self.label.grid(row=2,column=1, sticky='w')
        self.m_ar = tk.Entry(self.frame2, width=10, font=f_normal)
        self.m_ar.grid(row=2,column=2, sticky='e')
        
        self.label=tk.Label(self.frame2, text='Gamma [-]:', font=f_normal)
        self.label.grid(row=3,column=1, sticky='w')
        self.gamma=tk.Entry(self.frame2, width=10, font=f_normal)
        self.gamma.grid(row=3,column=2, sticky='e')
        
        self.label=tk.Label(self.frame2, text='Specific heat [kJ/kg.K]:', font=f_normal)
        self.label.grid(row=4,column=1, sticky='w')
        self.Cp=tk.Entry(self.frame2, width=10, font=f_normal)
        self.Cp.grid(row=4,column=2, sticky='e')
        
        self.label=tk.Label(self.frame3, text='Pressure ratio [-]:', font=f_normal)
        self.label.grid(row=0,column=1, sticky='w')
        self.pi_d=tk.Entry(self.frame3, width=10, font=f_normal)
        self.pi_d.grid(row=0,column=2, sticky='e') 
        
        self.label=tk.Label(self.frame4, text='Pressure ratio [-]:', font=f_normal)
        self.label.grid(row=0,column=1, sticky='w')
        self.pi_c=tk.Entry(self.frame4, width=10, font=f_normal)
        self.pi_c.grid(row=0,column=2, sticky='e')
        
        self.label=tk.Label(self.frame4, text='Efficiency [-]:', font=f_normal)
        self.label.grid(row=1,column=1, sticky='w')
        self.eta_c=tk.Entry(self.frame4, width=10, font=f_normal)
        self.eta_c.grid(row=1,column=2, sticky='e')
        
        self.label=tk.Label(self.frame5, text='Temperature [K]:', font=f_normal)
        self.label.grid(row=0,column=1, sticky='w')
        self.T_cc=tk.Entry(self.frame5, width=10, font=f_normal)
        self.T_cc.grid(row=0,column=2, sticky='e')
        
        self.label=tk.Label(self.frame5, text='Pressure ratio [-]:', font=f_normal)
        self.label.grid(row=1,column=1, sticky='w')
        self.pi_cc=tk.Entry(self.frame5, width=10, font=f_normal)
        self.pi_cc.grid(row=1,column=2, sticky='e')
            
        self.label=tk.Label(self.frame5, text='Efficiency [-]:', font=f_normal)
        self.label.grid(row=2,column=1, sticky='w')
        self.eta_cc=tk.Entry(self.frame5, width=10, font=f_normal)
        self.eta_cc.grid(row=2,column=2, sticky='e')
        
        self.label=tk.Label(self.frame5, text='LVC [kJ/kg]:', font=f_normal)
        self.label.grid(row=3,column=1, sticky='w')
        self.LVC=tk.Entry(self.frame5, width=10, font=f_normal)
        self.LVC.grid(row=3,column=2, sticky='e')
        
        self.checkbox = tk.Checkbutton(self.frame5, text='Afterburn', command=self.afterburn, font=f_normal)
        self.checkbox.grid(row=4,column=1, sticky='w')
        
        self.label=tk.Label(self.frame6, text='Shaft efficiency [-]:', font=f_normal)
        self.label.grid(row=0,column=1, sticky='w')
        self.eta_s=tk.Entry(self.frame6, width=10, font=f_normal)
        self.eta_s.grid(row=0,column=2, sticky='e')
        
        self.label=tk.Label(self.frame6, text='Turbine efficiency [-]:', font=f_normal)
        self.label.grid(row=2,column=1, sticky='w')
        self.eta_t=tk.Entry(self.frame6, width=10, font=f_normal)
        self.eta_t.grid(row=2,column=2, sticky='e')
        
        self.label=tk.Label(self.frame7, text='Nozzle type [-]:', font=f_normal)
        self.label.grid(row=0,column=1, sticky='w')
        self.PN_type = ttk.Combobox(self.frame7, width =20)
        self.PN_type['values'] = ['Converging', 'Converging-diverging']
        self.PN_type.grid(row=0, column=2, sticky='e')
        
        self.label=tk.Label(self.frame7, text='Efficiency [-]:', font=f_normal)
        self.label.grid(row=1,column=1, sticky='w')
        self.eta_PN=tk.Entry(self.frame7, width=20, font=f_normal)
        self.eta_PN.grid(row=1,column=2, sticky='e')
        
        if self.engine_info['type'] == 'Turbofan':
            self.frame9 = tk.LabelFrame(self.w1, text='Fan', font=f_title)
            self.frame9.grid(row=0, column=2, padx=10, pady=10, sticky='news')
            
            self.frame10 = tk.LabelFrame(self.w1, text='Bypass duct', font=f_title)
            self.frame10.grid(row=1, column=2, padx=10, pady=10, sticky='news')
            
            self.frame11 = tk.LabelFrame(self.w1, text='Mixer', font=f_title)
            self.frame11.grid(row=2, column=2, padx=10, pady=10, sticky='news')
            
            self.frame12 = tk.LabelFrame(self.w1, text='Fan nozzle', font=f_title)
            self.frame12.grid(row=3, column=2, padx=10, pady=10, sticky='news')
            
            self.label = tk.Label(self.frame9, text='Bypass ratio [-]:', font=f_normal)
            self.label.grid(row=0, column=0, sticky='w')
            self.alpha = tk.Entry(self.frame9, width=10, font=f_normal)
            self.alpha.grid(row=0, column=1, sticky='e')
            
            self.label = tk.Label(self.frame9, text='Split ratio [-]:', font=f_normal)
            self.label.grid(row=1, column=0, sticky='w')
            self.sigma = tk.Entry(self.frame9, width=10, font=f_normal)
            self.sigma.grid(row=1, column=1, sticky='e')
            
            self.label = tk.Label(self.frame9, text='Pressure ratio [-]:', font=f_normal)
            self.label.grid(row=2, column=0, sticky='w')
            self.pi_f = tk.Entry(self.frame9, width=10, font=f_normal)
            self.pi_f.grid(row=2, column=1, sticky='e')
            
            self.label = tk.Label(self.frame9, text='Efficiency [-]:', font=f_normal)
            self.label.grid(row=3, column=0, sticky='w')
            self.eta_f = tk.Entry(self.frame9, width=10, font=f_normal)
            self.eta_f.grid(row=3, column=1, sticky='e')
            
            self.label = tk.Label(self.frame10, text='Pressure ratio [-]:', font=f_normal)
            self.label.grid(row=0, column=0, sticky='w')
            self.pi_byp = tk.Entry(self.frame10, width=10, font=f_normal)
            self.pi_byp.grid(row=0, column=1, sticky='e')
            
            self.label = tk.Label(self.frame11, text='Pressure ratio [-]:', font=f_normal)
            self.label.grid(row=0, column=0, sticky='w')
            self.pi_mix = tk.Entry(self.frame11, width=10, font=f_normal)
            self.pi_mix.grid(row=0, column=1, sticky='e')
            
            self.label=tk.Label(self.frame12, text='Nozzle type [-]:', font=f_normal)
            self.label.grid(row=0,column=1, sticky='w')
            self.FN_type = ttk.Combobox(self.frame12, width =20)
            self.FN_type['values'] = ['Converging', 'Converging-diverging']
            self.FN_type.grid(row=0, column=2, sticky='e')
            
            self.label=tk.Label(self.frame12, text='Efficiency [-]:', font=f_normal)
            self.label.grid(row=1,column=1, sticky='w')
            self.eta_FN=tk.Entry(self.frame12, width=20, font=f_normal)
            self.eta_FN.grid(row=1,column=2, sticky='e')
        
        elif self.engine_info['type'] == 'Turboprop':
            self.frame9 = tk.LabelFrame(self.w1, text='Propeller', font=f_title)
            self.frame9.grid(row=0, column=2, padx=10, pady=10, sticky='news')
            
            self.label = tk.Label(self.frame9, text='Work coefficient [-]:', font=f_normal)
            self.label.grid(row=0, column=0, sticky='w')
            self.Cwp = tk.Entry(self.frame9, width=10, font=f_normal)
            self.Cwp.grid(row=0, column=1, sticky='e')
            
            self.label = tk.Label(self.frame9, text='Efficiency [-]:', font=f_normal)
            self.label.grid(row=1, column=0, sticky='w')
            self.eta_prop = tk.Entry(self.frame9, width=10, font=f_normal)
            self.eta_prop.grid(row=1, column=1, sticky='e')

        self.frame8 = tk.Frame(self.w1)
        self.frame8.grid(row=4, column=0, columnspan=3, padx = 10, pady = 10, sticky='news')

        self.button2 = tk.Button(self.frame8, text= 'Calculate', font=f_normal)
        self.button2.pack(side='right')
        self.button2['command'] = self.calculate
        self.button2 = tk.Button(self.frame8, text= 'Return', font=f_normal)
        self.button2.pack(side='right')
        self.button2['command'] = self.w1.destroy
        
    def afterburn(self):
        if not self.engine_info['ab']:
            self.engine_info['ab'] =  True
            self.w2 = tk.Tk()
            self.w2.title('Afterburn')
            self.w2.resizable(False, False)
            self.frame9 = tk.Frame(self.w2)
            self.frame9.pack(fill='both', expand=True, padx = 10, pady=10)
            
            self.frame10 = tk.Frame(self.w2)
            self.frame10.pack(fill='both', expand=True, padx = 10, pady=10)
            
            self.label = tk.Label(self.frame9, text='Afterburn temperature [K]:', font=f_normal)
            self.label.grid(row=0, column=0, sticky='w')
            self.T_ab = tk.Entry(self.frame9, width=20, font=f_normal)
            self.T_ab.grid(row=0, column=1)
            
            self.label = tk.Label(self.frame9, text='Pressure ratio [-]:', font=f_normal)
            self.label.grid(row=1, column=0, sticky='w')
            self.pi_ab = tk.Entry(self.frame9, width=20, font=f_normal)
            self.pi_ab.grid(row=1, column=1)
            
            self.label = tk.Label(self.frame9, text='Efficiency [-]:', font=f_normal)
            self.label.grid(row=2, column=0, sticky='w')
            self.eta_ab = tk.Entry(self.frame9, width=20, font=f_normal)
            self.eta_ab.grid(row=2, column=1)
            
            self.button3 = tk.Button(self.frame10, text = 'Enter', font=f_normal)
            self.button3.pack(side='right')
            self.button3['command'] = self.set_afterburn
        else:
            if 'pi_ab' in self.engine_info:
                self.engine_info.pop('pi_ab')
                self.engine_info.pop('eta_ab')
                self.engine_info.pop('T_ab')
            self.engine_info['ab'] = False
            try:
                self.w2.destroy()
            except:
                pass
        
    def set_afterburn(self):
        self.engine_info['pi_ab'] = float(self.pi_ab.get())
        self.engine_info['eta_ab'] = float(self.eta_ab.get())
        self.engine_info['T_ab'] = float(self.T_ab.get())
        self.w2.destroy()
        
    def calculate(self):
        if self.engine_info['type'] == 'Ramjet':
            self.engine_info['h'] = float(self.h.get())
            self.engine_info['M'] = float(self.M.get())
            self.engine_info['m_ar'] = float(self.m_ar.get())
            self.engine_info['gamma'] = float(self.gamma.get())
            self.engine_info['Cp'] = float(self.Cp.get())
            
            self.engine_info['pi_d'] = float(self.pi_d.get())
            
            self.engine_info['T_cc'] = float(self.T_cc.get())
            self.engine_info['pi_cc'] = float(self.pi_cc.get())
            self.engine_info['eta_cc'] = float(self.eta_cc.get())
            self.engine_info['LVC'] = float(self.LVC.get())
            
            self.engine_info['PN_type'] = self.PN_type.get()
            self.engine_info['eta_PN'] = float(self.eta_PN.get())
        else:
            self.engine_info['h'] = float(self.h.get())
            self.engine_info['M'] = float(self.M.get())
            self.engine_info['m_ar'] = float(self.m_ar.get())
            self.engine_info['LVC'] = float(self.LVC.get())
            self.engine_info['gamma'] = float(self.gamma.get())
            self.engine_info['Cp'] = float(self.Cp.get())

            self.engine_info['pi_d'] = float(self.pi_d.get())

            self.engine_info['pi_c'] = float(self.pi_c.get())
            self.engine_info['eta_c'] = float(self.eta_c.get())
        #--- Combustion chamber
            self.engine_info['T_cc'] = float(self.T_cc.get())
            self.engine_info['pi_cc'] = float(self.pi_cc.get())
            self.engine_info['eta_cc'] = float(self.eta_cc.get())
            self.engine_info['LVC'] = float(self.LVC.get())
            
        #--- Turbine and shaft
            self.engine_info['eta_s'] = float(self.eta_s.get())
            self.engine_info['eta_t'] = float(self.eta_t.get())

        #--- Primary nozzle
            self.engine_info['PN_type'] = self.PN_type.get()
            self.engine_info['eta_PN'] = float(self.eta_PN.get())
            if self.engine_info['type'] == 'Turbofan':
                self.engine_info['alpha'] = float(self.alpha.get())
                self.engine_info['sigma'] = float(self.sigma.get())
                self.engine_info['pi_f'] = float(self.pi_f.get())
                self.engine_info['eta_f'] = float(self.eta_f.get())
                self.engine_info['pi_byp'] = float(self.pi_byp.get())
                self.engine_info['pi_mix'] = float(self.pi_mix.get())
                self.engine_info['FN_type'] = self.FN_type.get()
                self.engine_info['eta_FN'] = float(self.eta_FN.get())
            elif self.engine_info['type'] == 'Turboprop':
                self.engine_info['Cwp'] = float(self.Cwp.get())
                self.engine_info['eta_prop'] = float(self.eta_prop.get())
        self.engine = eg.engine(self.engine_info)
        self.show_results()
        
    def show_results(self):
        self.w4 = tk.Tk()
        self.w4.title('Results')
        self.w4.minsize(width=300, height =500)
        self.w4.resizable(False, False)
        frame = tk.Frame(self.w4, bg= 'white')
        frame.grid(row=0, column=0, padx=10, pady=10, sticky='news')
        if self.engine_info['type'] == 'Ramjet':
            label = tk.Label(frame, bg ='white')
            label['text'] = 'Inlet'
            label['font'] = 'Consolas 12 bold'
            label.pack(anchor='w', pady=5)
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'V = ' + str(round(self.engine.V,1)) + ' m/s'
            label['font'] = f_results
            label.pack(anchor='w')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'Pa = ' + str(round(self.engine.Pa,1)) + ' kPa'
            label['font'] = f_results
            label.pack(anchor='w')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'Ta = ' + str(round(self.engine.Ta,1)) + ' K'
            label['font'] = f_results
            label.pack(anchor='w')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'P0a = ' + str(round(self.engine.P01,1)) + ' kPa'
            label['font'] = f_results
            label.pack(anchor='w')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'T0a = ' + str(round(self.engine.T01,1)) + ' K'
            label['font'] = f_results
            label.pack(anchor='w')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'Diffuser'
            label['font'] = 'Consolas 12 bold'
            label.pack(anchor='w',pady=5)
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'P03 = ' + str(round(self.engine.P03,1)) + ' kPa'
            label['font'] = f_results
            label.pack(anchor='w')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'T03 = ' + str(round(self.engine.T03,1)) + ' K'
            label['font'] = f_results
            label.pack(anchor='w')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'Burner'
            label['font'] = 'Consolas 12 bold'
            label.pack(anchor='w',pady=5)
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'mf = ' + str(round(self.engine.m_f,3)) + ' kg/s'
            label['font'] = f_results
            label.pack(anchor='w')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'P04 = ' + str(round(self.engine.P04,1)) + ' kPa'
            label['font'] = f_results
            label.pack(anchor='w')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'T04 = ' + str(round(self.engine.T04,1)) + ' K'
            label['font'] = f_results
            label.pack(anchor='w')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'Nozzle'
            label['font'] = 'Consolas 12 bold'
            label.pack(anchor='w',pady=5)
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'P08 = ' + str(round(self.engine.P06,1)) + ' kPa'
            label['font'] = f_results
            label.pack(anchor='w')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'T08 = ' + str(round(self.engine.T06,1)) + ' K'
            label['font'] = f_results
            label.pack(anchor='w')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'P8 = ' + str(round(self.engine.P8,1)) + ' kPa'
            label['font'] = f_results
            label.pack(anchor='w')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'T8 = ' + str(round(self.engine.T8,1)) + ' K'
            label['font'] = f_results
            label.pack(anchor='w')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'M8 = ' + str(round(self.engine.M8,3))
            label['font'] = f_results
            label.pack(anchor='w')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'u8 = ' + str(round(self.engine.u8,1)) + ' m/s'
            label['font'] = f_results
            label.pack(anchor='w')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'A8 = ' + str(round(self.engine.A8,3)) + ' m2'
            label['font'] = f_results
            label.pack(anchor='w')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'Output'
            label['font'] = 'Consolas 12 bold'
            label.pack(anchor='w', pady=5)
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'F = ' + str(round(self.engine.F, 1)) + ' N'
            label['font'] = f_results
            label.pack(anchor='w')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'TSFC = ' + str(round(self.engine.TSFC,3)) + ' kg/h/N'
            label['font'] = f_results
            label.pack(anchor='w')    
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'Net power = ' + str(round(self.engine.Power*1.34102/1000,1)) + ' hp'
            label['font'] = f_results
            label.pack(anchor='w')
            
        else:
            label = tk.Label(frame, bg ='white')
            label['text'] = 'Inlet'
            label['font'] = 'Consolas 12 bold'
            label.pack(anchor='w', pady=5)
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'V = ' + str(round(self.engine.V,1)) + ' m/s'
            label['font'] = f_results
            label.pack(anchor='w')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'Pa = ' + str(round(self.engine.Pa,1)) + ' kPa'
            label['font'] = f_results
            label.pack(anchor='w')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'Ta = ' + str(round(self.engine.Ta,1)) + ' K'
            label['font'] = f_results
            label.pack(anchor='w')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'P0a = ' + str(round(self.engine.P01,1)) + ' kPa'
            label['font'] = f_results
            label.pack(anchor='w')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'T0a = ' + str(round(self.engine.T01,1)) + ' K'
            label['font'] = f_results
            label.pack(anchor='w')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'Diffuser'
            label['font'] = 'Consolas 12 bold'
            label.pack(anchor='w',pady=5)
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'P02 = ' + str(round(self.engine.P02,1)) + ' kPa'
            label['font'] = f_results
            label.pack(anchor='w')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'T02 = ' + str(round(self.engine.T02,1)) + ' K'
            label['font'] = f_results
            label.pack(anchor='w')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'Compressor'
            label['font'] = 'Consolas 12 bold'
            label.pack(anchor='w',pady=5)
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'P03 = ' + str(round(self.engine.P03,1)) + ' kPa'
            label['font'] = f_results
            label.pack(anchor='w')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'T03 = ' + str(round(self.engine.T03,1)) + ' K'
            label['font'] = f_results
            label.pack(anchor='w')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'Burner'
            label['font'] = 'Consolas 12 bold'
            label.pack(anchor='w',pady=5)
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'mf = ' + str(round(self.engine.m_fcc,3)) + ' kg/s'
            label['font'] = f_results
            label.pack(anchor='w')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'P04 = ' + str(round(self.engine.P04,1)) + ' kPa'
            label['font'] = f_results
            label.pack(anchor='w')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'T04 = ' + str(round(self.engine.T04,1)) + ' K'
            label['font'] = f_results
            label.pack(anchor='w')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'Turbine'
            label['font'] = 'Consolas 12 bold'
            label.pack(anchor='w',pady=5)
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'P05 = ' + str(round(self.engine.P05,1)) + ' kPa'
            label['font'] = f_results
            label.pack(anchor='w')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'T05 = ' + str(round(self.engine.T05,1)) + ' K'
            label['font'] = f_results
            label.pack(anchor='w')
            
            if self.engine_info['type'] == 'Turbofan':
                label = tk.Label(frame, bg ='white')
                label['text'] = 'Fan'
                label['font'] = 'Consolas 12 bold'
                label.pack(anchor='w',pady=5)
                
                label = tk.Label(frame, bg ='white')
                label['text'] = 'P07 = ' + str(round(self.engine.P07,1)) + ' kPa'
                label['font'] = f_results
                label.pack(anchor='w')
                
                label = tk.Label(frame, bg ='white')
                label['text'] = 'T07 = ' + str(round(self.engine.T07,1)) + ' K'
                label['font'] = f_results
                label.pack(anchor='w')
                
                label = tk.Label(frame, bg ='white')
                label['text'] = 'Fan nozzle'
                label['font'] = 'Consolas 12 bold'
                label.pack(anchor='w',pady=5)
                
                label = tk.Label(frame, bg ='white')
                label['text'] = 'P9 = ' + str(round(self.engine.P9,1)) + ' kPa'
                label['font'] = f_results
                label.pack(anchor='w')
                
                label = tk.Label(frame, bg ='white')
                label['text'] = 'T9 = ' + str(round(self.engine.T9,1)) + ' K'
                label['font'] = f_results
                label.pack(anchor='w')
                
                label = tk.Label(frame, bg ='white')
                label['text'] = 'M9 = ' + str(round(self.engine.M9,3))
                label['font'] = f_results
                label.pack(anchor='w')
                
                label = tk.Label(frame, bg ='white')
                label['text'] = 'u9 = ' + str(round(self.engine.u9,1)) + ' m/s'
                label['font'] = f_results
                label.pack(anchor='w')
                
                label = tk.Label(frame, bg ='white')
                label['text'] = 'A9 = ' + str(round(self.engine.A9,3)) + ' m2'
                label['font'] = f_results
                label.pack(anchor='w')
                
                frame = tk.Frame(self.w4, bg= 'white')
                frame.grid(row=0, column=1, padx=10, pady=10, sticky='news')
                
                label = tk.Label(frame, bg ='white')
                label['text'] = 'Bypass duct'
                label['font'] = 'Consolas 12 bold'
                label.pack(anchor='w',pady=5)
                
                label = tk.Label(frame, bg ='white')
                label['text'] = 'P075 = ' + str(round(self.engine.P075,1)) + ' kPa'
                label['font'] = f_results
                label.pack(anchor='w')
                
                label = tk.Label(frame, bg ='white')
                label['text'] = 'T075 = ' + str(round(self.engine.T075,1)) + ' K'
                label['font'] = f_results
                label.pack(anchor='w')
                
                label = tk.Label(frame, bg ='white')
                label['text'] = 'Mixer'
                label['font'] = 'Consolas 12 bold'
                label.pack(anchor='w',pady=5)
                
                label = tk.Label(frame, bg ='white')
                label['text'] = 'P055 = ' + str(round(self.engine.P055,1)) + ' kPa'
                label['font'] = f_results
                label.pack(anchor='w')
                
                label = tk.Label(frame, bg ='white')
                label['text'] = 'T055 = ' + str(round(self.engine.T055,1)) + ' K'
                label['font'] = f_results
                label.pack(anchor='w')
            
            if self.engine_info['ab']:
                label = tk.Label(frame, bg ='white')
                label['text'] = 'Afterburn'
                label['font'] = 'Consolas 12 bold'
                label.pack(anchor='w',pady=5)
                
                label = tk.Label(frame, bg ='white')
                label['text'] = 'P06 = ' + str(round(self.engine.P06,1)) + ' kPa'
                label['font'] = f_results
                label.pack(anchor='w')
                
                label = tk.Label(frame, bg ='white')
                label['text'] = 'T06 = ' + str(round(self.engine.T06,1)) + ' K'
                label['font'] = f_results
                label.pack(anchor='w')
                
                label = tk.Label(frame, bg ='white')
                label['text'] = 'm_fab = ' + str(round(self.engine.m_fab,3)) + ' kg/s'
                label['font'] = f_results
                label.pack(anchor='w')
                
            if not self.engine_info['type'] == 'Turbofan':
                frame = tk.Frame(self.w4, bg= 'white')
                frame.grid(row=0, column=1, padx=10, pady=10, sticky='news')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'Primary nozzle'
            label['font'] = 'Consolas 12 bold'
            label.pack(anchor='w',pady=5)
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'P06 = ' + str(round(self.engine.P06,1)) + ' kPa'
            label['font'] = f_results
            label.pack(anchor='w')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'T06 = ' + str(round(self.engine.T06,1)) + ' K'
            label['font'] = f_results
            label.pack(anchor='w')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'P8 = ' + str(round(self.engine.P8,1)) + ' kPa'
            label['font'] = f_results
            label.pack(anchor='w')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'T8 = ' + str(round(self.engine.T8,1)) + ' K'
            label['font'] = f_results
            label.pack(anchor='w')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'M8 = ' + str(round(self.engine.M8,3))
            label['font'] = f_results
            label.pack(anchor='w')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'u8 = ' + str(round(self.engine.u8,1)) + ' m/s'
            label['font'] = f_results
            label.pack(anchor='w')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'A8 = ' + str(round(self.engine.A8,3)) + ' m2'
            label['font'] = f_results
            label.pack(anchor='w')
            
            if self.engine_info['type'] == 'Turboprop':
                label = tk.Label(frame, bg ='white')
                label['text'] = 'Propeller'
                label['font'] = 'Consolas 12 bold'
                label.pack(anchor='w',pady=5)
                
                label = tk.Label(frame, bg ='white')
                label['text'] = 'F = ' + str(round(self.engine.F_prop,3)) + ' N'
                label['font'] = f_results
                label.pack(anchor='w')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'Output'
            label['font'] = 'Consolas 12 bold'
            label.pack(anchor='w', pady=5)  
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'F = ' + str(round(self.engine.F, 1)) + ' N'
            label['font'] = f_results
            label.pack(anchor='w')
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'TSFC = ' + str(round(self.engine.TSFC,3)) + ' kg/h/N'
            label['font'] = f_results
            label.pack(anchor='w')    
            
            label = tk.Label(frame, bg ='white')
            label['text'] = 'Net power = ' + str(round(self.engine.Power*1.34102/1000,1)) + ' hp'
            label['font'] = f_results
            label.pack(anchor='w')   
                   
root = tk.Tk()
root.resizable(False, False)
root.title('Engines')
GUI_engine(root)
root.mainloop()