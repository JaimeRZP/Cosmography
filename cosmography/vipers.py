from .base import CosmographyBase
import numpy as np


class Vipers(CosmographyBase):
    """
        @ARTICLE{2017A&A...604A..33P,
        author = {{Pezzotta}, A. and {de la Torre}, S. and {Bel}, J. and {Granett}, B.~R. and {Guzzo}, L. and {Peacock}, J.~A. and {Garilli}, B. and {Scodeggio}, M. and {Bolzonella}, M. and {Abbas}, U. and {Adami}, C. and {Bottini}, D. and {Cappi}, A. and {Cucciati}, O. and {Davidzon}, I. and {Franzetti}, P. and {Fritz}, A. and {Iovino}, A. and {Krywult}, J. and {Le Brun}, V. and {Le F{\`e}vre}, O. and {Maccagni}, D. and {Ma{\l}ek}, K. and {Marulli}, F. and {Polletta}, M. and {Pollo}, A. and {Tasca}, L.~A.~M. and {Tojeiro}, R. and {Vergani}, D. and {Zanichelli}, A. and {Arnouts}, S. and {Branchini}, E. and {Coupon}, J. and {De Lucia}, G. and {Koda}, J. and {Ilbert}, O. and {Mohammad}, F. and {Moutard}, T. and {Moscardini}, L.},
        title = "{The VIMOS Public Extragalactic Redshift Survey (VIPERS). The growth of structure at 0.5 < z < 1.2 from redshift-space distortions in the clustering of the PDR-2 final sample}",
        journal = {\aap},
        keywords = {cosmology: observations, large-scale structure of Universe, galaxies: high-redshift, galaxies: statistics, Astrophysics - Cosmology and Nongalactic Astrophysics},
        year = 2017,
        month = jul,
        volume = {604},
        eid = {A33},
        pages = {A33},
        doi = {10.1051/0004-6361/201630295},
        archivePrefix = {arXiv},
        eprint = {1612.05645},
        primaryClass = {astro-ph.CO},
        adsurl = {https://ui.adsabs.harvard.edu/abs/2017A&A...604A..33P},
        adsnote = {Provided by the SAO/NASA Astrophysics Data System}
        }
    """
    def __init__(self):
        self.data_name = 'Vipers'
        self.z = np.array([0.60, 0.86])
        self.data = np.array([0.55, 0.40])
        self.cov = np.array([[0.12**2, 0],
                            [0, 0.11**2]])
