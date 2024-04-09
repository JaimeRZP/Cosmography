from .base import CosmographyBase
import numpy as np


class eBOSS(CosmographyBase):
    """
        @ARTICLE{2021PhRvD.103h3533A,
        author = {{Alam}, Shadab and {Aubert}, Marie and {Avila}, Santiago and {Balland}, Christophe and {Bautista}, Julian E. and {Bershady}, Matthew A. and {Bizyaev}, Dmitry and {Blanton}, Michael R. and {Bolton}, Adam S. and {Bovy}, Jo and {Brinkmann}, Jonathan and {Brownstein}, Joel R. and {Burtin}, Etienne and {Chabanier}, Sol{\`e}ne and {Chapman}, Michael J. and {Choi}, Peter Doohyun and {Chuang}, Chia-Hsun and {Comparat}, Johan and {Cousinou}, Marie-Claude and {Cuceu}, Andrei and {Dawson}, Kyle S. and {de la Torre}, Sylvain and {de Mattia}, Arnaud and {Agathe}, Victoria de Sainte and {des Bourboux}, H{\'e}lion du Mas and {Escoffier}, Stephanie and {Etourneau}, Thomas and {Farr}, James and {Font-Ribera}, Andreu and {Frinchaboy}, Peter M. and {Fromenteau}, Sebastien and {Gil-Mar{\'\i}n}, H{\'e}ctor and {Le Goff}, Jean-Marc and {Gonzalez-Morales}, Alma X. and {Gonzalez-Perez}, Violeta and {Grabowski}, Kathleen and {Guy}, Julien and {Hawken}, Adam J. and {Hou}, Jiamin and {Kong}, Hui and {Parker}, James and {Klaene}, Mark and {Kneib}, Jean-Paul and {Lin}, Sicheng and {Long}, Daniel and {Lyke}, Brad W. and {de la Macorra}, Axel and {Martini}, Paul and {Masters}, Karen and {Mohammad}, Faizan G. and {Moon}, Jeongin and {Mueller}, Eva-Maria and {Mu{\~n}oz-Guti{\'e}rrez}, Andrea and {Myers}, Adam D. and {Nadathur}, Seshadri and {Neveux}, Richard and {Newman}, Jeffrey A. and {Noterdaeme}, Pasquier and {Oravetz}, Audrey and {Oravetz}, Daniel and {Palanque-Delabrouille}, Nathalie and {Pan}, Kaike and {Paviot}, Romain and {Percival}, Will J. and {P{\'e}rez-R{\`a}fols}, Ignasi and {Petitjean}, Patrick and {Pieri}, Matthew M. and {Prakash}, Abhishek and {Raichoor}, Anand and {Ravoux}, Corentin and {Rezaie}, Mehdi and {Rich}, James and {Ross}, Ashley J. and {Rossi}, Graziano and {Ruggeri}, Rossana and {Ruhlmann-Kleider}, Vanina and {S{\'a}nchez}, Ariel G. and {S{\'a}nchez}, F. Javier and {S{\'a}nchez-Gallego}, Jos{\'e} R. and {Sayres}, Conor and {Schneider}, Donald P. and {Seo}, Hee-Jong and {Shafieloo}, Arman and {Slosar}, An{\v{z}}e and {Smith}, Alex and {Stermer}, Julianna and {Tamone}, Amelie and {Tinker}, Jeremy L. and {Tojeiro}, Rita and {Vargas-Maga{\~n}a}, Mariana and {Variu}, Andrei and {Wang}, Yuting and {Weaver}, Benjamin A. and {Weijmans}, Anne-Marie and {Y{\`e}che}, Christophe and {Zarrouk}, Pauline and {Zhao}, Cheng and {Zhao}, Gong-Bo and {Zheng}, Zheng},
        title = "{Completed SDSS-IV extended Baryon Oscillation Spectroscopic Survey: Cosmological implications from two decades of spectroscopic surveys at the Apache Point Observatory}",
        journal = {\prd},
        keywords = {Astrophysics - Cosmology and Nongalactic Astrophysics},
        year = 2021,
        month = apr,
        volume = {103},
        number = {8},
        eid = {083533},
        pages = {083533},
        doi = {10.1103/PhysRevD.103.083533},
        archivePrefix = {arXiv},
        eprint = {2007.08991},
        primaryClass = {astro-ph.CO},
        adsurl = {https://ui.adsabs.harvard.edu/abs/2021PhRvD.103h3533A},
        adsnote = {Provided by the SAO/NASA Astrophysics Data System}
        }
    """
    def __init__(self):
        self.data_name = 'eBOSS'
        self.rd = 147.3
        self.z = np.array([1.48])
        para = 13.23
        perp = 30.21
        fs8 = 0.462
        self.data = np.array([para, perp, fs8])
        self.cov = np.array([[0.7709, -0.05656, 0.01750],
                             [-0.05656, 0.2640, -0.006204],
                             [0.01750, -0.006204, 0.002308]])

    def get_rd(self):
        """
        Returns the sound horizon at the drag epoch
        Returns:
            rd (float): sound horizon at the drag epoch
        """
        return self.rd
