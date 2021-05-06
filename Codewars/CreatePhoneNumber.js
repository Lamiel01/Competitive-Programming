function createPhoneNumber(numbers){
  if (numbers.length != 10){
    return -1;
  }
    let first = `(${numbers[0]}${numbers[1]}${numbers[2]})`;
    let second = ` ${numbers[3]}${numbers[4]}${numbers[5]}`;
    let third = `-${numbers[6]}${numbers[7]}${numbers[8]}${numbers[9]}`;
    return first + second + third;
}

// Other solutions
function createPhoneNumber(numbers){
  var format = "(xxx) xxx-xxxx";
  
  for(var i = 0; i < numbers.length; i++)
  {
    format = format.replace('x', numbers[i]);
  }
  
  return format;
}
