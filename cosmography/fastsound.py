from .base import CosmographyBase
import numpy as np


class FastSound(CosmographyBase):
    """
        @ARTICLE{2016PASJ...68...38O,
        author = {{Okumura}, Teppei and {Hikage}, Chiaki and {Totani}, Tomonori and {Tonegawa}, Motonari and {Okada}, Hiroyuki and {Glazebrook}, Karl and {Blake}, Chris and {Ferreira}, Pedro G. and {More}, Surhud and {Taruya}, Atsushi and {Tsujikawa}, Shinji and {Akiyama}, Masayuki and {Dalton}, Gavin and {Goto}, Tomotsugu and {Ishikawa}, Takashi and {Iwamuro}, Fumihide and {Matsubara}, Takahiko and {Nishimichi}, Takahiro and {Ohta}, Kouji and {Shimizu}, Ikkoh and {Takahashi}, Ryuichi and {Takato}, Naruhisa and {Tamura}, Naoyuki and {Yabe}, Kiyoto and {Yoshida}, Naoki},
        title = "{The Subaru FMOS galaxy redshift survey (FastSound). IV. New constraint on gravity theory from redshift space distortions at z {\ensuremath{\sim}} 1.4}",
        journal = {\pasj},
        keywords = {cosmological parameters, cosmology: large-scale structure of universe, cosmology: observations, galaxies: distances and redshifts, methods: data analysis, Astrophysics - Cosmology and Nongalactic Astrophysics},
        year = 2016,
        month = jun,
        volume = {68},
        number = {3},
        eid = {38},
        pages = {38},
        doi = {10.1093/pasj/psw029},
        archivePrefix = {arXiv},
        eprint = {1511.08083},
        primaryClass = {astro-ph.CO},
        adsurl = {https://ui.adsabs.harvard.edu/abs/2016PASJ...68...38O},
        adsnote = {Provided by the SAO/NASA Astrophysics Data System}
        }
    """
    def __init__(self):
        self.data_name = 'FastSound'
        self.z = np.array([1.4])
        self.data = np.array([0.482])
        self.cov = np.array([[0.116**2]])
