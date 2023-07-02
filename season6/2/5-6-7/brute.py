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

def pad(key):
    return (key + ('\x00' * (32 - len(key.encode('utf8'))))).encode('utf8')[:32]

def decrypt(enc, password):
    unhexed = bytes.fromhex(enc)
    # unhexed_pass = bytes.fromhex(password)
    # print("IV")
    # print(unhexed[:16])
    # print("Encrypted")
    # print(unhexed[16:])
    cipher = AES.new(pad(password[:32]), AES.MODE_CBC, unhexed[:16])
    dec = cipher.decrypt(unhexed[16:])
    # try:
    #     # print(dec)
    #     out = unpad(dec, 16)
    #     out = out.decode()
    # except:
    #     return ""
    out = dec.decode("latin-1")

    # print(out)
    within = 0
    without = 0
    for a in out:
        if ord(a) < 120:
            within +=1
        else:
            without += 1
    if within > (without*1.3):
    # if all([ord(a) < 128 for a in out]):
        print(out)
        return out

enc = "878e68cefda370428b57cb223367a95bea5379ef3297ab1732f8a242f0ea560bd7364101eccbf638454891d672c30c84ba651c9d714b7d237e3b7079db072da3d8d888378179c848900952581c410b7bccfdb3a339e1a925a746b579f04a82da2fb5a1342fc7f0209512e9b239f6ea5e17d46796db60806f4bf508bff2b45af5b294e5907cddee66906173674b111d7814d6671c3089f30a60d78f64bc367da29fb0e883657164263d2a0934d3d15324ad1bb53b9708d346532164b70a655da488d31ccaaa54bd9708108d311f7c16b010e81c5c45f73caa37f79728c4960609338d7c64187a13819c5fa6029e019ec133dc17a374f35016d66f06a9e5a8ea34121313b57f096dc66696998a218859836266952d0dacad7aae6c0960f2d61557483152d8ceead116fea2dafdfc6fee29a545029c6ddbd4766bbfe6f4066002d0ef819bdd7123309deba1bed72bdad7cb2a3b14cac95487031bc2f4de4c4de17d0df9d8545551f4a89b4d64a5480463a8f68575cb6c77891d2e2f90be564fa437470e5a180e5e59667111fec2b473942f4f874db6ca327395928b96fb9fe2d47777ca6a043459b369f4584e4be6ca78f9c3c266c90f5d5b3ce226870d8803006fcca6848339c061a692a20987efe330b090015e23dd748ca9fa34ac3a1a188999d929d1ee61f7a4b14d9732b9a311989f3de91c25fa1b92e94309c87b6e81fe5f80e2928e9f17774a578dccf361dd4ba43db4f3fb9b52fe8dd5fe38134d361ca0708137d7836ba145688d904daea254f1f8457c296f9e0818aa0be25955ba51967ecefb1b7c00a063ec41e5da77496c45f8223295844deeb36bc520d5fa8863d6ee8a201bfb27292c4af527576dc30b4f64e602ab47af222e2c686641b73219f78d4205bad329a63483a912b4e94a9d139f1f33b474ee5cf4072e26e048e5a98bc1dfd82bd8ed2bbf4fb82194e44f0e91c4205263bd157586a1096977fb2415d7003e56403bfa8d0f962d950a2fdf9e2f65ff8c43b29f79836fa7d518067ddb35936af7f453ac4c5dbce2beefed375217b75044d14dd5a9744cb30d030e57249eb78b851a75e6839faa151e3a9e56f302cf01329236998b2c7948707a289f02c8e8d1fb25d3332611a5f65cf7905b2218ce0be2cec16718c5dd6fe3cad1d2cda72299d2c5662b2c8a821b6d07d56b8d57cd77957fe3c2cccd46996d04fc7dc6255f6f291180096c892b0571a10298003b4e8a04d14d354534459d41d3c96ca8307b4c79b221892ebe1ce6c848139cf6d8166226ec14c9ed5a5ca094a3b793b6606df5ab883f9b967a27ffd6dc01b98e0898b8cc0ad642a8cc2e8af2d0929a679b167da06e087c27408318b3560099bcc2480a423b60c56898f50abe762ac84069"

# enc = "7dc777b4a7b13335c57ff6761e9f8101d4de15a6ed1ee84be4cab3c16387a2ac3ba8050b8d5e51c0092e6a169ed89846092773ef2a6cb1f7398430945feb266b9d784e5638b7605a4a7175fcb525b8e882f0b4d510210c3eadc05da9ca1dec0589947bb937e7fb3d5374b026acf9ad4e0fed9da009d8696854f6db32a5ca4664d9c2bb6f41a1da7b5fbb5cd55f9543bdba9582bcacedaa70023ba54c1d893d4211e9081f60d204bfb512bec457d937d80af00468d78c5487bb6cae864988a90bd4b58cc903f889717d2bcbe8bef091434d57c8dd80d019d6d563dace28c80e6f46add2195d3a03de3f6e836ed5216eecc73e5ace023a797833d5782e1e7f6b17e6b509a2ee2972f0233ec97c1e7c4837600ce04f91c2c481824878fdef4dd85b8ac93698c97f8fbe05b7dd68ffc10142e709c9995daf844473efe97d93c3b62b7fd4b2c2f02ae3716ad9d371096771ce9d029d6569b0f9f009d5260fcdecc17c341dd710f213e013290ad32425f92490959c6deda00ce8477291d6bd16b8b2c9b5d0e33e5c17c168a52e44bb9f9a17a36dc45cff236f6e3bef2071cf1d00226b4873d1a06dee94d6d625f936ab302cd2daea03a74f99de93326128f6569e196fb31ec88713913f1a946325174927d055a84a11c851437125b7d0904bf83c3e2d13cea1d8c89ca3f458ad36937dfe61f46e570ecacff7e7a7e4fce518f8fa1c945e0b4b669cce49c2e67a213e6f7091d35554db980c06ecac77fe17dd8368d23f159eec4165c2bc49c7c31aad83ab4d869420768a0f0390510e9e645a00818de4255f99df0cd795e7df34161894146c48ea018388fea84aa3aba50bcb4004e6a3fd0988d4022631d1a5744e58cb1b8d9b47342f28ad4b99939bf55e0ee181bbdc22e8e8bd342a900657c5c2a71a32c7f592f1bc3e73ce88316a5750e9676b6b5b0be04a52d3dff95be40513508e39d7f320f7290ffa1e8806e2ff6431bf7e6a412c6166daa02253096afe614a5264b48a80f9f32c6985fce620bbcb254065b722f667de8f49cd9e330673977faec2d0a0d511b5ac185ea37e943a02b39e8025c9581f80d0df70d43398fd35c0af5e8f21c4b804fbc9e42ee2667a6a46b5214d4d53fcde5b4ce0c04811c5ace334435ce83556390918119d7c0f6241a80778f039db9c4db937ee619c30b792aa5b6224128dc4e163d1f67940af62ab2a7f20c4126b293aff41d8af21b6b717e00f33583fd9f0c89ed766e53fd63fff2e999854f575441635ce9618b82814a84df9677e357a70fa7522257191caf542a84bf553b4ef7ee22439f000487c276accaef61805111e6fe372184e7d1bafc79f9e7b530e823e26876debd67fc34c3a3c2f0fe1c309058fe9bcd9fee348b26d62126c50bf472b2a94dec5d336bed63f605745dcf0a0afd7ccad53c0194e3d4c324c328010882b88875ee17add20fd4e176fb1513927b70b78fba05bbb34e3dd8e3dfe1361ba9547f1fb86d25b4effc7ae3fde6ae1db212958dce17f1c5b685131ddde3a7ff75a64f169555f62c2b2ac0172e093562310589777d31a2cf94969b6c782e755679807f3a7e152b4a3fe32af1ebf8f24d7d89a9f83b2760dfa17ea311b5e2510e79f1fbff03c070d71967d3afbced6b3dda13f7ca6812e68d0ff14fa98120fc789f463c964f8e09dcacfb3e60dfb1a1031d3b913bbeefd1b2f3742a67a1892552ff056ff11534fdd9be2a6b1719d0722e15d9c9d3d984cec07a1ba7bbb442d944b37aa553f4df73021050dee33d0fc347e6c9870c360a58ce079d5f0fc3faf230282c6aa55a546b3b2b3cccd3278b37bc9f640db230a0621e9771a08c0bbca8772c784de9be6d201d0733972a987a44d871320f07c68b3e72ac08f52804e651430dded9ea15e2f5c73e4fc34e9d14ce42cf18dfd1eb897681f252cee2f1f1cbe5f7c71b64ea29936d2ca43954e0873f9126f16dd5aed74d435537e21720ca6cf70a0d3ba9df7e57206469e4bd40f95c6f283397bedd7a057e737c67ce4fa3b29b9e641d4e21f4004c69bc6dc381295bdf36420da6c4e472c2439c808883f484a8566844285fe71c955e2a90175f517b47bd0dcbacca3cdcaca11b665416c38af604b7e8afb7c75ae08a00a8963d0069f37bc39de889bf8ec45d92b78dc168a4f0f25f4bb06938a6c39e81ffc6ddf687796bc14c53454fba7fb1e3e89fab4f381be97f5d4fcb1f62a9133057b99d117a3323ffa7b6977ade9ba929910fe908374650654fb6091133795319473f941c1ffd968faa0de5da6b00d32e35b523b37a7c1a4c922996102b4c75ca3816a0adfc44024e6b9859def50d2357f8ed6c2f295d133f39c3e4515391acaf7a52cebd969a7853a1755b181eba67c78025f7b2ab4e77ce5a701eb763dd5aee6ff9043ea7abeb156f3b9d34605e3e00ca0a88adaa436548124b0b4a8a9acc6fabade0261d668daf6753d44b73420c0ec72b9152e7da5f1c7c4da615b6ba5eeea94ab832828202abd6089758201e8c282774ef7ee71bae4d416ddb9f2da304779c73823b2f391edf71fcfc018a4c37fa4e070eb59e710dc7c4d0941cf1e065d05f574b6a02e0e61dc025d10d9ab7eb3bd89336a98d41cebf36232c58338331eb1f6779f23263d2d53f1e7007f33e0f88c208a24a4f9f40daf200e1c8e72d46c0c7788a82241f999f7825ea6219226b5e44dd9d3b833a116f3fdbe9ee4922fd5cb384d00d3c2414ddbaa03c91802a6d22aa515a7e9a3ec91db9b63b221dcb2a2e2a06759fd278fb35c61109cfaaed7d8941005b3536713e3e04a30341455153e3da6e6eeb383cef8b8721fb3e3e265df18c9c77c3b743b724f77b0f3cd067ec39b58364de0394a1c589b28d312eb7a7fb93d62ae4627010c85a995ccb09c2a0263e5cbf84f1900ad5b1bcc55e85be3c76e74703874414fec484bb9d75a3796ff62ef63b5c8fdd2345ff4515eba2862fa879f08da3f341b0910212b04119d0ea94de3af19d4b6512ea7330c80a14c136a18707ba4ee25f1d6090cc6023e6adbd13960d95521aa413bfc286ff692c070d4f9d689eddc5822b585e6cdd0b4a530b0e96f6033ae6db4df49dfc0ef5e8d849db6a4021c7b13e34f14dc01ef4bb992ccd5bef91a91b0d3bd7516f561118cc39e52a6480f66cacdcdf48d412916a01d3c795ffbcc687c4cb08f09891e700a5a231ab748dbfcb389ed0090d2002f1b0fa6c71157f7702faa125fd6ea84ef173f06516b1bc685905711e039d22850687ad569def042d918954e1954190c508089e4389e7cb19b786e96fd5c89cec7bd94f7f0c3b4861deda673714c4064b0ca15f175cfda99418277c8b6f822da7604eead3b8b7a3c29bc06251d3609227016fbb24c4e268ed91f682c9da5d9aacf3693c770bf1fefcbca7e436e0fccf26ebbe2cc732b46059d878b798c56eaa04e799dc53b5cd603886cf7868b69fd910f32cf471ec0c621a5179f11868e347bac796fea8b8988bfe36c513c7eea3e49e1c9c20b590a3c4b01426f2e11ff5c40d3cd0f082015697dc28965841e439475c0c10662ec088ac56f4438f8316357bd5f8cf35601906d0f58fded26b1837d2fc77ccf30e006a54f10ba25efdf4fbe772ed34418735f13c9eae26df5c4a56e89f819bfc1781ea5b58656a7c8a30ce281a2f5587749c4ab835816e5fa6508a364b69c9472ee402deb0c862c959fbd4c7680cfa92d63b3f74317298d4accd0a9c0455341accc8e6c6de5e7e43e94238b1d87281833bc779ad1c110573ac00a73f0b4d11fbd6352df402aebd614869b7dfab39ae359ab8b1bcdf83bd039f3c1fbd5d18d216925c1a5cf932ad154fbce2bc47fe193c3590ac45348fad27b34fa67cd4ded9af4bd9cb61d4cbe1ed79abad101b1a1877915d24d22edf9"
enc = "ab4fa19dd3335e2481980945f3088794fe0f98231db5d481cad08ebf100cbf7ab44c38802a0d304d4234dca8abc8a6c70c15d21c7b430a5c9fdf5b95058706625448589fc82c0e386ccac313db8aaaa7b582d3f98ab3cf73a98f8d62ce0aa884fe39f7b074bc9d11b802dce9e0d2f6fcea9f200422788cd1e1de08e8ef6c9e89d19c87dc23d734c060d3ce02b4899dc36a20af3a02e1bf5e57775a202758152ec6993aa8c0204759adadbe1c75e326119731189d829ec3f76e18fd4b508193bc00df3f551a47aacdc6a474f65b067e33c9205f74a9480981308faa8f22a18199a729a1f498012a0929413ad8e6598c7e8c954873993d063f3bf1bc4636fa847ff71c24568833a472dfc806d790170c6d19e9a824b5e23105e4e672df01a81645eed656bdc8237d1df5eb850edc38875b828031944bcde6f09caab4b7fa903e9e7cd0ecff1fbad6ec97fae8e72b7c3f2556decf0c0bdd4f3425a6a1a95ebcdec428cc0150996af0c9d8771c91dbb494ee4c5ef5c04fbd600f490a61806a2e461ce1a4561ee437eb48be5a18570d922ee35212b0c78acb34ae286dafad0eb0392a9c6fc9ea3f60f64a1faf8f48c2823d1f20cde06ec85ab277daeeb6a6ba0ff82426553dd85c3e2a555fa6255dba407cb83a5bf035830e294fe486dd0eabdfe315"

with open("/usr/share/dict/words") as f:
# with open("/usr/share/wordlists/eng.wordlist") as f:
# with open("/usr/share/wordlists/entities3.txt") as f:
    words = [a.strip().upper().replace(" ", "") for a in f.readlines()]
    # words = [a.strip() for a in f.readlines()]

# words = ["creepscore", "creep score", "CREEPSCORE", "CREEPSCORES", "CREEPSCORED", "CREEP SCORE"]

words = ["Make Mine Freedom", "PINIONSVERIFYINPGP", "PINIONS", "MADNESS", "EVERYTHING WILL BE ALL-LIGHT", "ALL-LIGHT", "ETIDORHPA", "PURGATORY", "Water Music", "Firebird", "CONFIDENCE MAN", "HERMAN MELLVILLE", "INFERNO", "CANTO V", "CANTO IX", "CANTO XI", "CANTO XXVII", "CANTO XXII", "MAN CAN DO VIOLENCE TO HIMSELF AND HIS OWN BLESSINGS", "VIOLENCE", "HIMSELF", "BLESSINGS", "LIFE", "DEATH", "WOUND", "DRINK ME", "PERFECT", "Valhalla", "sulphur", "IT IS A VOICE INSIDE YOUR HEAD", "Cicada 3301", "SEX AND CANDY", "SEX", "CANDY", "Chatterley", "VIRGIN", ""]
words = [a.strip().upper().replace(" ", "") for a in words]

for w in words:
    # print(w)
    if decrypt(enc, w):
        print(w)

