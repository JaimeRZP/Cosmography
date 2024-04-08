from .cosmography_base import CosmographyBase

class CosmograghyVipers(CosmographyBase)
    self.data_name = 'Vipers'
    def __init__(self):
        self.z = np.array([0.60, 0.86])
        self.data = np.array([0.55, 0.40])
        self.cov = np.array([[0.12**2, 0], 
                            [0, 0.11**2]])

    def get_redshift(self):
        return self.z
    
    def get_data(self):
        return self.data
    
    def get_cov(self):
        return self.cov
    
        