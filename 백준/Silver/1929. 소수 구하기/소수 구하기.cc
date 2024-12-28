#include <iostream>
#define MAX 1000000
#include <cmath>
int checker[MAX + 1] = { 0, };

int main()
{
    int N, M = 0;
    std::cin >> M >> N;
    
    for (int k = 2; k < N + 1; k++)
        checker[k] = k;

    for (int i = 2; i * i <= N; i++)
    {
        if (checker[i] != 0)
        {
            for (int j = i * i; j < N + 1; j += i)
                checker[j] = 0;
        }
    }

    for (int i = M; i < N + 1; i++)
    {
        if (checker[i] != 0)
            std::cout << checker[i] << '\n';
    }

    return 0;
}