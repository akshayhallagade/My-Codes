void main() {
  var student1 = student();
  student1.id = 1;
  student1.name = "peter";
  print("The class having the ${student1.id} and ${student1.name}.");
}

class student {
  int id = -1;
  String name;

  void study() {}

  void sleep() {}
}
