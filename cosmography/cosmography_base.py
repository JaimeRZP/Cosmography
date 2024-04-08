import numpy  as np

class CosmographyBase(object):
    """
    Base class for cosmography data.
    """
    data_name = None

    def __init__(self):
        self._get_defaults()

    def _get_defaults(self):
        self.z = None
        self.data = None
        self.cov = None

    def get_redshift(self):
        """
        Returns the effective redshift of the data

        Returns:
            z (Array): redshift array
        """
        if self.z == None:
            raise NotImplementedError("This data set doesn't define this field")
        else:
            return self.z

    def get_data(self):
        """
        Returns the data array

        Returns:
            data (Array): data array
        """
        if self.data == None:
            raise NotImplementedError("This data set doesn't define this field")
        else:
            return self.data

    def get_cov(self):
        """
        Returns the data covariance

        Returns:
            cov (Array): covariance
        """
        if self.cov == None:
            raise NotImplementedError("This data set doesn't define this field")
        else:
            return self.cov

