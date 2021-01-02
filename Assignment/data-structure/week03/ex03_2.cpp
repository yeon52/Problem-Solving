#include <stdio.h>

int main()
{
	char arr[1000], tok[100], index[100];
	int i = 0, j=0, cnt=1;
	fgets(arr, sizeof(arr),stdin);
	while (arr[i] != '\0')
	{
		if (arr[i] == '\"')
		{
			i++;
			while (arr[i] != '\"')
				i++;
			i++;
			continue;
		}
		if (arr[i] == ',')
			cnt++;
		i++;
	}
	printf("%d\n", cnt);
	i = 0;
	while (arr[i] != '\0')
	{
		if (arr[i] == '\"')
		{
			int k = i + 1;
			while (arr[k] != '\"')
			{
				printf("%c", arr[k]);
				k++;
			}
			i = k + 1;
		}
		if (arr[i] == ',')
		{
			printf("\n");
			i++;
			continue;
		}
		printf("%c", arr[i++]);
	}
	return 0;
}