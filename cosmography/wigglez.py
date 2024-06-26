from .base import CosmographyBase
import numpy as np


class Wigglez(CosmographyBase):
    """
        @ARTICLE{2012MNRAS.425..405B,
        author = {{Blake}, Chris and {Brough}, Sarah and {Colless}, Matthew and {Contreras}, Carlos and {Couch}, Warrick and {Croom}, Scott and {Croton}, Darren and {Davis}, Tamara M. and {Drinkwater}, Michael J. and {Forster}, Karl and {Gilbank}, David and {Gladders}, Mike and {Glazebrook}, Karl and {Jelliffe}, Ben and {Jurek}, Russell J. and {Li}, I. -hui and {Madore}, Barry and {Martin}, D. Christopher and {Pimbblet}, Kevin and {Poole}, Gregory B. and {Pracy}, Michael and {Sharp}, Rob and {Wisnioski}, Emily and {Woods}, David and {Wyder}, Ted K. and {Yee}, H.~K.~C.},
        title = "{The WiggleZ Dark Energy Survey: joint measurements of the expansion and growth history at z < 1}",
        journal = {\mnras},
        keywords = {surveys, distance scale, large-scale structure of Universe, Astrophysics - Cosmology and Nongalactic Astrophysics},
        year = 2012,
        month = sep,
        volume = {425},
        number = {1},
        pages = {405-414},
        doi = {10.1111/j.1365-2966.2012.21473.x},
        archivePrefix = {arXiv},
        eprint = {1204.3674},
        primaryClass = {astro-ph.CO},
        adsurl = {https://ui.adsabs.harvard.edu/abs/2012MNRAS.425..405B},
        adsnote = {Provided by the SAO/NASA Astrophysics Data System}
        }
    """
    def __init__(self):
        self.data_name = 'Wigglez'
        self.z = np.array([0.44, 0.60, 0.73])
        self.data = np.array([0.413, 0.390, 0.437])
        cov_no_jitter = np.array([[6.4, 2.57, 0],
                                  [2.57, 3.969, 2.54],
                                  [0, 2.54, 5.184]])
        self.cov = 10**(-3)*cov_no_jitter
