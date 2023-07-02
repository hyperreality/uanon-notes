function iChing() {
  let one = Math.random() >= 0.5;
  let two = Math.random() >= 0.5;
  let three = Math.random() >= 0.5;
  let rand = false;
  if (one == two && two == three) {
    rand = true;
  }
  return rand;
}

function b64ToUtf8(b64String) {
  if (!window | typeof b64String !== 'string') return null;
  return window.atob(b64String);
}

export {
  b64ToUtf8,
  iChing
};