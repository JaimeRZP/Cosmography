from .base import CosmographyBase
import numpy as np


class BOSSDR12(CosmographyBase):
    """
        @ARTICLE{1607.03155,
        author = {{Alam}, Shadab and {Ata}, Metin and {Bailey}, Stephen and {Beutler}, Florian and {Bizyaev}, Dmitry and {Blazek}, Jonathan A. and {Bolton}, Adam S. and {Brownstein}, Joel R. and {Burden}, Angela and {Chuang}, Chia-Hsun and {Comparat}, Johan and {Cuesta}, Antonio J. and {Dawson}, Kyle S. and {Eisenstein}, Daniel J. and {Escoffier}, Stephanie and {Gil-Mar{\'\i}n}, H{\'e}ctor and {Grieb}, Jan Niklas and {Hand}, Nick and {Ho}, Shirley and {Kinemuchi}, Karen and {Kirkby}, David and {Kitaura}, Francisco and {Malanushenko}, Elena and {Malanushenko}, Viktor and {Maraston}, Claudia and {McBride}, Cameron K. and {Nichol}, Robert C. and {Olmstead}, Matthew D. and {Oravetz}, Daniel and {Padmanabhan}, Nikhil and {Palanque-Delabrouille}, Nathalie and {Pan}, Kaike and {Pellejero-Ibanez}, Marcos and {Percival}, Will J. and {Petitjean}, Patrick and {Prada}, Francisco and {Price-Whelan}, Adrian M. and {Reid}, Beth A. and {Rodr{\'\i}guez-Torres}, Sergio A. and {Roe}, Natalie A. and {Ross}, Ashley J. and {Ross}, Nicholas P. and {Rossi}, Graziano and {Rubi{\~n}o-Mart{\'\i}n}, Jose Alberto and {Saito}, Shun and {Salazar-Albornoz}, Salvador and {Samushia}, Lado and {S{\'a}nchez}, Ariel G. and {Satpathy}, Siddharth and {Schlegel}, David J. and {Schneider}, Donald P. and {Sc{\'o}ccola}, Claudia G. and {Seo}, Hee-Jong and {Sheldon}, Erin S. and {Simmons}, Audrey and {Slosar}, Anze and {Strauss}, Michael A. and {Swanson}, Molly E.~C. and {Thomas}, Daniel and {Tinker}, Jeremy L. and {Tojeiro}, Rita and {Maga{\~n}a}, Mariana Vargas and {Vazquez}, Jose Alberto and {Verde}, Licia and {Wake}, David A. and {Wang}, Yuting and {Weinberg}, David H. and {White}, Martin and {Wood-Vasey}, W. Michael and {Y{\`e}che}, Christophe and {Zehavi}, Idit and {Zhai}, Zhongxu and {Zhao}, Gong-Bo}},
        title = "{The clustering of galaxies in the completed SDSS-III Baryon Oscillation Spectroscopic Survey: cosmological analysis of the DR12 galaxy sample}",
        journal = {\mnras},
        keywords = {distance scale, large-scale structure of Universe, cosmology: observations, Astrophysics - Cosmology and Nongalactic Astrophysics},
        year = 2017,
        month = sep,
        volume = {470},
        number = {3},
        pages = {2617-2652},
        doi = {10.1093/mnras/stx721},
        archivePrefix = {arXiv},
        eprint = {1607.03155},
        primaryClass = {astro-ph.CO},
        adsurl = {https://ui.adsabs.harvard.edu/abs/2017MNRAS.470.2617A},
        adsnote = {Provided by the SAO/NASA Astrophysics Data System}
        }
    """
    def __init__(self):
        self.data_name = 'BOSS'
        self.rd = 147.78
        self.z = np.array([0.38, 0.51, 0.61])
        perp = np.array([1512.39, 1975.22, 2306.68])
        para = np.array([81.2087, 90.9029, 98.9647])
        fs8 = np.array([0.49749, 0.457523, 0.436148])
        self.data = np.concatenate([para, perp, fs8])
        self.cov = np.array([
                   [3.63049e+00, 1.80306e+00, 9.19842e-01,
                    9.71342e+00, 7.75546e+00, 5.97897e+00,
                    2.79185e-02, 1.24050e-02, 4.75548e-03],
                   [1.80306e+00, 3.77146e+00, 2.21471e+00,
                    4.85105e+00, 1.19729e+01, 9.73184e+00,
                    9.28354e-03, 2.22588e-02, 1.05956e-02],
                   [9.19842e-01, 2.21471e+00, 4.37982e+00,
                    2.43394e+00, 6.71715e+00, 1.60709e+01,
                    1.01870e-03, 9.71991e-03, 2.14133e-02],
                   [9.71342e+00, 4.85105e+00, 2.43394e+00,
                    5.00049e+02, 2.94536e+02, 1.42011e+02,
                    3.91498e-01, 1.51597e-01, 4.36366e-02],
                   [7.75546e+00, 1.19729e+01, 6.71715e+00,
                    2.94536e+02, 7.02299e+02, 4.32750e+02,
                    1.95890e-01, 3.88996e-01, 1.81786e-01],
                   [5.97897e+00, 9.73184e+00, 1.60709e+01,
                    1.42011e+02, 4.32750e+02, 1.01718e+03,
                    3.40803e-02, 2.46111e-01, 4.78570e-01],
                   [2.79185e-02, 9.28354e-03, 1.01870e-03,
                    3.91498e-01, 1.95890e-01, 3.40803e-02,
                    2.03355e-03, 8.11829e-04, 2.64615e-04],
                   [1.24050e-02, 2.22588e-02, 9.71991e-03,
                    1.51597e-01, 3.88996e-01, 2.46111e-01,
                    8.11829e-04, 1.42289e-03, 6.62824e-04],
                   [4.75548e-03, 1.05956e-02, 2.14133e-02,
                    4.36366e-02, 1.81786e-01, 4.78570e-01,
                    2.64615e-04, 6.62824e-04, 1.18576e-03]])

    def get_rd(self):
        """
        Returns the sound horizon at the drag epoch

        Returns:
            rd (float): sound horizon at the drag epoch
        """
        return self.rd
