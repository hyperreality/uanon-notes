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

word = "SHIFT$"
word = "FIRSTINCOMPLETENESSTHEOREM"
word = "INCOMPLETENESSTHEOREM"
word = "GÖDELSFIRSTINCOMPLETENESSTHEOREM"
word = "THEREISNOALGORITHMMWHOSEOUTPUTCONTAINSALLTRUESENTENCESOFARITHMETICANDNOFALSEONES"
word = "GÖDELSINCOMPLETENESSTHEOREM"
word = "For any consistent system F within which a certain amount of elementary arithmetic can be carried out, the consistency of F cannot be proved in F itself"
word = "There is no algorithm M whose output contains all true sentences of arithmetic and no false ones"
word = "GRIFT$"

out = decrypt_file(pad(word), "APRIL20.dat.enc")
print(out)
print(out[:16])
