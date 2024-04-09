from .base import CosmographyBase
import numpy as np


class FastSound(CosmographyBase):
    def __init__(self):
        self.data_name = 'FastSound'
        self.z = np.array([1.4])
        self.data = np.array([0.482])
        self.cov = np.array([[0.116**2]])
