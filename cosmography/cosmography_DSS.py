from .cosmography_base import CosmographyBase

class CosmograghyDSS(CosmographyBase):
    def __init__(self):
        self.data_name = 'DSS'
        self.z = np.array([0.0])
        self.data = np.array([0.39])
        self.cov = np.array([[0.022**2]])
