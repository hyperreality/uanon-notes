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

var ct1 = `82c92f1fe13a1a9586f1c9758ed9fb2a3a046d99db7cca3e4240840e62e2716033a08ccfee81aad0994bf650e0e6a4e9`;
var ct2 = `5967f41e14fb5d1c8c6d65152932014d065d03637d6979e235fdf35f32a0f557f01189f43608b63258ef302e09092381`;
var ct3 = `b54a5215b7c4be6cbb9b2fcf87ed07220c539caafc6a76eeb64eef0526beef49e3c967a2e47f444c81989b0c4990a859dcc10d63989b8d8d84294330db002d106af673069d00b330a6e386d8665cb96096c79082bf4f2de639787150f2beec5641a4cde2b81aa9c47c375d79b8a213fe9035c969b19459bcaa22203514149810e0fd0bdeecbaa08105af6ed51f1d570901722844301eaa83911213a1280896103623dd72c5053f656b7087b9c5718269c042b45256936b17f84192986a1f57ceb45c584b4397506b7035a81911d16eca2e7485adeb5d76b92a8355079e4ec06931101744259f614b43f9fa8ea64a46eb61ca27888af277f3cc94841f3a4db67e19ea5697e959ec24cdc2798c86f2c6511caf966dc9224c36a5a972ffe40cf11641ced7174cf6f5950ac4e6e93fabc6f682330e2610b1d976a48e9fc4d47cb7f0fa8502eb219b481f628ee3b980fdbd8475610a3e7c4f7c4b9a07414d9b5ef14d4a41a7772fd4db98151f6c042c7733dab3dfd63aac9ef985d0d4b14cc8b1cd308d6582deaf5ade9e1026fd9f0049f3662e4784391dd6a20460859c8a7fb67629e2d77f644411fa8d633bfa182ec21c5b2ba58abac6fd336f0dcd323393df13a74fa4e3e619091c19cf6503e69c9afe07997e954bd784c053ab7a3cb7b6393828b31a56af2fc9c892e982099069a9bb2f2f20a4e8a2c6e5c8ffd4f98cdfa0c58a4eafe2ec384a0b01d0d64734fc452f8e504cd041f5c32091116bdc181e083cc3ea795efdd201c80e1bb537b38718a20cdc018cf35f2e698eca276ae0594c60d194bb6ed0e5908fbb8606e939c597866a1cd7de557ad18cf9aff53211017babf86fc4472a366190fb47d34f28220d8a99ae0512e651380d45a5a8b89dcb235fa919a78da7378620bce4e6324d46a50c04b931de171441674869fc9f81f2e537cf6c9512505f88f78c1eb213801926d347bb54e28db834fe8fa89f52c3e41b91586d125201b1777c393e491a50b74996bd475220897194976d9d1450e37204016a0a03c116a85eac008ac93c7fef7a9dc9e7a2574e322d6948701f77172f6c06a41b163d7d85a277d6af05f980135795b3bdb5ba5e30e64d4dd610573725b5af29e54a8947a7d15afd58a3e48e787b95e93be5aed134c4c440f4490f748c070a9eba4071079c1a6254df1958c8b7475980bfe96187989203cedb391f1c7a7c86f0d2b00893ba9393c819eaf8c9fb312f11388a820e18178eb0c2adedd7fc0a137ba918adde47e43308847bb332f807f9bfe16c8e80e2d2af98c8f6b44ac1c688eb694a296b565eeeda5a692d8ebf3ec43d5196f5b2c236ba8b96063ac9f75ee49c48bd909d1b28ef9efb47dcefd987ee400df79192dc39fd06e31ae2edacbd0c860332a555586014f0b5d18ff2a458093a2186d655b0c9b4b4fea5a1fbb85e59af9a4e4662d40a810c287a457c80d09dfd2eb69da40423f852e67bbc6dcf9446a86df1fa35b8312ce136a20d86d40ff770467bd0012d39aa65954fffc146ad14e6178567c30a1518a5ce9f9016be07e40943fd4e939d55a0f4c0eb894a0f86ecd95218ebb242946c34b27b2a05e84998d3747e2e349773e93c8fd7976a08a3197f279371cfa127484704e02f2d2a3ff9a75850223a7b408d5feac6b337d2ffa61191fa280f1e9487e858ca64f50f6aa97a1bc13eedb92e7ad2588869917bf157f6a1f89710e66558523881b3d8e82d9c63f4560e9cde4d1613fbec2e5d75f38bdf5f162d5983946fff65a65369f68d9c4219b16ead523a992a6116342c024fb6dee68fff8ec8d3d016609f7aae64328aa09d193b1854a2eb0c2d9ef6a331df9e6179d93ca9ce4f2a4aafa7ca84431729c21f121e9c00007789803d9193e99631ff47979e9e25b56fa98e32977f6f1122079b04789c54654bab7718eea21524e6de0a4cf9e7d9c9cd8626f4b35f659f6e83c91d3ca0225de99c0c8a6a5a28cd1c39c3ec69017f81be1cf16c7a84970ab2fdd05479ca605093c17a3257d0c2af3b3215313c84656698d23706000e8ed8cca0`;

function func(data) {
  //console.log('Trying: ' + data);
  //data = data.toLowerCase();
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
var input = fs.createReadStream('wordlist2.txt');
// var input = fs.createReadStream('/home/abc/Downloads/uanon/uanon-notes/season1/spring7/greek_brute/el_romanized.txt');
//var input = fs.createReadStream('/home/abc/Downloads/uanon/uanon-notes/season1/spring7/greek_brute/words_romanized.txt');
//var input = fs.createReadStream('/home/abc/Downloads/uanon/uanon-notes/season1/spring7/greek_brute/words_freq.greek');
//var input = fs.createReadStream('latin-words.txt');

readLines(input, func);


