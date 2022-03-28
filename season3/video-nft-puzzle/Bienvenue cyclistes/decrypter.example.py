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

    with open(output_filename, 'wb') as outputfile:
        outputfile.write(dec_message)


def pad(key):
    return (key + (' ' * (32 - len(key.encode('utf8'))))).encode('utf8')[:32]

decrypt_file(pad("île monk"), "02-bridge.mp4.enc")
decrypt_file(pad("pont taschereau"), "03-street.mp4.enc")
decrypt_file(pad("avenue saint-charles"), "04-street.mp4.enc")
decrypt_file(pad("chemin de l'anse"), "05-nature_preserve.mp4.enc")
# decrypt_file(pad("parc-nature de l'anse-à-l'orme"), "06-dam.mp4.enc")
# decrypt_file(pad("morgan arboretum"), "06-dam.mp4.enc")
decrypt_file(pad("arboretum morgan"), "06-dam.mp4.enc")
decrypt_file(pad("forêt-de-senneville"), "06-dam.mp4.enc")

