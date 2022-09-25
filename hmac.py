import hmac
import hashlib 
import binascii
 
def hmacs(key, msg):
    key = binascii.unhexlify(key)
    msg = msg.encode()
    return hmac.new(key, msg, hashlib.sha256).hexdigest().upper()
 
 
print(hmacs("ABCDE", "hmac used for authentication and integerity"))
