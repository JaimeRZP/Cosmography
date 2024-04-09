from .base import CosmographyBase
import numpy as np


class Sixdf(CosmographyBase):
    """
    6df data
    """
    def __init__(self):
        self.data_name = '6df'
        self.z = np.array([0.067])
        self.data = np.array([0.423])
        self.cov = np.array([[0.055**2]])
