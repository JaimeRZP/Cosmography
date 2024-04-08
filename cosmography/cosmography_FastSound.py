from .cosmography_base import CosmographyBase

class CosmograghyFastSound(CosmographyBase):
    self.data_name = 'FastSound'
    def __init__(self):
        self.z = np.array([1.4])
        self.data = np.array([0.482])
        self.cov = np.array([[0.116**2]])

    def get_redshift(self):
        return self.z
    
    def get_data(self):
        return self.data
    
    def get_cov(self):
        return self.cov
    
        
