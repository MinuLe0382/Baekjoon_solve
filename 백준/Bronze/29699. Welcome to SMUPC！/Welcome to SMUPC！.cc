#include <iostream>
#include <string>

int main() {
    std::string temp = "WelcomeToSMUPC";
    int N = 0;
    const int length = 14;
    std::cin >> N;

    std::cout << temp[(N - 1) % length];

    return 0;
}