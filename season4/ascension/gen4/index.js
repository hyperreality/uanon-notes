let w;
let optimize = true;
let active = 1;
let timerMax = 1;
let timer = timerMax;
let dx = 1;
let dy = 0;
let started = false;

function setup() {
  createCanvas(600, 400);
  colorMode(HSB);
  rectMode(CENTER);
  //if (!started) return; // <- Crash Safety; Remove this line to run program at your own risk
  w = new UnknownObject1(
      Number("012345680124368001246385021468020124356701243571012435760123465701234568012463850123465802146802012436850124357601234657012436850124638001246385021468020124357"),
      600, 
      0, 
      0
    );
}

function draw() {
  if (!started) return;
  background(0);
  translate(width / 2, height / 2);
  if (active == 1) {
    if (timer == 0) {
      w.step();
      timer = timerMax;
    }
    timer--;
  }
  w.show();
}

class UnknownObject1 {
  constructor(res, scl, x, y) {
    this.res = res;
    this.size = scl;
    this.scl = scl / res;

    this.board = [];
    this.setup(res);

    this.x = x - scl / 2;
    this.y = y - scl / 2;
  }
  setup(res) {
    this.res = res;
    for (let y = 0; y < this.res; y++) {
      this.board[y] = [];
      for (let x = 0; x < this.res; x++) {
        this.board[y][x] = new Cell(0);
      }
    }
    this.board[round(res - 1)][round(res / 2 - 1)].state = 1;
    this.board[round(res - 2)][round(res / 2)].state = 1;
    this.board[round(res - 1)][round(res / 2)].state = 1;
    this.board[round(res - 2)][round(res / 2 - 1)].state = 1;
  }

  show() {
    push();
    noStroke();
    fill(50);
    rect(0, 0, this.scl * this.res, this.scl * this.res);
    fill(0);
    rect(0, 0, this.scl * this.res, this.scl * this.res);
    pop();
    for (let y = 0; y < this.res; y++) {
      for (let x = 0; x < this.res; x++) {
        this.board[y][x].setData(x, y, this.x, this.y, this.scl);
        this.board[y][x].show();
      }
    }
  }
  step() {
    for (let y = 0; y < this.res; y++) {
      for (let x = 0; x < this.res; x++) {
        this.neighbors(x, y);
      }
    }
    for (let y = 0; y < this.res; y++) {
      for (let x = 0; x < this.res; x++) {
        this.board[y][x].setState();
      }
    }
  }
  neighbors(x, y) {
    let population = 0;
    let s = 1;
    for (let k = -s; k <= s; k++) {
      for (let j = -s; j <= s; j++) {
        let index = findIndex(x + j, y + k, this.res, this.res);
        if ((j == 0) & (k == 0)) {
        } else {
          if (this.board[index[1]][index[0]].state == 1) {
            population += 1;
          }
        }
      }
    }
    if (optimize) {
      if (population == 0) {
        this.board[y][x].tempState = this.board[y][x].state;
        return;
      }
    }
    let index = findIndex(x + dx, y + dy, this.res, this.res);
    if (this.board[index[1]][index[0]].state == 1) {
      this.board[y][x].tempState = 1;
    } else {
      if (this.board[y][x].state == 1) {
        if (population < 2) {
          this.board[y][x].tempState = 0;
        } else if (population >= 2 && population <= 3) {
          this.board[y][x].tempState = 1;
        } else if (population > 3) {
          this.board[y][x].tempState = 0;
        }
      } else {
        if (population == 3) {
          this.board[y][x].tempState = 1;
        }
      }
    }
  }
}

class Cell {
  constructor(state) {
    this.state = state;
    this.tempState = state;

    this.x = 0;
    this.y = 0;
    this.ox = 0;
    this.oy = 0;
    this.scl = 0;
  }
  setData(x, y, ox, oy, scl) {
    this.x = x;
    this.y = y;
    this.ox = ox;
    this.oy = oy;
    this.scl = scl;
  }
  show() {
    if (this.state == 1) {
      let b = 0.9;
      push();
      noStroke();
      fill(0, 0, 0, 1);
      rect(
        (this.x + 0.5) * this.scl + this.ox,
        (this.y + 0.5) * this.scl + this.oy,
        this.scl,
        this.scl
      );
      let t = map(this.state, 0, 1, 16, 100);
      fill(0, 0, t, 1);
      rect(
        (this.x + 0.5) * this.scl + this.ox,
        (this.y + 0.5) * this.scl + this.oy,
        this.scl * b,
        this.scl * b
      );
      pop();
    }
  }
  setState() {
    this.state = this.tempState;
  }
}

function findIndex(x, y, width, height) {
  let xpos = x % width;
  let ypos = y % height;
  if (xpos < 0) {
    xpos = width - abs(xpos);
  }
  if (ypos < 0) {
    ypos = height - abs(ypos);
  }
  return [xpos, ypos];
}

function onOff() {
  started = !started;
  const stop = document.getElementById('stop');
  const execute = document.getElementById('execute');
  if (!started) {
    execute.classList.remove('hidden');
    stop.classList.add('hidden');
  } else {
    stop.classList.remove('hidden');
    execute.classList.add('hidden');
  }
}
