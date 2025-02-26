import base64
import hashlib

import rsa
import yaml


class HotloadUtil(object):
    def read_yaml(self, key):
        with open(key, 'r') as f:
            value = yaml.safe_load(f)
            return value[key]

    def md5_encode(self, data):
        data = str(data).encode('utf-8')
        md5sum = hashlib.md5(data).hexdigest()
        return md5sum

    def base64_decode(self, data):
        data = str(data).encode('utf-8')
        return base64.b64decode(data)

    # def create_key(self):
    #     (public_key,secret_key) = rsa.newkeys(1024)
    #     with open("./public_key.pem",'w') as f:
    #         f.write(public_key.save_pkcs1().decode('utf-8'))
    #     with open("./secret_key.pem",'w') as f:
    #         f.write(secret_key.save_pkcs1().decode('utf-8'))


def rsa_encrypt(data, key):
    data = str(data).encode('utf-8')
    with open("../public.pem", 'r') as f:
        public_key = rsa.PublicKey.load_pkcs1_openssl_pem(f.read().encode('utf-8'))

    byte_value = rsa.encrypt(data, public_key)
    return base64.b64encode(byte_value).decode('utf-8')