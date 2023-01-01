const number_of_rows = 200;
const number_of_columns = 200;

let grid_array = [];
let percentChance = 0.5;
let cell_size = 10;
let started = false;

function setup() {
  createCanvas(600, 400);
  background('#000000');
  stroke(200);
  frameRate(10);

  // border
  noFill(); rect(0,0, width-1, height-1);

  for (let j = 0; j < number_of_rows; j += 1) {
    for (let i = 0; i < number_of_columns; i += 1) {
      let index = i + (j * number_of_columns);
      grid_array[index] = 0;
      if (random() < percentChance) {
        grid_array[index] = 1;
      }
    }
  }
}

function draw() {
  if (!started) return;
  // draw grid
  for (let j = 0; j < number_of_rows; j += 1) {
    for (let i = 0; i < number_of_columns; i += 1) {
      let index = i + (j * number_of_columns);
      let cell_value = grid_array[index];
      fill((1-cell_value) * 255);
      rect(i*cell_size, j*cell_size, cell_size, cell_size);
    }
  }
  let grid_array_2 = [];
  for (let j = 0; j < number_of_rows; j += 1) {
    for (let i = 0; i < number_of_columns; i += 1) {
      let index = i + (j * number_of_columns);
      grid_array_2[index] = 0;
    }
  }
  for (let j = 0; j < number_of_rows; j += 1) {
    for (let i = 0; i < number_of_columns; i += 1) {
      let neighbours = 0;
      for (let y = -1; y <= 1; y += 1) {
        for (let x = -1; x <= 1; x += 1) {
          let wrapped_i = (i + x + number_of_rows) % number_of_rows;
          let wrapped_j = (j + y + number_of_columns) % number_of_columns;
          if (!(x == 0 && y == 0)) {
            let index = (wrapped_i) + (wrapped_j * number_of_columns);
            neighbours += grid_array[index];
          }
        }
      }
      let index = i + (j * number_of_columns);
      if (grid_array[index] == 1 && neighbours < 2) {
        grid_array_2[index] = 0;
      }
      if (grid_array[index] == 1 && (neighbours == 2 || neighbours == 3)) {
        grid_array_2[index] = 1;
      }
      if (grid_array[index] == 1 && neighbours > 3) {
        grid_array_2[index] = 0;
      }
      if (grid_array[index] == 0 && neighbours == 3) {
        grid_array_2[index] = 1;
      }
    }
  }
  grid_array = grid_array_2;
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