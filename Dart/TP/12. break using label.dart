void main() {
  myparticularloop:
  for (int i = 1; i <= 3; i++) {
    for (int j = 1; j <= 3; j++) {
      print("$i, $j");
      if (i & j == 2) {
        break myparticularloop;
      }
    }
  }
}
