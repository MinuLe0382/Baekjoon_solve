#include <iostream>
#include <string>

int main() {
    std::string result;
    std::string line;
    int line_count = 0;
    int alphabet[26] = { 0, };

    while (line_count < 50 && std::getline(std::cin, line)) {
        if (!line.empty()) {
            result += line + " "; // 줄을 추가하고 줄바꿈 포함
        }
        line_count++;
    }

    for (char ch : result)
    {
        if (ch == ' ')
            continue;
        else
            alphabet[ch - 'a']++;
    }
    
    int max = 0;
    for (int i = 0; i < 26; i++)
    {
        if (max < alphabet[i])
            max = alphabet[i];
    }
    for (int i = 0; i < 26; i++)
    {
        if (max == alphabet[i])
            std::cout << (char)(i + 'a');
    }

    return 0;
}