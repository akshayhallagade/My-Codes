void main() {
  var num1 = 101;
  var num2 = 2;
  var res = 0;
  var resfordev = 0.0;
  //created for the division value. beacause value we are getting is double.
  res = num1 + num2;
  print("Addition: ${res}");
  res = num1 - num2;
  print("Subtraction: ${res}");
  res = num1 * num2;
  print("Multiplication: ${res}");
  resfordev = num1 / num2;
  print("Division: ${resfordev}"); //Here, Resfordev is used.
  res = num1 ~/ num2;
  print("Divident: ${res}");
  res = num1 % num2;
  print("Remainder: ${res}");
  num1++;
  print("Increment: ${num1}");
  num2--;
  print("Decrement: ${num2}");
}
