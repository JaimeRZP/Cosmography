from .cosmography_base import CosmographyBase
import numpy as np
from pandas import read_table

class CosmograghyDS17(CosmographyBase)
    self.data_name = 'DS17'
    def __init__(self):
        self.path = "../data/PantheonDS17/"
        SN = _read_light_curve_parameters()
        self.z = np.array(SN.zcmb)
        self.data = np.array(SN.mb)
        base_cov = np.genfromtxt(self.path+'syscov_panth.txt') 
        self.cov = base_cov + np.diag(SN.dmb**2)
    
    def _read_light_curve_parameters(self):
        with open(self.path+"lcparam_DS17f.txt", 'r') as text:
            clean_first_line = text.readline()[1:].strip()
            names = [e.strip().replace('3rd', 'third')
                    for e in clean_first_line.split()]

        lc_parameters = read_table(
            path, sep=' ', names=names, header=0, index_col=False)
        return lc_parameters
        
