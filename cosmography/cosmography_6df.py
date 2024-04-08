from .cosmography_base import CosmographyBase

class Cosmograghy6df(CosmographyBase):
    self.data_name = '6df'
    def __init__(self):
        self.z = np.array([0.067])
        self.data = np.array([0.423])
        self.cov = np.array([[0.055**2]])

    def get_redshift(self):
        return self.z
    
    def get_data(self):
        return self.data
    
    def get_cov(self):
        return self.cov
    
        
