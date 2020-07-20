// Select color input
// Select size input

var colorPicker = document.getElementById('colorPicker');
var rowsCount = document.getElementById('inputHeight');
var cellsCount = document.getElementById('inputWidth');
var pixelCanvas = document.getElementById('pixelCanvas');
var form = document.getElementById('sizePicker');


// When size is submitted by the user, call makeGrid()
form.addEventListener('submit', function(horse) {
  pixelCanvas.innerHTML='';
  horse.preventDefault();
  makeGrid();
});

pixelCanvas.addEventListener('click', function (horse){
  if (horse.target.nodeName === 'TD') {
    horse.target.style.backgroundColor = colorPicker.value;
  }
})

function makeGrid() {

for (let i = 0; i < rowsCount.value; i++) {
  const row=pixelCanvas.insertRow(0);
  for (let j =0 ; j < cellsCount.value; j++) {
    row.insertCell(0);
  }
}

}
