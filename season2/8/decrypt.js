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

var ct1 = `b74d2823b8b5da4ee7f69ca02e55ce509d5a71d434683248f9594e1e754096f324dc3ec61048463fdc1054a1d5adcc15`;

function func(data) {
  //console.log('Trying: ' + data);
  //data = data.toLowerCase();
  try {
    data = "ACCESS" + data.toUpperCase();
    ldec = AES.decrypt('cbc', ct1, data);
    console.log(data)
    console.log(ldec);
  } catch {
  }
}
//var input = fs.createReadStream('wordlist.txt');
var input = fs.createReadStream('/usr/share/dict/words');

readLines(input, func);

