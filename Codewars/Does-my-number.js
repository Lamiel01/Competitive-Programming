function narcissistic(value) {
  // Code me to return true or false
  let sum = 0;
  let number = String(value);
  for (let i = 0; i < number.length; i++) {
    sum += number[i] ** number.length;
  }
  return sum == value;
}
