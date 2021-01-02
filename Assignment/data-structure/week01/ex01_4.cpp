#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

char *strdup(char *s);
char tolower(char c);
int isupper(char c);
int main() 
{
	char word[100][20], input[20], *dif[100];
	int i = 0, cnt = 0, chk = 0;
	while (1)
	{
		scanf("%s", input);
		if (strcmp(input, "EOF") == 0)
			break;
		strcpy(word[i++],input);
	}
	for (int j = 0; j < i; j++)
	{
		for (int k = 0; k < strlen(word[j]); k++)
		{
			if (isupper(word[j][k]) == 1)
				word[j][k] = tolower(word[j][k]);
		}
	}
	dif[0] = strdup(word[0]);
	int n = 1;
	for (int j = 0; j < i; j++)
	{
		chk = 0;
		for (int k = 0; k < n; k++)
		{
			if (strcmp(dif[k], word[j]) == 0)
			{
				chk = 1;
				continue;
			}
		}
		if (chk == 0)
			dif[n++] = word[j];
	}
	printf("%d", n);
}
char *strdup(char *s)
{
	char *p;
	p = (char *)malloc(strlen(s) + 1);
	if (p != NULL)
		strcpy(p, s);
	return p;
}
char tolower(char c)
{
	return c + 32;
}
int isupper(char c)
{
	if (c >= 65 && c <= 90)
		return 1;
	return 0;
}