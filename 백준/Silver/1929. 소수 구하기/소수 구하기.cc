#include <iostream>
#include <cmath>
#include <vector>

int main()
{
    int N, M = 0;
    std::cin >> M >> N;
    std::vector<int> checker(N + 1, 0);
    for (int k = 0; k < N + 1; k++)
        checker[k] = k;
    checker[1] = 0;
    for (int i = 2; i <= int(pow(N, 0.5)); i++)
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
            std::cout << checker[i] << std::endl;
    }

    return 0;
}