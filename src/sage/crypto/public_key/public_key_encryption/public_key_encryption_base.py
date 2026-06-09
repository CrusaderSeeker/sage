from abc import abstractmethod
from typing import Any, Self

from sage.misc.superseded import experimental_warning
from sage.structure.sage_object import SageObject

experimental_warning(
    41218,
    "SageMath's key exchange functionality is experimental and might change in the future.",
)

class PublicKeyEncryptionBase(SageObject):

    @abstractmethod
    def generate_secret_key(self):

        raise NotImplementedError

    @abstractmethod
    def generate_public_key(self):

        raise NotImplementedError

    @abstractmethod
    def encrypt_message(self, public_key, message):

        raise NotImplementedError

    @abstractmethod
    def decrypt_message(self, private_key, cipher):

        raise NotImplementedError

