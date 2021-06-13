const crypto = require('crypto');
const fs = require('fs');

function encrypt256ctr(text, key, civ = null) {
  const IV_LENGTH = 16;
  const algorithm = 'aes-256-ctr';
  const ENCRYPTION_KEY = Buffer.concat([Buffer.from(key), Buffer.alloc(32)], 32);
  let iv = (civ) ? civ : crypto.randomBytes(IV_LENGTH);
  let cipher = crypto.createCipheriv(algorithm, Buffer.from(ENCRYPTION_KEY, 'hex'), iv);
  let encrypted = cipher.update(text);
  encrypted = Buffer.concat([encrypted, cipher.final()]);
  return iv.toString('hex') + encrypted.toString('hex');
}

function decrypt256ctr(text, key) {
  const algorithm = 'aes-256-ctr';
  const ENCRYPTION_KEY = Buffer.concat([Buffer.from(key), Buffer.alloc(32)], 32);
  let textParts = [
    text.substring(0, 32),
    text.substring(32, text.length)
  ];
  let iv = Buffer.from(textParts.shift(), 'hex');
  let encryptedText = Buffer.from(textParts.join(''), 'hex');
  let decipher = crypto.createDecipheriv(algorithm, Buffer.from(ENCRYPTION_KEY, 'hex'), iv);
  let decrypted = decipher.update(encryptedText);
  decrypted = Buffer.concat([decrypted, decipher.final()]);
  return decrypted.toString();
}

function encrypt256cbc(text, key, civ = null) {
  const IV_LENGTH = 16;
  const algorithm = 'aes-256-cbc';
  const ENCRYPTION_KEY = Buffer.concat([Buffer.from(key), Buffer.alloc(32)], 32);
  let iv = (civ) ? civ : crypto.randomBytes(IV_LENGTH);
  let cipher = crypto.createCipheriv(algorithm, Buffer.from(ENCRYPTION_KEY, 'hex'), iv);
  let encrypted = cipher.update(text);
  encrypted = Buffer.concat([encrypted, cipher.final()]);
  return iv.toString('hex') + encrypted.toString('hex');
}

function decrypt256cbc (text, key) {
  const algorithm = 'aes-256-cbc';
  const ENCRYPTION_KEY = Buffer.concat([Buffer.from(key), Buffer.alloc(32)], 32);
  let textParts = [
    text.substring(0, 32),
    text.substring(32, text.length)
  ];
  let iv = Buffer.from(textParts.shift(), 'hex');
  let encryptedText = Buffer.from(textParts.join(''), 'hex');
  let decipher = crypto.createDecipheriv(algorithm, Buffer.from(ENCRYPTION_KEY, 'hex'), iv);
  let decrypted = decipher.update(encryptedText);
  decrypted = Buffer.concat([decrypted, decipher.final()]);
  return decrypted.toString();
}

function encrypt(mode = null, text, key, iv) {
  if (typeof mode !== 'string' || typeof text !== 'string') {
    return null;
  } else if (!text.length) {
    return null;
  }
  let r;
  switch (mode) {
    case 'ctr': {
      if (!key) {
        key = '';
      }
      r = (iv) ? encrypt256ctr(text, key, iv) : encrypt256ctr(text, key);
      break;
    }
    case 'cbc': {
      if (!key) {
        key = '';
      }
      r = (iv) ? encrypt256cbc(text, key, iv) : encrypt256cbc(text, key);
      break;
    }
  }
  return r;
}

function decrypt(mode = null, text, key, iv) {
  if (typeof mode !== 'string' || typeof text !== 'string') {
    return null;
  } else if (!text.length) {
    return null;
  }
  let r;
  switch (mode) {
    case 'ctr': {
      if (!key) {
        key = '';
      }
      r = (iv) ? decrypt256ctr(text, key, iv) : decrypt256ctr(text, key);
      break;
    }
    case 'cbc': {
      if (!key) {
        key = '';
      }
      r = (iv) ? decrypt256cbc(text, key, iv) : decrypt256cbc(text, key);
      break;
    }
  }
  return r;
}


const AES = {
  decrypt: decrypt,
  encrypt: encrypt
};


function readLines(input, func) {
  var remaining = '';

  input.on('data', function(data) {
    remaining += data;
    var index = remaining.indexOf('\n');
    while (index > -1) {
      var line = remaining.substring(0, index);
      remaining = remaining.substring(index + 1);
      func(line);
      index = remaining.indexOf('\n');
    }
  });

  input.on('end', function() {
    if (remaining.length > 0) {
      func(remaining);
    }
  });
}

var ct1 = `5fbea6826018446a11723163e466fb6be754a170f545d5e94ce4ef1b359c3a4e`;
var pass = "meep";

const qr = `d79967f167cc3ffe65c2e9485ad30c6a045dac87317828b66196550f5bcd66c6fd8a414b281d60fe98bb83bdb474523412121d27d38d75e2ffb5355923d8370a`;
const gpg = `50dcd121d510d6d9ad782721991b9edff2d630722d040e13a525b1b7de02a3e1af4e4e8fcc4181d375c2fa8ebb3dea1d3ab22c36d990c6158d480bcbf6e34c992d5527cdb7454c8a46d346bf159fbb18d0111f7415a158b19acf290a6fc0304c5fae21b022433900cca3336d22862ececd2b6597d0dde4d877caeb80b0ad7c2d516d3efacf79ed7e68105bf4d33210748c1710be127ab9506c331e1af0d3846a93a5943a61a866d4339faa19186b7a6c02dfb1e2624c7a022798fa0e13a3aed7f68e163b1d290d5cc45f0a3b281e623feb3304aa42921ab3794d830910c4f455a0310cd9831016b35778213443fbee6b81d0b7453cd4b39812a5ae19536409f145f05fb25e6408315a4c44acd68320a00403d03049af6c8f962b3a127538a26862b6927174b434f04caa267e88cca72401185181ede8ec6a4d9a0917a95007872912c03b2e2851641c8a9ed060eedc8d9f4d74ad75dcffe2b8e427f017f277d02eb4a81d85acac1c58b50d8ecb134de4dc4cc76a5149645507b6c5bf69bfc87b2860957631d127de4f544d601f29cc0581d09943e8954e2d34353210343e1e9f31293a2cfce359cd6bb9a809fe999f81503ffe04b15d6e039fb07d156c5ff5e181766aeef4d8c69c332510341d913b4275dd60a91dbdefa2e16196f6c0298af6f7c1dba7097fefa5d5f50154e498f41c851dbf7c94d9c6d4fbc59b0bddda7795b006260b63f4d067d12f043b25de466c306feb423c5c428d9e393482ccf1432064ec3b33882442efc6305278fecf6ae584917427dbba2de588e0220f04586cbfad567f5a44245ff180a229562f1b8f2969244212df8464f10a849e36b56dc7fa8eb27c2efbd74daf22f8541c51ad3c88af97623ada30d0c90c091d3bd2b340f6a5b092c383ab6483e9d35d894780dcd74b395ae141cd3a5e76c00fd7a5eb0ca915a1928f8b13623510c50b9092ac9cd2cceaee524424fff1973258ea981958701741cee3e01342abf791a23448f524395114fcbc333dd1fa91bdef5bcbe7153af8b832f3f11644c5238120db20cc1bc12a3fb89a46e35c80643ed944f4eda5cd055f95519fe81a64619dfdefdce58b5d824944b19f0d60052aa763e2b491dc453416bac8c6b5461094a7b5caa1089bc5b20305ee4fbbc00c5af7c91b0cb23acb3bcd504b9e37dfff9905f6d93df50c128b1bc26f630614b60ae39ce009d0eb27daac06de10480484535ed1b7bded7e4690da46b80fa1734e913635816b03e9f61fcc24a2735c08f31305401351a6262d893b9efd1887f56444c2045b72f1ee1575215e8455edb33d4b67bb870a610875f10c9dddd688ca0c9de127d5d23aded8ba395f143ae6027977c43a203b819cac4cc53e7ca493f98c266c5b0045f1f56f7d9c754b18e9a7de80345760c8a5aa716812c1b3ebd83b3c285854577b14709667582c415c5df2b13dcd760c3bf166d830df3966c24942852901013734988187cb04f401eae3fb25b450cb6cdcca735dc5ee88bf1dfc635e8bcf69ea7b49fb9abde3297b19a6d7aa6cd6c3fc5118037bf0c89ed662d27f8a4372778ec26a1be873c50f0a994e962a6707631b93d79b6a1771f999943377a53bdd6dd99d38072427b1c8722ff2b810ea6406b59a922bfd78efbe485cc85af2868f9cccf2c127a61248f0c694b45e78974b55a9a4427c71c31a8abe9b9367590f4b0d62099152e7bfeff023de03dca7d3e97b5164c0d2235537e206b85abc94c0c652820d5d4ac14567bc452eef10f356564a089a04a294c2b82d15587514d21790ed7b7eabdd1b3542681259ba6ea3d7916ed03c4791ee007aa0c1d1e13692a83269cc9a3752832ca34380efd5c472a6522de2c23361433311fa79e567c386a5946d7d3e418f85d963a5279f7476c071d746af3fa8eecf2a8f0b19d7db8c2d5b25ddf482be4fdaf36f36268a5a2fe60ace9a758bd94347a9692d6717ea3c1369e2fe022da2cfe57dc6af258c4ab557c8b394b48ae06b3ad154cee0d634768843596be9be7e48dc531c340fa01bd8f227c3232857e8223b0cc3256ef3109b4869d1ea4aa408842efc8f7f17f1c4d462cbacd352f0b7ff9b9b88453887685ea57e9df872fd5f0f93160ad92f27b99151f28674d1af6672e1c10d1c9c8b78738593eaab97003a8e1c1fe1502c98846d1f8b67d23a2512d6bab525aa1a4903bf4c72457004922fbe9e9c8be9dbcebbaa39115f46caac14bbf32ffce046ff3563300d40b47c7b46b7ac6d9eb2bd8fdf5e656f2eadf0ac1fdd2865af5ff5c20e401a5afda2211debdbfa041b48bc4502ef059c5f6017e9e35d114d799b22d0aaf0154fd29abdafce638074e48c4a0c2961ac466739c206f35e72e8ac5ac060d22d2aaa42438428757379d14ca56a5c5c6ce59a7887054d028b28ad7c49376e60b49610ebc9eeb8015446fca837eb709304f3a01802f7797a8ff31ed0b920da6a55e1cc68ea60ce681b42463dd2f3ac8297a24274521adeb700d263c30ace7b615eb999f77b36edf67b62b85cd5077927013a0d09bd5d5d39e184467ce4bec05d79eba49ec72fe3bfb88d64950f8ef2efa653943124367e33ab8c289641d49cc447b0de313121b065ef3c885041f5262b8a7afb5bc9832a7d23240a0f02085512e462640c9f4bd04c0625f95e90bfae7d1eb0758bbb6a877702a4f7f3eafe145177df4480f4783bfe8dd78edcd8d92811338d2da17ebda3d88ea444024839da45adfd4eb748138623526cc3358b29b2b893c10b6838cd2fd5d774f1872b1b8d7ebe4a2f57825a8de97b73a4846e5c807ed49f8886a8ff831d4d88953004621931722d26380787ae7451726738f1bb953534c71e1a6149b024d875c0040afd1ba1338239023ea2f4a77440adc89ae9d354917659bb108cbb3fde2580ee1196fb12ecf178edfc2f0acc1250d35435f8bdf8ce3fe159541a5d1ea78fd8acdbef27c95174a64e7be4e31b6dd6f769a475558abc9c7dad13e93f7a2c0bcb62bb2ee4e27f12351f509c1aa0c1f511f46e7bde8a06f0d3cddb9339cb31cfd152c10982f93e5987f46ed1826784ca1567149e0926c6f2989acf58186476fef973409fff294f001b8a55f2afd4272f20b23fdf384da4ee7852f16102ff06e1`;

console.log(qr.length);
console.log(gpg.length);

var ldec = AES.decrypt('cbc', ct1, pass);
console.log('Test: ' + ldec);


function func(data) {
  //console.log('Trying: ' + data);
  //data = data.toUpperCase();
  try {
    ldec = AES.decrypt('cbc', qr, data);
    console.log(ldec);
  } catch {
  }
  try {
    ldec = AES.decrypt('cbc', gpg, data);
    console.log(ldec);
  } catch {
  }
}
var input = fs.createReadStream('wordlist.txt');
//var input = fs.createReadStream('/usr/share/dict/words');
readLines(input, func);


