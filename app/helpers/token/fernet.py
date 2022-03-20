"""Fernet encryption/decryption utility class"""

from cryptography.fernet import Fernet, InvalidToken

from settings import AUTH_SECRET


class FernetHelper:
    """Fernet encode decode helper. Every parameter must be encoded"""

    def __init__(self):
        # key = Fernet.generate_key() --> generates key/ for prod use your own key
        key = AUTH_SECRET
        self.fernet = Fernet(key=key.encode("utf-8"))

    def encrypt(self, plain_text):
        """Encrypts the plain text"""
        encrypted = self.fernet.encrypt(plain_text.encode("utf-8"))
        return encrypted.decode("utf-8")

    def decrypt(self, cipher_text):
        decrypted = None
        try:
            decrypted = self.fernet.decrypt(cipher_text.encode("utf-8"))
        except InvalidToken:
            return None
        return decrypted.decode("utf-8")
