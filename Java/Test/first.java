public class first {
    static boolean printChar(char c) {
        System.out.print(c);
        return true;
    }

    public static void main(String[] argv) {
        int i = 0;
        for (printChar('A'); printChar('B') && (i < 2); printChar('C')) {
            i++;
            printChar('D');
        }
    }
}