"""
This class is a Singleton that stores the general information of the organization.

Author: Jonathan
"""


class GeneralInfo:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(GeneralInfo, cls).__new__(cls)
        return cls._instance

    def __init__(self, name_organization: str, address: str, nit: str):
        if not hasattr(self, 'initialized'):
            self.name_organization = name_organization
            self.address = address
            self.nit = nit
            self.initialized = True
