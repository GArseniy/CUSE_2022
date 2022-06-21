#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    fstream fin;
    fin.open("fileB.txt");
    int n;
    fin >> n;
    int A[n];
    for (int i = 0; i < n; ++i)
    {
        fin >> A[i];
    }
    int min_pref[10];
    min_pref[0] = 0;
    for (int i = 1; i < 10; ++i)
    {
        min_pref[i] = 1000000000;
    }
    int s = 0;
    int ans = 0;
    for (int i = 0; i < n; ++i)
    {
        s += A[i];
        int t = s % 10;
        if ((s - min_pref[t]) > ans)
        {
            ans = s - min_pref[t];
        }
        if (s < min_pref[t])
        {
            min_pref[t] = s;
        }
    }
    cout << ans;
    return 0;
}
