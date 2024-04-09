from .base import CosmographyBase
import numpy as np


class Sixdf(CosmographyBase):
    """
        @ARTICLE{2012MNRAS.423.3430B,
        author = {{Beutler}, Florian and {Blake}, Chris and {Colless}, Matthew and {Jones}, D. Heath and {Staveley-Smith}, Lister and {Poole}, Gregory B. and {Campbell}, Lachlan and {Parker}, Quentin and {Saunders}, Will and {Watson}, Fred},
        title = "{The 6dF Galaxy Survey: z{\ensuremath{\approx}} 0 measurements of the growth rate and {\ensuremath{\sigma}}$_{8}$}",
        journal = {\mnras},
        keywords = {surveys, galaxies: statistics, cosmological parameters, cosmology: observations, large-scale structure of Universe, Astrophysics - Cosmology and Nongalactic Astrophysics},
        year = 2012,
        month = jul,
        volume = {423},
        number = {4},
        pages = {3430-3444},
        doi = {10.1111/j.1365-2966.2012.21136.x},
        archivePrefix = {arXiv},
        eprint = {1204.4725},
        primaryClass = {astro-ph.CO},
        adsurl = {https://ui.adsabs.harvard.edu/abs/2012MNRAS.423.3430B},
        adsnote = {Provided by the SAO/NASA Astrophysics Data System}
        }
    """
    def __init__(self):
        self.data_name = '6df'
        self.z = np.array([0.067])
        self.data = np.array([0.423])
        self.cov = np.array([[0.055**2]])
