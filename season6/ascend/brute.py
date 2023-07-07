from hashlib import blake2b
import bisect
import json
import itertools
from struct import pack
from binascii import hexlify, unhexlify
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from tqdm import tqdm

def hash(message, rounds=1):
    h = message
    for i in range(rounds):
        if i + 1 == rounds:
            h = blake2b(h, digest_size=32).hexdigest()
        else:
            h = blake2b(h, digest_size=32).digest()
    return h

def stringify(message):
    if isinstance(message, str):
        message = [message]
    return json.dumps(message, separators=(',', ':'), ensure_ascii=False)

def generate_proof(message, depth=1):
    magic_bytes = b'\x05\x01'
    # print(message)
    passphrase = stringify(message)
    # print(passphrase)
    length = pack('>l', len(passphrase))
    concatenated = magic_bytes + length + passphrase.encode()
    return hash(concatenated, rounds=depth)

def verify_proof(proof, secret, depth=2, start_depth=1):
    rounds = depth - start_depth
    proof_bytes = unhexlify(proof.encode('utf8'))
    return hash(proof_bytes, rounds=rounds) == secret

def submit_answer(message, depth=1):
    proof = generate_proof(message, depth=depth)
    return proof

def print_proof(*message):
    magic_bytes = b'\x05\x01'
    passphrase = stringify(message)
    length = pack('>l', len(passphrase))
    print(magic_bytes + length + passphrase)



def decrypt(enc, password):
    unhexed = bytes.fromhex(enc)
    # unhexed_pass = bytes.fromhex(password)
    # print("IV")
    # print(unhexed[:16])
    # print("Encrypted")
    # print(unhexed[16:])
    cipher = AES.new(password[:32].encode(), AES.MODE_CBC, unhexed[:16])
    dec = cipher.decrypt(unhexed[16:])
    out = dec.decode('latin-1')

    # print(out)
    length = 0
    asci = 0
    for a in out:
        length += 1
        if ord(a) < 128:
            asci += 1
    if asci / length > 0.9:
    # if "bit.ly" in out:
        print(out)
        return out

# enc = "4e41f390c0ace978d22f12afee1a1eae21193b17a87e0a2b759a2577920639446ef3ce0e152f847842c22ad7be763d7433e604cea9102a9c2c15c8c88310c4e0"
# words = [a.upper() for a in [
#     "Communication",
#     "Language",
#     "Finance",
#     "Culture",
#     "Ascension",
#     "Class"
# ]]

# for perm in itertools.permutations(words, r=6):
#     # print(i)
#     # i = "".join(i)
#     perm = list(perm)
#     perm[0] = f"SPRING{perm[0]}"
#     perm[1] = f"SUMMER{perm[1]}"
#     perm[2] = f"AUTUMN{perm[2]}"
#     perm[3] = f"WINTER{perm[3]}"
#     perm[4] = f"CRYPTOWINTER{perm[4]}"
#     perm[5] = f"DAWN{perm[5]}"
#     proof = submit_answer(perm)
#     if decrypt(enc, proof):
#         print(perm)
#         break


# enc = "4396d9be46de84c22ab14e7bde4617d2157db553145eac1dc0c0638782c0ac358271f8f71d5a5312fd9c12dc2732e1ddc5e53b33e962214cdd38b64f031b2cf9affad32a16ad70edafef85068a5063d377fd6f81acebbe9e33cf1f977aeb33ce"

# pluscodes = ["48V2+QH","7MV8XWQF+6X","GC38+X3","86MC+2X","9CP5C6C2+XP","577H7FH7+P9","399C+X2","PXXV+M","7MWG2FX3+C2"]

# for perm in itertools.permutations(pluscodes):
#     proof = submit_answer(perm)
#     if decrypt(enc, proof):
#         print(perm)
#         break

# chosen = ["GÖDEL,ESCHER,BACH:ANETERNALGOLDENBRAID", "INORDERTOLIVE:ANORTHKOREANGIRL'SJOURNEYTOFREEDOM", "THELIVINGMOUNTAIN"]
# print(len(chosen))
# proof = submit_answer(chosen)
# print(proof)

# enc = "523e5c3e7fd0812da729f081a81faccf3b1d354287f08a9568c96c0253de6b1e3dc12951b9e7993648b4b9bf331609300b439fe89815c5ae2871753c38af1de152b3a4819dd3ab2e748a090815ae25a4"

books = [
    "1984",
    "APORTRAITOFTHEARTISTASAYOUNGMAN",
    "BEINGINTIME",
    "BEYONDGOODANDEVIL",
    "CANDIDE",
    "CRITIQUEOFPUREREASON",
    "CRYPTONOMICON",
    "DR.HEIDEGGER'SEXPERIMENT",
    "EITHER/OR",
    "EPISTLETODR.ARBUTHNOT",
    "ETIDORHPA",
    "FEARANDTREMBLING",
    "GÖDEL,ESCHER,BACH:ANETERNALGOLDENBRAID",
    "HACKTHISZINEV.11",
    "INORDERTOLIVE:ANORTHKOREANGIRL'SJOURNEYTOFREEDOM",
    "INDUSTRIALSOCIETYANDITSFUTURE",
    "M.BUTTERFLY",
    "MIDDLEMARCH",
    "MONADOLOGY",
    "NOTESFROMTHEUNDERGROUND",
    "NOVUMORGANUM",
    "RABBIT,RUN",
    "SELF-RELIANCE",
    "THECITYOFGOD",
    "THEDEMON-HAUNTEDWORLD",
    "THEDIVINECOMEDY",
    "THEFALL",
    "THEGAYSCIENCE",
    "THELIVINGMOUNTAIN",
    "THEMANINTHEWELL",
    "THEMONTAUKPROJECT:EXPERIMENTSINTIME",
    "THEPEARL",
    "THEPICTUREOFDORIANGRAY",
    "THEPRESENTCRISIS",
    "THEREPUBLICANNOISEMACHINE",
    "THESOCIALCONTRACT",
    "THETURNOFTHESCREW",
    "THEWINTEROFOURDISCONTENT",
    "TRACTATUSLOGICO-PHILOSOPHICUS",
    "TWODOGMASOFEMPIRICISM",
    "VALLEYOFTHEDOLLS",
    "WALDENTWO"
]
# print(len(books))

chosen = sorted(['CANDIDE', 'CRYPTONOMICON', "DR.HEIDEGGER'SEXPERIMENT", 'EITHER/OR', 'ETIDORHPA', 'FEARANDTREMBLING', 'GÖDEL,ESCHER,BACH:ANETERNALGOLDENBRAID', 'HACKTHISZINEV.11', 'INDUSTRIALSOCIETYANDITSFUTURE', "INORDERTOLIVE:ANORTHKOREANGIRL'SJOURNEYTOFREEDOM", 'M.BUTTERFLY', 'NOVUMORGANUM', 'SELF-RELIANCE', 'THEDEMON-HAUNTEDWORLD', 'THEDIVINECOMEDY', 'THEGAYSCIENCE', 'THEMANINTHEWELL', 'THEPICTUREOFDORIANGRAY', 'THEPRESENTCRISIS', 'THESOCIALCONTRACT', 'THEWINTEROFOURDISCONTENT', 'TRACTATUSLOGICO-PHILOSOPHICUS', 'VALLEYOFTHEDOLLS'])
books_notchosen = [b for b in books if b not in chosen]

assert(all(c in books for c in chosen))
print(len(chosen))

# for x in range(len(chosen)):
#     topop = chosen[x]
#     for comb in itertools.combinations(books_notchosen, r=9):
#         # print(comb)
#         if topop in comb:
#             continue
#         perm = chosen.copy()
#         perm.pop(x)
#         # perm.pop(y)
#         for c in comb:
#             bisect.insort(perm, c)
#         try:
#             industrial = perm.index("INDUSTRIALSOCIETYANDITSFUTURE")
#             inorder = perm.index("INORDERTOLIVE:ANORTHKOREANGIRL'SJOURNEYTOFREEDOM")
#             perm[industrial] = "INORDERTOLIVE:ANORTHKOREANGIRL'SJOURNEYTOFREEDOM"
#             perm[inorder] = "INDUSTRIALSOCIETYANDITSFUTURE"
#         except ValueError:
#             pass
#         # print(perm)
#         # print(len(perm))
#         proof = submit_answer(perm)
#         if decrypt(enc, proof):
#             print(perm)


# enc = "ea337764dd58a90952dbaa823f7299f7dfe91e2cccdda4989542a6f9dc4b429db4381e157972afc487ebc7917da6864a27157d7c2378c730a7ebb3d6f7dd7f9f027f0423f92db79685635e06ef156d7ea739b00a18ffff7daf9a17538d83248873522924e18f8be8d40a0dc0ad9a9e05915f8ef9b757075fbbb3a162109ae586"

# with open("/usr/share/wordlists/wikipedia.txt") as f:
#     wordlist = [a.strip().upper() for a in f.readlines()]
# print(wordlist[:100])

# for w in wordlist:
#      proof = submit_answer(w.replace(" ", ""))
#      if decrypt(enc, proof):
#          print(w)
# print("here")

# i75 = []
# for w in wordlist:
#     blabla = w.split()
#     if len(blabla) == 2 and len(blabla[0]) == 7 and len(blabla[1]) == 5:
#         # if blabla[0][0] == "G" and blabla[1][0] == "R":
#         #     print(w)
#         # if blabla[1] == "BLAKE":
#         i75.append(w.replace(" ", ""))


# i75 = []
# with open("/usr/share/wordlists/wikipedia.txt") as f:
#     w2 = [a.strip().upper() for a in f.read().split()]
# bla = len(w2)
# for i, w in enumerate(w2):
#     if len(w2[i]) == 7 and i != (len(w2)-1) and len(w2[i+1]) == 5:
#         i75.append(f"{w2[i]}{w2[i+1]}")

# print(i75[:100])



enc = "749b934035f139017ce60688bfee7794d4d692857ebc0751109282a98805130053739ebb04034ebba48bc1400532f2aae578686e87ed2dbb33efd28e0c161f61"
enc = "51b6fd5fe73f014b543ee7874ff6c2adac61711d1727543e54fe0df627503a6ac4d79436f87024185713217e62fb0d8c46a0ab8b62c1526ed0deba788b3bb005"
# "590b1d137d594e7ebdf10b2d7ff9d794f110b76039517a995253c9df608e760097105981ef5c6696c1e0e8415ade90347f6bdedb0ea8a2e9490dbd9c92ddc8b73109c586217bff6ec19ec770f056bde5",
# "70a7967ce7796004d3c7dda9eab6ba8bea11269f9f44f30784c98d20ca2a7a1437b04349bc0093668a3a00179e4e4ee2c1244292f260e37a544a66aae2b5fe3506dbf34eaafe053f23ff4b1cdaf1f8e60b0bcc21583eaea9ad428111b185815b8390c7cc35274f20fa8259d785c62aa1c5bf5837cbd54b24d8ca5f44fe2fd9ca5161d68b7c469a2c5c9c833231c8dd1886d5a647f13494b565b13e9b5cbb586e23fced386a80d604b75486277265ed11260851b50e82d052056984a18dc77f640f4b49b737ff87f17bb81e8b71ca1924d84859373df9b8c5ca4a7c3a4dc3065fea151de170a3a9204935ff947ede5a71f7d909dc0ae99c803dffe19a36c6760295846750b37f7008c2becde574270ab88ac188a2ca9ebf4ebfc60446bbbd3b64790a4115219e3504f4389a400bd39e31ee58cb5d22ba522c1c8132ac433c3b3d7f14136ea4272b238256f8f8330265dbd5b6cf58728f15335eb948a9b789d5c1fdfe1b3d28efe83ac78d2c446a6c837b145e95022fd51cf18656b1352bf636cf823b361569c3b9b044cc06e0a3a1f1b6923a991705f8c7459fde1297ca8296198265c029fdcaef8375b0ac67492553f47a3984119c532d4b9eeb3e872e02c5950758804d1867d8afd476cbf934dcf6114fe5bc705f0d13dd01825d2de81ee99ffbc4b82e8023d5cb3954d199abd22d6c6e5a0e7bc04245903d750dc45cb78ba53169b4977db73a285b90cadb693933f9a7bae86bbfd357744d00bbf32df47047787ae1267c3cab51eb1cd192d5728384",

# names = ["CARLSAGAN", "ADRIANLAMO", "HECTORMONSEGUR", "AARONSWARTZ", "BARNABYJACK", "PAPALEGBA", "PAPALEKBA"]
names = ["TERRYDAVIS", "DANKAMINSKY", "IANMURDOCK", "LEEHOLLOWAY", "VANCERODRIGUEZ", "JONATHANJAMES", "CARLSAGAN", "ADRIANLAMO", "HECTORMONSEGUR", "AARONSWARTZ", "BARNABYJACK", "PAPALEGBA", "PAPALEKBA", "BRANDONVEDAS", "CYNTHIABEATT","DOUGLASADAMS", "FRANCISBACON", "ANTHONYHSIEH", "WILLIAMBLAKE"]

# with open("/usr/share/dict/words") as f:
with open("/usr/share/wordlists/male.txt") as f:
    firstnames = [a.strip().upper() for a in f.readlines()]
with open("/usr/share/wordlists/last-names.txt") as f:
    lastnames = [a.strip().upper() for a in f.readlines()]

i75 = []
for w1 in firstnames:
    if len(w1) == 7:
        for w2 in lastnames:
            if len(w2) == 5:
                i75.append(f"{w1}{w2}")
print(len(i75))

bla = [
    ["TERRYDAVIS"],
    ["DANKAMINSKY"],
    ["IANMURDOCK"],
    ["LEEHOLLOWAY"],
    ["JONATHANJAMES"],
    ["VANCERODRIGUEZ"],
    ["MATTHEWBEVAN", "MICHAELCALCE", "BRANDONVEDAS"],
    # i75,
    # names, 
    # [a.replace(" ", "") for a in wordlist],
    ["GLEBKORABLYOV", "GLEBKORABLJOV"],
    ["HYP3R", "HOLLOWSONG"]
    # ["U", "U ANON", "ME"],
    # ["U R", "TEDKACZYNSKI", "CARL SAGAN", "SATOSHINAKOMOTO", "LENSASSAMAN"] + ["", "U", "U ANON", "UANON", "URANON2", "ANON 2"]
    # dictwords,
    # ["U", "U ANON", "UANON", "ANON 2"],
    # [a for a in wordlist],
]
for out in tqdm(itertools.product(*bla)):
    # print(list(out))
    proof = submit_answer(list(out))
    if decrypt(enc, proof):
       print(out)


# print(decrypt("a71c5c26d99cb5b0a2fc8a78236ea2b939d0d77ffe0239b4bdf58af04fce6c7a", "d6e6702b-013c-469a-8367-b8ac2402cba8"))

# season = "

bla = [
    ["TERRYDAVIS"],
    ["DANKAMINSKY"],
    ["IANMURDOCK"],
    ["LEEHOLLOWAY"],
    ["JONATHANJAMES"],
    ["VANCERODRIGUEZ"],
    ["MATTHEWBEVAN", "MICHAELCALCE", "BRANDONVEDAS"],
    # i75,
    # names, 
    # [a.replace(" ", "") for a in wordlist],
    ["GLEBKORABLYOV", "GLEBKORABLJOV"],
    ["HYP3R", "HOLLOWSONG"]
    # ["U", "U ANON", "ME"],
    # ["U R", "TEDKACZYNSKI", "CARL SAGAN", "SATOSHINAKOMOTO", "LENSASSAMAN"] + ["", "U", "U ANON", "UANON", "URANON2", "ANON 2"]
    # dictwords,
    # ["U", "U ANON", "UANON", "ANON 2"],
    # [a for a in wordlist],
]
for out in tqdm(itertools.product(*bla)):
    # print(list(out))
    proof = submit_answer(list(out))
    if decrypt(enc, proof):
       print(out)


# print(decrypt("a71c5c26d99cb5b0a2fc8a78236ea2b939d0d77ffe0239b4bdf58af04fce6c7a", "d6e6702b-013c-469a-8367-b8ac2402cba8"))

bla = ["EVENINMYDREAMS,YOU'REINMYDREAMS"]

summer = [
"PIRATESANDEMPERORS",
"VALLEYOFTHEDOLLS",
"HOWCOLUMBUSSTOODTHEEGG",
"THEKING'SORDERS",
"ANGELNUMBERSIII:DOMINIONUNDERCONTROLVOTINGSYSTEMS",
"THERIGGEDELECTION",
"HORRORSCOPE",
"THEQUEEN'STIMEMACHINE",
"THEWELL",
"CHINAGIRL",
"ATALEOFTWOBACONS",
]

autumn = [
"GEOQUESTR",
"BENFORD'SCLAW",
"FREEDOMCLUB",
"TOMYDARLINGGF",
"XSSMARKSTHESPOT",
"ANGELNUMBERSIV:OPENEROFTHEWAY",
]

winter = [
"TODIEBYYOUROWNSWORD",
"REACTIONSETCETERA",
"ANINTRODUCTIONTOEXISTENTIALTYPES",
"SHEMOVEDAMONGTHEHYMNALS,SO",
"WHENIWAKEUP,AMISTILLME?",
"TEACHINGANOLDGODNEWTRICKS",
"VINUMDÆMONUM",
]

cryptowinter = [
"$IX$IX$IX",
"THEBLACKBOX",
]

dawn = [
"ARSMAGNALUCISETUMBRAE",
"VALLEYOFTHEDOLLSPT.II",
"TURING'STEST",
"EVENINMYDREAMS,YOU'REINMYDREAMS",
"UCANBEARTWHENWEMELT",
"THEWORLDISBOUNDINSECRETKNOTS",
]

