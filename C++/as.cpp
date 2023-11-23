#include <iostream>
#include <conio.h>
#include <iostream>
using namespace std;

int main()
{
    int x = 2;
    int y = 20;
    int z = 11;
    int ans;
    cout << solve(x, y, z);
    return 0;
}

int solve(int a, int b, int m)
{
    if (b == 0)
    {
        return 1;
    }
    else if (b % 2 == 0)
    {
        return solve((a * a) % m, b / 2, m);
    }
    else if (b % 2 != 0)
    {
        return ((a % m) * solve((a * a) % m, (b - 1) / 2, m)) % m;
    }
}
