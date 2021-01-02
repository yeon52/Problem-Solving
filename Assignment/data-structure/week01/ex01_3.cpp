#include <stdio.h>
#include <stdlib.h>

void sort(int *p, int n);

int main(void)
{
	int *p = (int *)malloc(400);;
	int N;
	scanf("%d", &N);
	for (int i = 0; i < N; i++)
		scanf("%d", (p + i));
	sort(p,N);
	for (int i = 0; i < N; i++)
		printf("%d\n", *(p + i));
	return 0;
}
void sort(int *p, int n)
{
	int tmp;
	while (n > 0)
	{
		for (int i = 0; i < n-1 ; i++)
		{
			if (*(p + i) > *(p + (i + 1)))
			{
				tmp = *(p + i);
				*(p + i) = *(p + (i + 1));
				*(p + (i + 1)) = tmp;
			}
		}
		n--;
	}
}