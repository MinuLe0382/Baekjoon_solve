#include <iostream>
#include <string>
int main()
{   
    std::string number;
    while (true)
    {   
        bool flag = true;
        std::cin >> number;
        if (number == "0")
            break;
        else
            for (size_t i = 0; i < size(number); i++)
            {
                if (number[i] != number[int(size(number) - i - 1)])
                {
                    flag = false;
                    std::cout << "no" << '\n';
                    break;
                }
            }
            if (flag)
                std::cout << "yes" << '\n';
    }

    return 0;
}