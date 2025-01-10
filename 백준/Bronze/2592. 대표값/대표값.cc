#include <iostream>
int main()
{
    int bindo[100] = { 0 };
    int cur = 0;
    int summation = 0;
    int binmax = 0;
    int max = 0;
    for (int i = 0; i < 10; i++)
    {    
        std::cin >> cur;
        summation += cur;
        cur = cur / 10;
        bindo[cur] += 1;
        if (bindo[cur] > binmax)
        {
            binmax = bindo[cur];
            max = cur;
        }  
    }
    std::cout << summation / 10 << std::endl;
    std::cout << max * 10 << std::endl;

    return 0;
}   