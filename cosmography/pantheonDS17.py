from .base import CosmographyBase
import numpy as np


class PantheonDS17(CosmographyBase):
    def __init__(self, path='../data/PantheonDS17/'):
        self.data_name = 'PantheonDS17'
        SN = np.transpose(np.loadtxt(path+'lcparam_DS17f.txt',
                                     usecols=(1, 4, 5)))
        self.z = np.array(SN[0])
        self.data = np.array(SN[1])
        base_cov = np.loadtxt(path+'syscov_panth.txt')
        self.cov = base_cov + np.diag(SN[2]**2)
