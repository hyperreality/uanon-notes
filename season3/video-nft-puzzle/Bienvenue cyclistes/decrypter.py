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
decrypt_file(pad("réserve naturelle du boisé-roger-lemoine"), "06-dam.mp4.enc")
decrypt_file(pad("barrage du grand-moulin"), "07-park.mp4.enc")
decrypt_file(pad("parc national du mont-tremblant"), "08-municipality.mp4.enc")
decrypt_file(pad("la conception"), "09-bridge.mp4.enc")
decrypt_file(pad("pont de l'île perry"), "10-bridge.mp4.enc")
decrypt_file(pad("estacade du pont champlain"), "11-municipality.mp4.enc")
decrypt_file(pad("sainte-catherine"), "12-bridge.mp4.enc")
decrypt_file(pad("passerelle normandie"), "13-island.mp4.enc")
decrypt_file(pad("île grosbois"), "14-final-location.txt.enc")


# with open('municipalities.txt') as f:
#     munis = [a.strip().lower() for a in f.readlines()]

# for m in munis:
#     print(m)
#     decrypt_file(pad(m), "12-bridge.mp4.enc")
#     with open("12-bridge.mp4.dec", "rb") as f:
#         firstbytes = f.read(2)
#         if firstbytes == b"\x00\x00":
#             print("found")
#             break
