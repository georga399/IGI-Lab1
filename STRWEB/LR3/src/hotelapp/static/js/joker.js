document.getElementById('styleToggle').addEventListener('change', function() {
  const styleControls = document.getElementById('styleControls');
  styleControls.style.display = this.checked ? 'block' : 'none';
});

document.getElementById('fontSize').addEventListener('change', function() {
  document.body.style.fontSize = this.value;
});

document.getElementById('textColor').addEventListener('input', function() {
  document.body.style.color = this.value;
});

document.getElementById('bgColor').addEventListener('input', function() {
  document.body.style.backgroundColor = this.value;
});

