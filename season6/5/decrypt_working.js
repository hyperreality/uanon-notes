const crypto = require('crypto');
const fs = require('fs');

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

var ct1 = `d62926101a27f69250673b04e115a736ea5ac71fbc8129ef2c20536b6cb73272d1326a14c9127730`;
var ct2 = `2435f9b6c5d33b2df628cac97408f28970601658d3f98b16bcfd7a4ae91712b8e302a95c7b319595`;
var ct3 = `5081c8b724046343910080c639a9415cdb0591c9e44c5256e0124cadef223c2e3cc7240182b34951`;
var ct4 = `27a070de99e5d9157ff1a7183924e6362e289832568e814359f6f13369903ce0da056fe4fc082d11`;

function func(data) {
  // data = data.substring(0,4);
  // console.log('Trying: ' + data);
  // data = Buffer.from(data, "hex");
  try {
    ldec = AES.decrypt('cbc', ct1, data);
    console.log(data)
    console.log(ldec);
  } catch {
  }
  try {
    ldec = AES.decrypt('cbc', ct2, data);
    console.log(data)
    console.log(ldec);
  } catch {
  }
  try {
    ldec = AES.decrypt('cbc', ct3, data);
    console.log(data)
    console.log(ldec);
  } catch {
  }
}
var input = fs.createReadStream('wordlist4.txt');

readLines(input, func);


