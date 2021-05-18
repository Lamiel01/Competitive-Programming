function solution(str){
  var result = str.split(/(..)/).filter(function (el) {
  return el != false;
});
  return str.length % 2 == 0 ? result : (result + '_').split(",")
}
