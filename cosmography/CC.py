from .base import CosmographyBase
import numpy as np


class CC(CosmographyBase):
    """
        @article{2011.11645,
        title        = {{Eppur {\`e} piatto? The Cosmic Chronometers Take on Spatial Curvature and Cosmic Concordance}},
        author       = {{Vagnozzi}, Sunny and {Loeb}, Abraham and {Moresco}, Michele},
        year         = 2021,
        month        = feb,
        journal      = {\apj},
        volume       = 908,
        number       = 1,
        pages        = 84,
        doi          = {10.3847/1538-4357/abd4df},
        keywords     = {Observational cosmology, Cosmic background radiation, Galaxy ages, Cosmological parameters, Galaxies, 1146, 317, 576, 339, 573, Astrophysics - Cosmology and Nongalactic Astrophysics, General Relativity and Quantum Cosmology},
        eid          = 84,
        archiveprefix = {arXiv},
        eprint       = {2011.11645},
        primaryclass = {astro-ph.CO},
        adsurl       = {https://ui.adsabs.harvard.edu/abs/2021ApJ...908...84V},
        adsnote      = {Provided by the SAO/NASA Astrophysics Data System}
        }
    """
    def __init__(self):
        self.data_name = 'CC'
        self.z = np.array([
            0.07, 0.09, 0.12, 0.17,
            0.179, 0.199, 0.2,
            0.27, 0.28, 0.352,
            0.38, 0.3802, 0.4,
            0.4004, 0.4247, 0.44,
            0.4497, 0.47, 0.4783,
            0.48, 0.51, 0.593, 0.6,
            0.61, 0.68, 0.73, 0.781,
            0.875, 0.88, 0.9, 1.037,
            1.3, 1.363, 1.43,
            1.53, 1.75, 1.965])
        self.data = np.array([
            69.0, 69.0, 68.6,
            83.0, 75.0, 75.0, 72.9,
            77.0, 88.8, 83.0, 81.5,
            83.0,  95.0, 77.0, 87.1,
            82.6, 92.8,  89.0, 80.9,
            97.0,  90.4, 104.0, 87.9,
            97.3, 92.0, 97.3,  105.0,
            125.0, 90.0, 117.0, 154.0,
            168.0, 160.0, 177.0, 140.0,
            202.0, 186.5])
        err = np.array([
            19.6, 12.0, 26.2, 8.0,
            4.0, 5.0, 29.6, 14.0,
            36.6, 14.0, 1.9, 13.5,
            17.0, 10.2,  11.2, 7.8,
            12.9, 23.0, 9.0, 62.0,
            1.9, 13.0, 6.1, 2.1,
            8.0, 7.0, 12.0, 17.0,
            40.0, 23.0, 20.0, 17.0,
            33.6, 18.0,  14.0, 40.0,  50.4])
        cov = np.zeros([len(self.z), len(self.z)])
        for i in np.arange(len(self.z)):
            cov[i, i] = err[i]**2
        self.cov = cov
