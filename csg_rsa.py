import rsa
import unittest

def rsa_sign(message, privkey_file):
    """
    Sign a string message using the key contained in the privkey_file.

    message - string
    privkey_file - file object (as returned by Python's `open` bif)
    """
    privkey = rsa.PrivateKey.load_pkcs1(privkeyfile)
    signature = rsa.sign(message, privkey, "SHA-512")

    return signature.encode("base64")

class FunctionsTest(unittest.TestCase):
    
    def test_rsa_sign(self):
        # TODO
        pass

if __name__ == "__main__":
    unittest.main()
