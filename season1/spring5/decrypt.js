const crypto = require('crypto');

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

const l = `75f10a9d5b9d64c9cc92a1b853438cbf8a686cf9163ba9bf54d155c5579b28cf023e2200fe4556435027141243c9d6354a13e03b80b8794c05c7e66e4f531368ea9e076c717d1e1e99d96250842d8cbb`;
const m = `58e382f2f77dab3c4275effbf4b7cc38523d0878155be11b43b5b9720fd4d793ca94384b30486b175b1debc21a9ece8d29d0363200449745ddcd9e1a3ef7e08450ea64d6110835782bef42f770316d357367f7d524041a315534fac029f374473a44b0ee347f99f0fd35ea185bca93a80e263487f0dcd6b4e7c53d69d46c68c528a6ea8890882b1e62e9598be01eda4008e5f9208d5c829596e942cdd4ba495a75d9866bf20cc823299c01f91cd0060d`;

const proof = "7e83d05c30be582797c6801842bdcaaa3e365daf36148f269ef89ed907e911d1";

const ldec = AES.decrypt('cbc', l, proof);
console.log(ldec);
const mdec = AES.decrypt('cbc', m, proof);
console.log(mdec);
