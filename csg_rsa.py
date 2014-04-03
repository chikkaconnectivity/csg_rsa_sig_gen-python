import rsa
import unittest

VERSION = (0, 1, 0)

def rsa_sign(message, privkey_file):
    """
    Sign a string message using the key contained in the privkey_file.

    message - string
    privkey_file - file object (as returned by Python's `open` bif)
    """
    privkey = rsa.PrivateKey.load_pkcs1("".join(privkey_file))
    signature = rsa.sign(message, privkey, "SHA-512")

    return signature.encode("base64")

class FunctionsTest(unittest.TestCase):
    
    def test_rsa_sign(self):
        message = "that then i'd scorn to change my state with kings"
        expected_signed = ""

        with open("signed.b64") as es:
            expected_signed = "".join(es)

        with open("private_key.pem1") as privkey_file:
            function_signed = rsa_sign(message, privkey_file)

            self.assertEquals(expected_signed, function_signed)

if __name__ == "__main__":
    unittest.main()
