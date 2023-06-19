from Crypto.Cipher import AES
import hashlib
import os

def decrypt_file(key, filename):
    output_filename = os.path.splitext(filename)[0] + '.dec'
    with open(filename, 'rb') as inputfile:
        enc_file = inputfile.read()
        enc_body = enc_file[16:]
        iv = enc_file[:16]

    decryptor = AES.new(key, AES.MODE_CBC, IV=iv)
    dec_message = decryptor.decrypt(enc_body)

    with open(output_filename, "wb") as f:
        f.write(dec_message)

    return dec_message

def pad(key):
    return (key + (' ' * (32 - len(key.encode('utf8'))))).encode('utf8')[:32]

# password = "GEB"

# out = b""

# out +=
words = [
    "MI",
    # "MU",
    # "MIU",
    # "MII",
    # "MI→MIU",
    # "MIU→MIUIU",
    # "MUU→MU",
]
decrypt_file(pad("MI"), "image1.enc")
out = decrypt_file(pad("MI→MIU"), "image2.enc")
out = decrypt_file(pad("MI→MII"), "image3.enc")
out = decrypt_file(pad("MI→MII→MIIII→MUI"), "image4.enc")
out = decrypt_file(pad("MI→MII→MIIII→MUI"), "image5.enc")
out = decrypt_file(pad("FALSE"), "image6.enc")
# out = decrypt_file(pad("MI→MII→MIIII→MUI→MU"), "image5.enc")
print(out)
print(out[:16])
    # # print(out[:16])
# out += decrypt_file(pad("strange loops"), "chunk2.enc")
# out += decrypt_file(pad("isomorphism"), "chunk3.enc")
# bla = decrypt_file(pad("semantic magic"), "chunk4.enc")
# out += bla
# print(bla)
# out += decrypt_file(pad("Dostoevsky"), "chunk5.enc")
# out += decrypt_file(pad("level-crossing feedback loop"), "chunk6.enc")

# output_filename = "out.pdf"
# with open(output_filename, 'wb') as outputfile:
#     outputfile.write(out)
