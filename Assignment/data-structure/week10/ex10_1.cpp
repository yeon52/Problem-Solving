#include <stdio.h>
#include <stdbool.h>
#include <string.h>

bool is_palindrome(char *str);
int main()
{
	char str[50];
	scanf("%s", str);
	if (is_palindrome(str) == 1)
		printf("Yes");
	else
		printf("No");
	return 0;
}
bool is_palindrome(char *str)
{
	if (str[0] != str[strlen(str) - 1])
		return false;
	else if (strlen(str) == 1)
		return true;
	else if (str[0] == str[strlen(str) - 1])
	{
		for (int i = 0; i < strlen(str); i++)
			str[i] = str[i + 1];
		str[strlen(str) - 1] = '\0';
		return is_palindrome(str);
	}
	return true;
}