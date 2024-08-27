from .base import CosmographyBase
import numpy as np


class PantheonDS17(CosmographyBase):
    """
        @ARTICLE{1710.00845,
        author = {{Scolnic}, D.~M. and {Jones}, D.~O. and {Rest}, A. and {Pan}, Y.~C. and {Chornock}, R. and {Foley}, R.~J. and {Huber}, M.~E. and {Kessler}, R. and {Narayan}, G. and {Riess}, A.~G. and {Rodney}, S. and {Berger}, E. and {Brout}, D.~J. and {Challis}, P.~J. and {Drout}, M. and {Finkbeiner}, D. and {Lunnan}, R. and {Kirshner}, R.~P. and {Sanders}, N.~E. and {Schlafly}, E. and {Smartt}, S. and {Stubbs}, C.~W. and {Tonry}, J. and {Wood-Vasey}, W.~M. and {Foley}, M. and {Hand}, J. and {Johnson}, E. and {Burgett}, W.~S. and {Chambers}, K.~C. and {Draper}, P.~W. and {Hodapp}, K.~W. and {Kaiser}, N. and {Kudritzki}, R.~P. and {Magnier}, E.~A. and {Metcalfe}, N. and {Bresolin}, F. and {Gall}, E. and {Kotak}, R. and {McCrum}, M. and {Smith}, K.~W.},
        title = "{The Complete Light-curve Sample of Spectroscopically Confirmed SNe Ia from Pan-STARRS1 and Cosmological Constraints from the Combined Pantheon Sample}",
        journal = {\apj},
        keywords = {cosmology: observations, dark energy, supernovae: general, Astrophysics - Cosmology and Nongalactic Astrophysics},
        year = 2018,
        month = jun,
        volume = {859},
        number = {2},
        eid = {101},
        pages = {101},
        doi = {10.3847/1538-4357/aab9bb},
        archivePrefix = {arXiv},
        eprint = {1710.00845},
        primaryClass = {astro-ph.CO},
        adsurl = {https://ui.adsabs.harvard.edu/abs/2018ApJ...859..101S},
        adsnote = {Provided by the SAO/NASA Astrophysics Data System}
        }
    """
    def __init__(self, path='../data/PantheonDS17/'):
        self.data_name = 'PantheonDS17'
        SN = np.transpose(np.loadtxt(path+'lcparam_DS17f.txt',
                                     usecols=(1, 4, 5)))
        self.z = np.array(SN[0])
        self.data = np.array(SN[1])
        base_cov = np.loadtxt(path+'syscov_panth.txt')
        self.cov = base_cov + np.diag(SN[2]**2)
        self.M_SH0ES = 19.2
        self.M_planck = 19.4
