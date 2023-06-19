from Crypto.Cipher import AES
import hashlib
import os

def decrypt_file(key, filename):
    output_filename = os.path.splitext(filename)[0] + '.dec'
    print(key)
    with open(filename, 'rb') as inputfile:
        enc_file = inputfile.read()
        enc_body = enc_file[16:]
        iv = enc_file[:16]
    print(iv)

    decryptor = AES.new(key, AES.MODE_CBC, IV=iv)
    dec_message = decryptor.decrypt(enc_body)

    with open(output_filename, 'wb') as outputfile:
        outputfile.write(dec_message)


def pad(key):
    return (key + (' ' * (32 - len(key.encode('utf8'))))).encode('utf8')[:32]

decrypt_file(pad("ANTFUGUE"), "trace1.txt.enc")

