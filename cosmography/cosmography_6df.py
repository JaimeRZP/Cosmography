from .cosmography_base import CosmographyBase

class Cosmograghy6df(CosmographyBase):
    """
    6df data
    """
    def __init__(self):
        self.data_name = '6df'
        self.z = np.array([0.067])
        self.data = np.array([0.423])
        self.cov = np.array([[0.055**2]])

    
        
