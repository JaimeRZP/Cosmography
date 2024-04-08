from .base import CosmographyBase
import numpy as np

class CMB(CosmographyBase):
    def __init__(self):
        self.data_name = 'CMB'
        self.z = np.array([1089.95]) 
        self.data = np.array([1.04109])
        self.cov = np.array([[0.00030**2]])

        
