#include <stdio.h>
#include <string.h>

int compare(char *str1_, char *str2_);
int main()
{
	char str1[50], str2[50];
	scanf("%s %s", str1, str2);
	if (compare(str1, str2) == -1 || compare(str2, str1) == 0)
		printf("%s %s", str2, str1);
	else if (compare(str1, str2) == 1)
		printf("%s %s", str1, str2);
	else
	  printf("Error");
	return 0;
}
int compare(char *str1_, char *str2_)
{
	int i = 0;
	int Max_len;
	char *str1, *str2;
	str1 = strdup(str1_);
	str2 = strdup(str2_);

	if (str1[0] == '\0' && str1[0] != '\0')
		return -1;
	else if (str1[0] != '\0' && str1[0] == '\0')
		return 1;
	else if (str1[0] == '\0' && str1[0] == '\0')
		return 0;
	else if (str1[0] > str2[0])
		return -1;
	else if (str1[0] < str2[0])
		return 1;
	else if(str1[0] == str2[0])
	{
		for (int i = 0; i < strlen(str1); i++)
			str1[i] = str1[i + 1];
		for (int i = 0; i < strlen(str2); i++)
			str2[i] = str2[i + 1];
		return compare(str1, str2);
	}
	return 2;
}