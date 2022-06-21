#include <iostream>
#include <fstream>


using namespace std;


int main()
{
    ifstream fin;
    fin.open("File_B__mctk.txt");

    int n;
    fin >> n;
    int A[n];
    for (int i = 0; i < n; ++i)
    {
        fin >> A[i];
    }
    //**********************************************
    int MaxSum = -100000;
    int k = 3;
    for (int i = 0; i<n; ++i)
    {
        int sum = A[i];
        if ((sum % k == 0) and (sum > MaxSum))
        {
            MaxSum = sum;
        }
        for (int j = i+1; j < n; ++j)
        {
            sum += A[j];
            if ((sum % k == 0) and (sum > MaxSum))
            {
                MaxSum = sum;
            }
        }
    }
    cout << MaxSum << endl;
    //**********************************************
    return 0;
}
