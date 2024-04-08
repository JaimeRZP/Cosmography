from .cosmography_base import CosmographyBase

class CosmograghyWigglez(CosmographyBase):
    self.data_name = 'Wigglez'
    def __init__(self):
        self.z = np.array([0.44, 0.60, 0.73])
        self.data =  np.array([0.413, 0.390, 0.437])
        cov_no_jitter = np.array([[6.4, 2.57, 0], 
                                [2.57,3.969, 2.54], 
                                [0, 2.54, 5.184]])
        self.cov = 10**(-3)*cov_no_jitter

    
        
