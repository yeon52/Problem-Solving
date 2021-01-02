#pragma warning (disable : 4996)
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX 70000
char *strdup(char *s);
int isalpha(char a);
int isupper(char a);
char tolower(char a);
int main(void)
{
	char buf[20];
	char *words[MAX];
	char *tmp;
	int number[MAX] = { 0 };
	int cnt = 0, k = 0;
	FILE *fp = fopen("pride_and_prejudice.txt", "r");
	while (fscanf(fp, "%s", buf) != EOF)
	{
		int length = strlen(buf);
		if (length < 7)
			continue;

		for (int i = 0; i < length; i++)
		{
			if (isalpha(buf[0]) == 0)
			{
				for (int i = 0; i < length; i++)
					buf[i] = buf[i + 1];
				buf[length - 1] = '\0';
				length--;
			}
			if (isalpha(buf[length - 1]) == 0)
			{
				buf[length - 1] = '\0';
				length--;
			}
		}
		for (int i = 0; i < length; i++)
		{
			if (isupper(buf[i]) != 0)
				buf[i] = tolower(buf[i]);
		}
		int chk = 0;
		for (int i = 0; i < k; i++)
		{
			if (strcmp(words[i], buf) == 0)
			{
				number[i]++;
				chk = 1;
				cnt = 0;
				break;
			}
		}
		if (chk == 0 && length >= 7)
		{
			words[k++] = strdup(buf);
			cnt = 0;
		}
	}
	int j = k;
	while (j>0)
	{
		for (int i = 0; i < j - 1; i++)
		{
			if (strcmp(words[i], words[i + 1]) > 0)
			{
				tmp = strdup(words[i]);
				words[i] = strdup(words[i + 1]);
				words[i + 1] = strdup(tmp);

				int tmp2 = number[i];
				number[i] = number[i + 1];
				number[i + 1] = tmp2;
			}
		}
		j--;
	}
	for (int i = 0; i < k; i += 10)
		printf("%s %d\n", words[i], number[i] + 1);

	fclose(fp);
	return 0;
}
int isalpha(char a)
{
	if ((a >= 65 && a <= 90) || (a >= 97 && a <= 122))
		return 1;
	return 0;
}
int isupper(char a)
{
	if (a >= 65 && a <= 90)
		return 1;
	return 0;
}
char tolower(char a)
{
	return a + 32;
}
char *strdup(char *s)
{
	char *p;
	p = (char *)malloc(strlen(s) + 1);
	if (p != NULL)
		strcpy(p, s);
	return p;
}