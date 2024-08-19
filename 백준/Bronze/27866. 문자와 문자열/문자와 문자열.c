#include<stdio.h>

int main()
{
    char input_word[1001] = { 0 };
    int target_index = 0;
    gets(input_word);
    scanf("%d", &target_index);
    
    printf("%c", input_word[target_index - 1]);
    return 0;
}