from .base import CosmographyBase
import numpy as np

class Vipers(CosmographyBase):
    def __init__(self):
        self.data_name = 'Vipers'
        self.z = np.array([0.60, 0.86])
        self.data = np.array([0.55, 0.40])
        self.cov = np.array([[0.12**2, 0], 
                            [0, 0.11**2]])

    
        
