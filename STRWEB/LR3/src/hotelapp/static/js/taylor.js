function mathF(x) {
  return Math.asin(x);
}

function taylor(x, n) {
  let y = x;
  let i = 0;
  let prev = x;
  for (1 = 1; i < n; i++) {
    prev *= (x * x * (2 * i - 1) * 2 * i) / (4 * i * i * (2 * i + 1));
    y += prev;             
  }
  return y;
}

