from .cosmography_base import CosmographyBase

class CosmograghyFastSound(CosmographyBase):
    self.data_name = 'FastSound'
    def __init__(self):
        self.z = np.array([1.4])
        self.data = np.array([0.482])
        self.cov = np.array([[0.116**2]])

    
        
