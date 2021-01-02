#include <stdio.h>
#include <string.h>

int isanagram(char *a, char *b);
int main()
{
	char input[100][20], *anagram[20][20];
	int i = 0, p = 0, q = 0, n=0, chk = 0, index[1000], cnt_q[1000],x=0, order[100], t=0;
	while (1)
	{
		scanf("%s", input[i]);

		if (strcmp(input[i], "EOF")==0)
			break;
		i++;
	}
	for (int j = 0; j < i; j++)
	{
		for (int m = 0; m < n; m++)
		{
			if (j == index[m])
			{
				chk = 1;
				break;
			}
		}
		if (chk == 0)
			anagram[p][q++] = input[j];
		else
		{
			chk = 0;
			continue;
		}
		for (int k = j + 1; k < i; k++)
		{
			if (isanagram(input[j], input[k]) == 1)
			{
				index[n++] = k;
				anagram[p][q++] = input[k];
			}
		}
		cnt_q[x++] = q;
		p++;
		q = 0;
		chk = 0;
	}
	x = 0;
	
	char *tmp;
	for (int j = 0; j < p; j++)
	{
		int z = cnt_q[x];
		while (z>0)
		{
			for (int i = 0; i < z - 1; i++)
			{
				if (strcmp(anagram[j][i], anagram[j][i+1]) > 0)
				{
					tmp = strdup(anagram[j][i]);
					anagram[j][i] = strdup(anagram[j][i+1]);
					anagram[j][i+1] = strdup(tmp);
				}
			}
			z--;
		}
		x++;
	}

	for (int j = 0; j < p; j++)
		order[j] = j;
	
	int temp, z = p;
	
	while (z > 0)
	{
		for (int i = 0; i < z - 1; i++)
		{
			if (strcmp(anagram[order[i]][0], anagram[order[i + 1]][0]) > 0)
			{
				temp = order[i];
				order[i] = order[i + 1];
				order[i + 1] = temp;

				temp = cnt_q[i];
				cnt_q[i] = cnt_q[i + 1];
				cnt_q[i + 1] = temp;
			}
		}
		z--;
	}

	x = 0;
	for (int j = 0; j < p; j++)
	{
		for (int k = 0; k < cnt_q[x]; k++)
		{
			printf("%s ", anagram[order[j]][k]);
		}
		x++;
		printf("\n");
	}
	return 0;
}
int isanagram(char *a, char *b)
{
	int cnt_a[26] = { 0 }, cnt_b[26] = { 0 };

	for (int i = 0; i < strlen(a); i++)
		cnt_a[a[i] - 97]++;
	for (int i = 0; i < strlen(b); i++)
		cnt_b[b[i] - 97]++;

	for (int i = 0; i < 26; i++)
	{
		if (cnt_a[i] != cnt_b[i])
			return 0;
	}
	return 1;
}
