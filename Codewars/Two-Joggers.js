var nbrOfLaps = function (x, y) {
  let count = x;
  while (count % y !== 0) {
    count += x;
  }
  return [count/x, count/y];
}

// Other solution
function gcd(a, b) {
  if(b == 0)
    return a;
  return gcd(b, a % b);
}

var nbrOfLaps = function (x, y) {
  var lcm = (x*y)/ gcd(x,y);
  return [lcm/x, lcm/y];
}
