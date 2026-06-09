from abc import abstractmethod
from typing import TYPE_CHECKING
from sage.rings.integer import Integer
from sage.misc.prandom import randint, choice
from sage.arith.functions import lcm
from sage.arith.misc import inverse_mod

from sage.crypto.public_key.public_key_encryption.public_key_encryption_base import(
    PublicKeyEncryptionBase,
)

class RSA(PublicKeyEncryptionBase):

    def __init__(
            self,
        p: Integer | int,
        q: Integer | int
    ) -> None:

        self._p = Integer(p)
        self._q = Integer(q)

        self._n = self._p * self._q

        self._l = lcm(self._p - 1, self._q - 1)

    def generate_public_key(self) -> Integer:
        x = self._l.coprime_integers(self._l)
        x.remove(1)
        
        return choice(x)

    def generate_private_key(self, public_key) -> Integer:
        return inverse_mod(public_key, self._l)

    def encrypt_message(self, public_key, message) -> Integer:
        return message.powermod(public_key, self._n)

    def decrypt_message(self, private_key, cipher) -> Integer:
        return cipher.powermod(private_key, self._n)

    def parameters(self) -> tuple[Integer, Integer, Integer, Integer, Integer]:
        return (self._p, self._q, self._n, self._l)
