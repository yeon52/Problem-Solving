#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
	int N;
	char *name[100], *singer[100], arr[100][200], *number[100], name_[100][100], singer_[100][100];
	int number_[100];
	scanf("%d", &N);
	getchar();
	for (int i = 0; i < N; i++)
		fgets(arr[i], sizeof(arr[i]), stdin);
	for (int i = 0; i < N; i++)
	{
		name[i] = strtok(arr[i], "-");
		singer[i] = strtok(NULL, "-");
		number[i] = strtok(NULL, " #.");
	}
	for (int i = 0; i < N; i++)
	{
		strcpy(name_[i], name[i]);
		name_[i][strlen(name_[i]) - 1] = '\0';
		strcpy(singer_[i], singer[i]);
		number_[i] = atoi(number[i]);
	}
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < strlen(singer_[i])-1; j++)
			singer_[i][j] = singer_[i][j + 1];
		singer[i][strlen(singer_[i]) - 1] = '\0';
	}
		
	int j = N, temp=0;
	char tmp[100];
	while (j > 0)
	{
		for (int i = 0; i < j - 1; i++)
		{
			if (number_[i]>number_[i+1])
			{
				strcpy(tmp, name_[i]);
				strcpy(name_[i] ,name_[i + 1]);
				strcpy(name_[i + 1], tmp);

				strcpy(tmp ,singer_[i]);
				strcpy(singer_[i],singer_[i + 1]);
				strcpy(singer_[i + 1], tmp);

				temp = number_[i];
				number_[i] = number_[i + 1];
				number_[i + 1] = temp;
			}
		}
		j--;
	}
	for (int i = 0; i < N; i++)
		printf("%02d-%s-%s.mp3\n", i+1, name_[i], singer_[i]);
	return 0;
}