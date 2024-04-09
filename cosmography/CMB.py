from .base import CosmographyBase
import numpy as np


class CMB(CosmographyBase):
    """
        @ARTICLE{2020A&A...641A...6P,
        author = {{Planck Collaboration} and {Aghanim}, N. and {Akrami}, Y. and {Ashdown}, M. and {Aumont}, J. and {Baccigalupi}, C. and {Ballardini}, M. and {Banday}, A.~J. and {Barreiro}, R.~B. and {Bartolo}, N. and {Basak}, S. and {Battye}, R. and {Benabed}, K. and {Bernard}, J. -P. and {Bersanelli}, M. and {Bielewicz}, P. and {Bock}, J.~J. and {Bond}, J.~R. and {Borrill}, J. and {Bouchet}, F.~R. and {Boulanger}, F. and {Bucher}, M. and {Burigana}, C. and {Butler}, R.~C. and {Calabrese}, E. and {Cardoso}, J. -F. and {Carron}, J. and {Challinor}, A. and {Chiang}, H.~C. and {Chluba}, J. and {Colombo}, L.~P.~L. and {Combet}, C. and {Contreras}, D. and {Crill}, B.~P. and {Cuttaia}, F. and {de Bernardis}, P. and {de Zotti}, G. and {Delabrouille}, J. and {Delouis}, J. -M. and {Di Valentino}, E. and {Diego}, J.~M. and {Dor{\'e}}, O. and {Douspis}, M. and {Ducout}, A. and {Dupac}, X. and {Dusini}, S. and {Efstathiou}, G. and {Elsner}, F. and {En{\ss}lin}, T.~A. and {Eriksen}, H.~K. and {Fantaye}, Y. and {Farhang}, M. and {Fergusson}, J. and {Fernandez-Cobos}, R. and {Finelli}, F. and {Forastieri}, F. and {Frailis}, M. and {Fraisse}, A.~A. and {Franceschi}, E. and {Frolov}, A. and {Galeotta}, S. and {Galli}, S. and {Ganga}, K. and {G{\'e}nova-Santos}, R.~T. and {Gerbino}, M. and {Ghosh}, T. and {Gonz{\'a}lez-Nuevo}, J. and {G{\'o}rski}, K.~M. and {Gratton}, S. and {Gruppuso}, A. and {Gudmundsson}, J.~E. and {Hamann}, J. and {Handley}, W. and {Hansen}, F.~K. and {Herranz}, D. and {Hildebrandt}, S.~R. and {Hivon}, E. and {Huang}, Z. and {Jaffe}, A.~H. and {Jones}, W.~C. and {Karakci}, A. and {Keih{\"a}nen}, E. and {Keskitalo}, R. and {Kiiveri}, K. and {Kim}, J. and {Kisner}, T.~S. and {Knox}, L. and {Krachmalnicoff}, N. and {Kunz}, M. and {Kurki-Suonio}, H. and {Lagache}, G. and {Lamarre}, J. -M. and {Lasenby}, A. and {Lattanzi}, M. and {Lawrence}, C.~R. and {Le Jeune}, M. and {Lemos}, P. and {Lesgourgues}, J. and {Levrier}, F. and {Lewis}, A. and {Liguori}, M. and {Lilje}, P.~B. and {Lilley}, M. and {Lindholm}, V. and {L{\'o}pez-Caniego}, M. and {Lubin}, P.~M. and {Ma}, Y. -Z. and {Mac{\'\i}as-P{\'e}rez}, J.~F. and {Maggio}, G. and {Maino}, D. and {Mandolesi}, N. and {Mangilli}, A. and {Marcos-Caballero}, A. and {Maris}, M. and {Martin}, P.~G. and {Martinelli}, M. and {Mart{\'\i}nez-Gonz{\'a}lez}, E. and {Matarrese}, S. and {Mauri}, N. and {McEwen}, J.~D. and {Meinhold}, P.~R. and {Melchiorri}, A. and {Mennella}, A. and {Migliaccio}, M. and {Millea}, M. and {Mitra}, S. and {Miville-Desch{\^e}nes}, M. -A. and {Molinari}, D. and {Montier}, L. and {Morgante}, G. and {Moss}, A. and {Natoli}, P. and {N{\o}rgaard-Nielsen}, H.~U. and {Pagano}, L. and {Paoletti}, D. and {Partridge}, B. and {Patanchon}, G. and {Peiris}, H.~V. and {Perrotta}, F. and {Pettorino}, V. and {Piacentini}, F. and {Polastri}, L. and {Polenta}, G. and {Puget}, J. -L. and {Rachen}, J.~P. and {Reinecke}, M. and {Remazeilles}, M. and {Renzi}, A. and {Rocha}, G. and {Rosset}, C. and {Roudier}, G. and {Rubi{\~n}o-Mart{\'\i}n}, J.~A. and {Ruiz-Granados}, B. and {Salvati}, L. and {Sandri}, M. and {Savelainen}, M. and {Scott}, D. and {Shellard}, E.~P.~S. and {Sirignano}, C. and {Sirri}, G. and {Spencer}, L.~D. and {Sunyaev}, R. and {Suur-Uski}, A. -S. and {Tauber}, J.~A. and {Tavagnacco}, D. and {Tenti}, M. and {Toffolatti}, L. and {Tomasi}, M. and {Trombetti}, T. and {Valenziano}, L. and {Valiviita}, J. and {Van Tent}, B. and {Vibert}, L. and {Vielva}, P. and {Villa}, F. and {Vittorio}, N. and {Wandelt}, B.~D. and {Wehus}, I.~K. and {White}, M. and {White}, S.~D.~M. and {Zacchei}, A. and {Zonca}, A.},
        title = "{Planck 2018 results. VI. Cosmological parameters}",
        journal = {\aap},
        keywords = {cosmic background radiation, cosmological parameters, Astrophysics - Cosmology and Nongalactic Astrophysics},
        year = 2020,
        month = sep,
        volume = {641},
        eid = {A6},
        pages = {A6},
        doi = {10.1051/0004-6361/201833910},
        archivePrefix = {arXiv},
        eprint = {1807.06209},
        primaryClass = {astro-ph.CO},
        adsurl = {https://ui.adsabs.harvard.edu/abs/2020A&A...641A...6P},
        adsnote = {Provided by the SAO/NASA Astrophysics Data System}
        }
    """
    def __init__(self):
        self.data_name = 'CMB'
        self.z = np.array([1089.95])
        self.data = np.array([1.04109])
        self.cov = np.array([[0.00030**2]])
