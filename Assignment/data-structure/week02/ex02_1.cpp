#include <stdio.h>
#include <string.h>

int main() {
	char words[20];
	char tmp;
  
	scanf("%s", words);
	int j = strlen(words);
	while (j > 0)
	{
		for (int i = 0; i < j - 1; i++)
		{
			if (words[i]> words[i + 1])
			{
				tmp = words[i];
				words[i] = words[i + 1];
				words[i + 1] = tmp;
			}
		}
		j--;
	}

	for (int i = 0; i < strlen(words); i++)
		printf("%c", words[i]);
	return 0;
}