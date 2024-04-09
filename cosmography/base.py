

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
        if self.z is None:
            raise NotImplementedError("Not found")
        else:
            return self.z

    def get_data(self):
        """
        Returns the data array

        Returns:
            data (Array): data array
        """
        if self.data is None:
            raise NotImplementedError("Not found")
        else:
            return self.data

    def get_cov(self):
        """
        Returns the data covariance

        Returns:
            cov (Array): covariance
        """
        if self.cov is None:
            raise NotImplementedError("Not found")
        else:
            return self.cov
