#include <iostream>

int main()
{
    int current = 0;
    int max = 0;
    int rider, taker;

    for (int i = 0; i < 10; i++)
    {
        std::cin >> taker >> rider;
        current = current - taker + rider;
        if (max < current)
            max = current;
    }
    
    std::cout << max;

    return 0;
}