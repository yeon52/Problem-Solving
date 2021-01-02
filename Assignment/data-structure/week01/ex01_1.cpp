#include <stdio.h>

void sort_abc(int *a, int *b, int *c);
int main()
{
    int a, b, c;
    scanf("%d%d%d", &a, &b, &c);
    sort_abc(&a, &b, &c);
    printf("%d %d %d\n", a, b, c);
}
void sort_abc(int *a, int *b, int *c)
{
	int tmp;
  for (int i = 0; i < 3; i++)
	{
		if (*b < *a)
		{
			tmp = *a;
			*a = *b;
			*b = tmp;
		}
		if (*c < *b)
		{
			tmp = *b;
			*b = *c;
			*c = tmp;
		}
		if (*c < *a)
		{
			tmp = *c;
			*c = *a;
			*a = tmp;
		}
	}
}