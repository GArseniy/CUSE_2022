#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    fstream fin;
    fin.open("27.txt");
    int n;
    fin >> n;
    int c_n;
    int s = 0;
    int min_pref_3[3];
    min_pref_3[0] = 0;
    int ans = 0;
    int t;
    for (int i = 1; i<3; ++i)
    {
        min_pref_3[i] = 100000;
    }
    for (int i = 0; i < n; ++i)
    {
        fin >> c_n;
        s += c_n;
        t = s % 3;
        if (ans < (s - min_pref_3[t]))
        {
            ans = s - min_pref_3[t];
        }
        if (min_pref_3[t] > s)
        {
            min_pref_3[t] = s;
        }
    }
    cout << ans;
    return 0;
}