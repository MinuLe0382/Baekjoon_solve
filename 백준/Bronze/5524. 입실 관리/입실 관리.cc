#include <iostream>
#include <string>

int main()
{
    int T = 0;
    std::cin >> T;
    for (int i = 0; i < T; i++)
    {
        std::string name;
        std::cin >> name;
        for (char &ch : name)
        {
            if ('A' <= ch and 'Z' >= ch)
                ch = ch + ('a' - 'A');   
        }
        std::cout << name << std::endl;
    }

    return 0;
}