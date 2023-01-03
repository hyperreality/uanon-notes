from Crypto.Cipher import AES
import hashlib
import os
from tqdm import tqdm

def decrypt_file(key, filename, size):
    output_filename = "decoded_" + os.path.splitext(filename)[0] + '.png'
    with open(filename, 'rb') as inputfile:
        enc_file = inputfile.read()
        enc_body = enc_file[16:]
        iv = enc_file[:16]

    decryptor = AES.new(key, AES.MODE_CBC, IV=iv)
    dec_message = decryptor.decrypt(enc_body[:len(enc_body)-1])

        # print(dec_message[:48])
        # print("Hit")
        # print(filename)
        # print(key)

    with open(output_filename, 'wb') as outputfile:
        outputfile.write(dec_message)


def decrypt_file2(key, filename, size):
    output_filename = "decoded_" + os.path.splitext(filename)[0] + '.png'
    with open(filename, 'rb') as inputfile:
        enc_file = inputfile.read()
        enc_body = enc_file[16:]
        iv = enc_file[:16]

    decryptor = AES.new(key, AES.MODE_CBC, IV=iv)
    dec_message = decryptor.decrypt(enc_body)

        # print(dec_message[:48])
        # print("Hit")
        # print(filename)
        # print(key)

    with open(output_filename, 'wb') as outputfile:
        outputfile.write(dec_message)


def pad(key):
    return (key + (' ' * (32 - len(key.encode('utf8'))))).encode('utf8')[:32]


decrypt_file(pad("GRIFT$"), "i1.txt", 9999999999)
decrypt_file(pad("GRIFT$"), "i2.txt", 9999999999)
decrypt_file(pad("GRIFT$"), "i3.txt", 9999999999)
decrypt_file(pad("GRIFT$"), "i4.txt", 9999999999)
decrypt_file(pad("GRIFT$"), "i5.txt", 9999999999)
decrypt_file(pad("GRIFT$"), "i6.txt", 9999999999)


decrypt_file2(pad("GRIFT$"), "d_i1.txt", 9999999999)

# with open('i1.txt', 'rb') as f:
#     i1 = f.read()
# with open('i2.txt', 'rb') as f:
#     i2 = f.read()
# with open('i3.txt', 'rb') as f:
#     i3 = f.read()
# with open('i4.txt', 'rb') as f:
#     i4 = f.read()
# with open('i5.txt', 'rb') as f:
#     i5 = f.read()
# with open('i6.txt', 'rb') as f:
#     i6 = f.read()

