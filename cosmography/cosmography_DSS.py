from .cosmography_base import CosmographyBase

class CosmograghyDSS(CosmographyBase)
    self.data_name = 'DSS'
    def __init__(self):
        self.z = np.array([0.0])
        self.data = np.array([0.39])
        self.cov = np.array([[0.022**2]])

    def get_redshift(self):
        return self.z
    
    def get_data(self):
        return self.data
    
    def get_cov(self):
        return self.cov
    
        
