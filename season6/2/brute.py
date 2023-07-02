from hashlib import blake2b
import json
import itertools
from struct import pack
from binascii import hexlify, unhexlify

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
    return json.dumps(message, separators=(',', ':')).encode('utf-8')

def generate_proof(message, depth=1):
    magic_bytes = b'\x05\x01'
    passphrase = stringify(message)
    # print(passphrase)
    length = pack('>l', len(passphrase))
    return hash(magic_bytes + length + passphrase, rounds=depth)

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



from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt(enc, password):
    unhexed = bytes.fromhex(enc)
    # unhexed_pass = bytes.fromhex(password)
    # print("IV")
    # print(unhexed[:16])
    # print("Encrypted")
    # print(unhexed[16:])
    cipher = AES.new(password[:32].encode(), AES.MODE_CBC, unhexed[:16])
    dec = cipher.decrypt(unhexed[16:])
    # try:
    #     # print(dec)
    #     out = unpad(dec, 16)
    #     out = out.decode()
    # except:
    #     return ""
    out = dec.decode('latin-1')

    # print(out)
    # if all([ord(a) < 128 for a in out]):
    if "bit.ly" in out:
        print(out)
        return out

# enc = "f7d58219f0cc3754c8fdfe40ffc661b577b084e70a120b33dede3fa473b1e229b3677bfe89d7079aa97fd385de42bcef"

# secret = "1ded532de28702c0bf7a979e2c46fdc72c333b8874bb4c76a3a44a4affb16aae"

# enc = "b6fcd4aa0fc2261c1ad7d1ccd8f4db2b26dd0bcc90909caeaa88fb84fd80715804a340f1aba6889708e2e377136e1406d359b9ca5fab4424521526c8a94b1aaa429c4354534e571088c06b1f75cfc6585b861498ba61afd2acadd6574aaa5272a8e020f536f177c210b5056cba505d16e337c16b5a67d6605050bd05640dea5bd3deda0cddbd712250da33a1d4dc1b2b2d4453a12c7e3a1ea840c8d1a91b9920d7923a893331a6bf51be63fc74879e8348cad07c75a3fe6e688f89c5bc5610d81a77e49433c832e821c74eb73e8cb028c1301c2d8ef9d0d9fa927545272316a47836a7cc994d31e73e2358b0a2e8fb1960e07162e68777383c6c5ea0172195e28031ad3378f9bf6ac71b19c31efd9bbb90f1de4e9e47c5a7cca2a2e89c32d53cd089d41b32077bcbd3e1df0a70e9d32020065c24bf5cb1f5c4012a4f32c45da68da142d72d00fb2a349b397a2476fb7971baf98d3349ae19834629b02f185ef1"

# secret = "d1f48a4255c77f557ac7aa2b7ff4048d9ec4e0dea9609bbd990f67cd84e9cb2e"

# enc = "b6fcd4aa0fc2261c1ad7d1ccd8f4db2b26dd0bcc90909caeaa88fb84fd80715804a340f1aba6889708e2e377136e1406d359b9ca5fab4424521526c8a94b1aaa429c4354534e571088c06b1f75cfc6585b861498ba61afd2acadd6574aaa5272a8e020f536f177c210b5056cba505d16e337c16b5a67d6605050bd05640dea5bd3deda0cddbd712250da33a1d4dc1b2b2d4453a12c7e3a1ea840c8d1a91b9920d7923a893331a6bf51be63fc74879e8348cad07c75a3fe6e688f89c5bc5610d81a77e49433c832e821c74eb73e8cb028c1301c2d8ef9d0d9fa927545272316a47836a7cc994d31e73e2358b0a2e8fb1960e07162e68777383c6c5ea0172195e28031ad3378f9bf6ac71b19c31efd9bbb90f1de4e9e47c5a7cca2a2e89c32d53cd089d41b32077bcbd3e1df0a70e9d32020065c24bf5cb1f5c4012a4f32c45da68da142d72d00fb2a349b397a2476fb7971baf98d3349ae19834629b02f185ef1"
# secret = "d1f48a4255c77f557ac7aa2b7ff4048d9ec4e0dea9609bbd990f67cd84e9cb2e"

# enc = "d990e0e553649e2ae9785bb3758a90d97d373cb5635be877d5cedd32cc31242ec9212aa126a5613f85bec0dba16a8d2c52a1feac1e43aec781cb91a4b7bbfe2ead71ccd1bb60ecc044098dab4dc9abe549e183f10210868591d81ad192001cac011bcb81c48635f87d85c95a64b18635e3570020b3116146ec6cc6674d3d7e0d46a53fa5c352ddb473a8fabe85a4d8b38da94b6257100d2e857f382f48c0e4706cc7c055e91bfb3655d894320eef0f1a72c371e857a2d792289da5343a58b31ad9d83cd797be2613a6e16feb4a98fef37a2fc9a860397db4bbb24262b936626a76dc0371adda47c802c0e9b50a0741055a29138aeed20ba75d00d4cef31e714f270d3bf3fb30a8c7b522db2121e1420bb5ae8dedab25475aaa953cbceab49a34f302e481a6d66252a6ee91bcf961efdd2ef60551d6a9df9fa3294f5c214a2d8efc8f7010ed6420003e4fede2747e22cd0a1a67874f6e8b6e48c2d09de78eef3382851df331c664021e72d0fe1b258b8ad3756cb548e8b69c5a166ab735a9ec05486b18eb719e9f830dfc10b89aea9ffe152ae885fed1aba02c354bb20f3a00a60712cdf802db6098fdd89766497bf22d817fc5013f53e365a0ca1960e41b767399f312bcd204cf25060be7d1a3d2d39931042063ae142bfca762d0c05f5c0b8b5f5814a3f044a7b5ffd0510040767be550716923ce408f33bd889aa565e705a65c34a512bc7928e84884ce09339ca98110f490e09ec2b395a43ece9774d95d2b3998534404f12c4982eaa48b2b41da75de535ac5e7c244df206c1b75670b940f48ae4544e0d35fe16bf7b1be418fd410ffaf82e58eb354822a0dc1674a732b3e5c3d0e0aed5b145546c3dee409d63fd4933bbe9780ac56c9a5fcbbc17c2bdb30110548b6be69d40ba4cb234a4277e449f26859353c22784948d82d5cb2cdf245c80e4ac21c870e0fb195b0cd59cd6b7c531ade6f415ecff27696a264d8897fc67699d727affb55007317e51f7e1fb6851cd3122098447811adb0d0a50d8fb26d5851e9210674c859b0004acc8f418184ccfdabce02b4691a2bd881e090657820079578650846c8ae30a5ae55b0fd2b5228e4f4abbba6887d9784e0ce45b88c7e8d6541f12093c368d4873c25d0e117b0b1d1d39f8a37936ce3a3ca62e03792d70e68a32fafc75e6df5d02a6757d05984b9ef4ad2160c364a78248ea77820f66f91d7eed31686b14a7b29c26c376de9a4bd3eafcd9b0e48ed4046e4fa88593063a955d8d8672465f90d2b73601035da996ed90ea19210d1842aa0907283cae57c0af2230e51d0710d777236c11d05a47a54309aba4e9b54c237d3e29942a0eb3d44ab9091897802e984205c9c91c8f3c9806a1aa5e8177f7bb853ae88a3b48c926f4672c327ad656649c357eaf99df3778edac86d9abc5e4f0f54bfe38eddcc99a68b5bf9f1f7aa702013070811502c7f9ffbeed7cd219d11d26f80f6ff84226811d8ef1104bebd9fc59c44ba42cec17a8fee22d3d081ee20b7ece11b817c6d214b266686a58e3c91cb12d74798a173e18400305f881e28599c605d0abffe7a1888eb82022a59eda0a153b661fc4503e5381e44a543879b6a2cb375e1088a40f0a279acc7d8b546ef7292e804455733a37a15bbd24c39afc289d5bcc1e6dee4e468221a074ca731b77ff9d68eb11564d4b229e3ac526cdc2ad9c26d68df8e49c4354330ab6fb8e1b1aa9f11d0c96d3d173e857ca0667bda88c1179f9c4d12e50091cf100e147a280e07d2d9b3789dbd0c9a15546df72947de6c1dcaea5f0d8fd12e55f3dd42da515058faa6199b720d97084e8d42d9782ced12bf602236961b99c7863bd20a62d9a335e747e557c5a954a22e2d440f01f4327d2a391c9db6270cb71733babe26610c143a5e118ce3a38e7090187dc752b288a186ffb0503604bb7b956e50edc31d237f111c21925a11d87b82dd0a74211201f237fa5117bf54d70b6b442a08707e43ec1efb1fb5a1e71b5e1fa0e6588a9e5e87405292d98ccc613d74741a5691c1e61595885d29cdb773945063afcf0522eeb516e35dc987a0462e6613bd3b2a82ebb1f6b705f3870497d20dac573df33ffddd077835d83797e149c0f3cbc9d51e63c3bc4241730f545fb09672607713d78a2ce6810f609673fa05459e82b10fa753333aae85637c4a797a8a80745fed71587a35a38c437f7c1e3e5e82ef2e45b3de2cc4ae9fe2a44a86e9040b068273fa8316735c298e07cfb5ce9970f612e4efa24f4ab63d527b8a12f4397e15b5ba1f5590b06eae9e5c3291b089e8332f12e820a2d5a30da5313ca75d40f56b30429c6bfc5315244b7f6521e6ccdff479fe91115002e9401b732c45d3ce5873f0cbbfa80ce61cf37f5f1bba0543e9353726a1d5641410c571b0e4f58f1c95691ada9a757abcf44678971d4435d2d84d3ca11f8baf8df95a2309b89a71850217c308e72ecf8a7dfa5347845850e576ca1638db3a9229ffeaf37fe0584d9b34988fce55aa419021ffbf8c992a4549add8df602fec96ae5e1e1adff1e8c7b8f266e838633f7bb39756d01b7c42c4a29c2b0b71f506042ed51449fe54ef5f1e575c63460564fb660816f31e1846fd4bb391fdc4a978da34f8fdb3347d465028955f0aac383f37589d963356261641938c7a1fdad8c2454ba47338549005327e807736309f44107b19f53bf6c371a7276192f57d347b121d3cdd4bdc564e"

# secret = "782cc7422e60c651ba6b174ef6858ce60a68766ab09dd9d9440129984f66ed19"

# with open("/usr/share/dict/words") as f:
#     words = [a.strip().upper() for a in f.readlines()]
# for w in words:
#     proof = submit_answer(w, secret)
#     if decrypt(enc, proof):
#         print(w)

# enc = "d990e0e553649e2ae9785bb3758a90d97d373cb5635be877d5cedd32cc31242ec9212aa126a5613f85bec0dba16a8d2c52a1feac1e43aec781cb91a4b7bbfe2ead71ccd1bb60ecc044098dab4dc9abe549e183f10210868591d81ad192001cac011bcb81c48635f87d85c95a64b18635e3570020b3116146ec6cc6674d3d7e0d46a53fa5c352ddb473a8fabe85a4d8b38da94b6257100d2e857f382f48c0e4706cc7c055e91bfb3655d894320eef0f1a72c371e857a2d792289da5343a58b31ad9d83cd797be2613a6e16feb4a98fef37a2fc9a860397db4bbb24262b936626a76dc0371adda47c802c0e9b50a0741055a29138aeed20ba75d00d4cef31e714f270d3bf3fb30a8c7b522db2121e1420bb5ae8dedab25475aaa953cbceab49a34f302e481a6d66252a6ee91bcf961efdd2ef60551d6a9df9fa3294f5c214a2d8efc8f7010ed6420003e4fede2747e22cd0a1a67874f6e8b6e48c2d09de78eef3382851df331c664021e72d0fe1b258b8ad3756cb548e8b69c5a166ab735a9ec05486b18eb719e9f830dfc10b89aea9ffe152ae885fed1aba02c354bb20f3a00a60712cdf802db6098fdd89766497bf22d817fc5013f53e365a0ca1960e41b767399f312bcd204cf25060be7d1a3d2d39931042063ae142bfca762d0c05f5c0b8b5f5814a3f044a7b5ffd0510040767be550716923ce408f33bd889aa565e705a65c34a512bc7928e84884ce09339ca98110f490e09ec2b395a43ece9774d95d2b3998534404f12c4982eaa48b2b41da75de535ac5e7c244df206c1b75670b940f48ae4544e0d35fe16bf7b1be418fd410ffaf82e58eb354822a0dc1674a732b3e5c3d0e0aed5b145546c3dee409d63fd4933bbe9780ac56c9a5fcbbc17c2bdb30110548b6be69d40ba4cb234a4277e449f26859353c22784948d82d5cb2cdf245c80e4ac21c870e0fb195b0cd59cd6b7c531ade6f415ecff27696a264d8897fc67699d727affb55007317e51f7e1fb6851cd3122098447811adb0d0a50d8fb26d5851e9210674c859b0004acc8f418184ccfdabce02b4691a2bd881e090657820079578650846c8ae30a5ae55b0fd2b5228e4f4abbba6887d9784e0ce45b88c7e8d6541f12093c368d4873c25d0e117b0b1d1d39f8a37936ce3a3ca62e03792d70e68a32fafc75e6df5d02a6757d05984b9ef4ad2160c364a78248ea77820f66f91d7eed31686b14a7b29c26c376de9a4bd3eafcd9b0e48ed4046e4fa88593063a955d8d8672465f90d2b73601035da996ed90ea19210d1842aa0907283cae57c0af2230e51d0710d777236c11d05a47a54309aba4e9b54c237d3e29942a0eb3d44ab9091897802e984205c9c91c8f3c9806a1aa5e8177f7bb853ae88a3b48c926f4672c327ad656649c357eaf99df3778edac86d9abc5e4f0f54bfe38eddcc99a68b5bf9f1f7aa702013070811502c7f9ffbeed7cd219d11d26f80f6ff84226811d8ef1104bebd9fc59c44ba42cec17a8fee22d3d081ee20b7ece11b817c6d214b266686a58e3c91cb12d74798a173e18400305f881e28599c605d0abffe7a1888eb82022a59eda0a153b661fc4503e5381e44a543879b6a2cb375e1088a40f0a279acc7d8b546ef7292e804455733a37a15bbd24c39afc289d5bcc1e6dee4e468221a074ca731b77ff9d68eb11564d4b229e3ac526cdc2ad9c26d68df8e49c4354330ab6fb8e1b1aa9f11d0c96d3d173e857ca0667bda88c1179f9c4d12e50091cf100e147a280e07d2d9b3789dbd0c9a15546df72947de6c1dcaea5f0d8fd12e55f3dd42da515058faa6199b720d97084e8d42d9782ced12bf602236961b99c7863bd20a62d9a335e747e557c5a954a22e2d440f01f4327d2a391c9db6270cb71733babe26610c143a5e118ce3a38e7090187dc752b288a186ffb0503604bb7b956e50edc31d237f111c21925a11d87b82dd0a74211201f237fa5117bf54d70b6b442a08707e43ec1efb1fb5a1e71b5e1fa0e6588a9e5e87405292d98ccc613d74741a5691c1e61595885d29cdb773945063afcf0522eeb516e35dc987a0462e6613bd3b2a82ebb1f6b705f3870497d20dac573df33ffddd077835d83797e149c0f3cbc9d51e63c3bc4241730f545fb09672607713d78a2ce6810f609673fa05459e82b10fa753333aae85637c4a797a8a80745fed71587a35a38c437f7c1e3e5e82ef2e45b3de2cc4ae9fe2a44a86e9040b068273fa8316735c298e07cfb5ce9970f612e4efa24f4ab63d527b8a12f4397e15b5ba1f5590b06eae9e5c3291b089e8332f12e820a2d5a30da5313ca75d40f56b30429c6bfc5315244b7f6521e6ccdff479fe91115002e9401b732c45d3ce5873f0cbbfa80ce61cf37f5f1bba0543e9353726a1d5641410c571b0e4f58f1c95691ada9a757abcf44678971d4435d2d84d3ca11f8baf8df95a2309b89a71850217c308e72ecf8a7dfa5347845850e576ca1638db3a9229ffeaf37fe0584d9b34988fce55aa419021ffbf8c992a4549add8df602fec96ae5e1e1adff1e8c7b8f266e838633f7bb39756d01b7c42c4a29c2b0b71f506042ed51449fe54ef5f1e575c63460564fb660816f31e1846fd4bb391fdc4a978da34f8fdb3347d465028955f0aac383f37589d963356261641938c7a1fdad8c2454ba47338549005327e807736309f44107b19f53bf6c371a7276192f57d347b121d3cdd4bdc564e"
# password = "How to Disappear Completely".upper()
# password = "HowToDisappearCompletely".upper()
# proof = submit_answer(password)
# decrypt(enc, proof)

# password = "LIMBO"
# proof = submit_answer(password, secret)
# decrypt(enc, proof)

# password = "SÉSAMEOUVRETOI"
# enc = "d6cf9e0053ec5c0fd7dc9b33ffedde9a4e49f46f1a0b7a74847f7e376e1ab26a"
# proof = submit_answer(password)
# # print(proof)
# decrypt(enc, proof)



# enc = "50947b031027da46a447330ffe37ba4adec5a43a7a3da86435a9fa24c177ffeb12719ad36ddc39cf3aa4b7da9c9d3dde58bce38bf588fcbcf64d03f5550e4de7de1cab258b18924d179a6f2be913f968490a1f5dfd04a65bdc289b5df76761c4dd4ab8c0b49caa419eb7a3c009c194d879ebbd5fe0c5edb56517f31735f9ef4e86b0849680978249bc1a0889fbf1b04f7c9376c14ceb431973f83f5caf01f5f4c7f0420667defc0614e0550846ed5d07037276ef468cfd4cf1c41046601b747fa23101f792d8806ec21ab6304c99bf070bf6f2dd3d445949f6738d384e5054b4a8793cf390ba239c58915c6994e80de836fbb61cbb5e5eb7f0c17bae692c438ecf6b8931f3f0a9453a7b9664cdb015f921d76aa00a4bf3cb992eda691beae816debc35f5c1effff25dbfd92894d95e3d03eac7f36d4f2c015a9a4093a60fa1734011eae516a46d0b4dc19051676bbb180f67171d60eb01e89bd2e0b504a0d1eb6e6dc985b62aa9dd52649d309ea39a6dfbc954497c86f981c4373f5f095cbc34c6f88c9abc606e8a9ffbdb57feab90935aa64a3a3ae109c06e9880d9b3b5bb45ecde4629a0f171f7b176f4dcae42b2ff1ecc01f9166e715b078c1fbe4837c265272b0320d1193923ef5514020afbdafe"
# with open("/usr/share/wordlists/entities.txt") as f:
# with open("/usr/share/dict/words") as f:
#     words = [a.strip().upper() for a in f.readlines()]

# for w in words:
#     proof = submit_answer(w.replace(" ", ""))
#     if decrypt(enc, proof):
#         print(w)

# bla

# enc = "dbbd20ecf2fcbc308d02512cab5ba53da14a56bd867b34bbfa3e05a66296bd2363a92f737a42ddf5a3c57e889cd2fcdb59a16c0a1f9fb087a03869c3e855fee9aaea2b67fa96a770a0c19271418403e19ffdf53c110af57c5721de9b7ee344aa40443e3c69c78477c93d1405851d38fc2e5a52a92270918a598825e071896f0b0cc1b4502bfcb574429c9a23901cf7e30484a893e6b94fe4b45fdab6800b3696"
# # with open("/usr/share/wordlists/entities.txt") as f:
# with open("/usr/share/dict/words") as f:
#     words = [f"WEST {a.strip().upper()}" for a in f.readlines()]

# for w in words:
#     proof = submit_answer(w.replace(" ", ""))
#     if decrypt(enc, proof):
#         print(w)


enc = "d6cf9e0053ec5c0fd7dc9b33ffedde9a4e49f46f1a0b7a74847f7e376e1ab26a"
enc = "58eea5af60f6e2642905f8a1a2317896a1d4d5fb7fb47aab0a34b0ee9f85f2f0"
# enc = "e5000f2e5b44fe797b6edb4f5775aea04dbe1e1cbd38cf88f1ab9c4002601bf2"
# enc = "c0203eddb0e8757ec88f21b0eeddd2c3f74ff94f979336554bfd0a3e1922e609be0708d3796646a93cdca64b24d82048bf74c46e0eace288d4ab1ab97e02c48a6513b8dbdcde0a93820b0267f45b47d1f22b7205cabb18b2c393a52323b799e13b22d3dd4a012177092738a1cf6772ec8db7ee86f179ee6e94dc3c148966e8eb2eddbb352d9cca034d567a489e633ee1e818f182c20f45f294ad54f5e5ae8996cdc4bc0616af880e018c554bdcf78ef569c0ffc9bae36dec3fed6be712f00d81fb900f48801f5fe4d480f93e4ada66825d66536b85d221c1971e01fbc32f994d4278351ee9150b798dc1abef1ce742865f46118ba06747328b48189d1faae7ed"

# with open("/usr/share/dict/words") as f:
# with open("/usr/share/wordlists/entities3.txt") as f:
# with open("/usr/share/wordlists/eng.wordlist") as f:
# with open("/usr/share/wordlists/rockyou.txt", "rb") as f:
    # words = [a.decode('latin-1').strip().upper().replace(" ", "") for a in f.readlines()]
    # words = [a.strip().upper().replace(" ", "") for a in f.readlines()]

words = []
# words = ["5-6-7", "bit.ly/3IiqhFH", "https://bit.ly/3IiqhFH", "BUVEZ-MOI", "BUVEZMOI"]
# words = ["EVERYTHING WILL BE ALL-LIGHT", "EVERYTHINGWILLBEALL-LIGHT", "EVERYTHINGWILLBEALLLIGHT", "MAN CAN DO VIOLENCE TO HIMSELF AND HIS OWN BLESSINGS", "IT IS A VOICE INSIDE YOUR HEAD", "VOICEINSIDEYOURHEAD", "SEXANDCANDY", "ETIDORHPA", "DRINKME"]
# words = ["CREEPSCORE", "CREEPSCORES", "CREEPSCORED"]
words.append("PINIONSVERIFYINPGP")

wordlist = """The best known example of quantum cryptography is quantum key distribution which offers an information-theoretically secure solution to the key exchange problem. For example, it is impossible to copy DNA encoded in a quantum state. If one attempts to read the encoded data, the quantum state will be changed due to wave function collapse (no-cloning theorem). This could be used to detect eavesdropping in quantum key distribution (QKD) of the Q.E.""".upper().split()

for i, w in enumerate(wordlist):
    try:
        words.append(w)
        words.append(w + wordlist[i+1])
        words.append(w + wordlist[i+1] + wordlist[i+2])
        words.append(w + wordlist[i+1] + wordlist[i+2] + wordlist[i+3])
        words.append(w + wordlist[i+1] + wordlist[i+2] + wordlist[i+3] + wordlist[i+4])
        words.append(w + wordlist[i+1] + wordlist[i+2] + wordlist[i+3] + wordlist[i+4] + wordlist[i+5])
        words.append(w + wordlist[i+1] + wordlist[i+2] + wordlist[i+3] + wordlist[i+4] + wordlist[i+5] + wordlist[i+6])
    except:
        pass

modded = ["".join(filter(str.isalnum, w)) for w in words]
words.extend(modded)

print(words)

for w in words:
    # w = f"CREEPSCORE3301"
    proof = submit_answer(w)
    # proof = "6666617f35414d95e3b1864e10137d4359c87ae23d2231badb592c81d7d6ebae"
    # print(proof)
    if decrypt(enc, proof):
        print(w)

