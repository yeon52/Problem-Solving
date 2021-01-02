#include <stdio.h>
#include <string.h>

int main() 
{
	char arr[1000], *csv[100];
	int i = 0;
	fgets(arr, sizeof(arr),stdin);

	csv[i] = strtok(arr, ",");
	while (csv[i]!=NULL)
	{
		i++;
		csv[i] = strtok(NULL, ",");
	}
	printf("%d\n", i);
	for (int j = 0; j < i; j++)
	{
		printf("%s\n", csv[j]);
	}
		
}