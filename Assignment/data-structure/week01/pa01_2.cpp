#pragma warning (disable : 4996)
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
char *strdup(char *s);

int main(void)
{
	int n, m, i, j;
	char buf[20];
	char *str[10][10];
	
	scanf("%d %d", &m, &n);

	for (i = 0; i < m; i++)
	{
		for (j = 0; j < n; j++)
		{
			scanf("%s", buf);
			str[i][j] = strdup(buf);
		}
	}
	for (int p = 0; p < n-1; p++)
	{
		int max = strlen(str[0][p]);
		for (int q = 0; q < m; q++)
		{
			if (max < strlen(str[q][p]))
				max = strlen(str[q][p]);
		}
		for (int r = 0; r < m; r++)
		{
			int length = (max - strlen(str[r][p]));
			for (int v = 0; v < length; v++)
				strcat(str[r][p], " ");
		}
	}

	for (int p = 0; p < m; p++)
	{
		for (int q = 0; q < n-1; q++)
		{
			printf("%s ", str[p][q]);
		}
		printf("%s\n",str[p][n-1]);
	}
	return 0;
}
char *strdup(char *s)
{
	char *p;
	p = (char *)malloc(strlen(s) + 1);
	if (p != NULL)
		strcpy(p, s);
	return p;
}
