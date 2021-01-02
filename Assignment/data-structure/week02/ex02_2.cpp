#include <stdio.h>
#include <string.h>

int isnum(char a);
int main() 
{
	char word[100];
	scanf("%s", word);
	int length = strlen(word), sum[100] = {0}, k=0, cnt=0, sum_all=0;
	
	for (int i = 0; i < length; i++)
	{
		if ((isnum(word[i]) == 1)&&(isnum(word[i+1]) == 1))
		{
			cnt++;
			sum[k++] = word[i]-48;
			
		}
		int cnt_ = cnt;
		if ((isnum(word[i]) == 1) && (isnum(word[i + 1]) == 0))
		{
			sum[k++] = word[i] - 48;
			for (int i = 0; i < cnt_ + 1; i++)
			{
				for (int j = 0; j < cnt; j++)
				{
					sum[i] *= 10;
				}
				cnt--;
			}
			for (int i = 0; i < cnt_+1; i++)
				sum_all += sum[i];
			sum[i] = { 0 };
			cnt = 0;
			k = 0;
		}
	}
	printf("%d", sum_all);
	return 0;
}
int isnum(char a)
{
	if (a >= 48 && a <= 57)
		return 1;
	return 0;
}