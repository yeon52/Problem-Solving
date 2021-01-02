#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

typedef struct {
	int coef;
	int expo;
} Term;

Term *recognize(char arr[]);
int main()
{
	char expr[30];
	scanf("%s", expr);
	Term *t = recognize(expr);
	printf("%d %d\n", t->coef, t->expo);
	return 0;
}
Term *recognize(char arr[])
{
	Term *t = (Term*)malloc(sizeof(Term));
	int i = 0;
	int sign_coef = 1, coef = 0, expo = 0;
	int end = strlen(arr);
	if (arr[0] == '-')
	{
		sign_coef = -1;
		i++;
	}
	while (i < end && arr[i] >= '0'&& arr[i] <= '9')
	{
		coef = coef * 10 + (int)(arr[i] - '0');
		i++;
	}
	if (coef == 0)
		coef = sign_coef;
	else
		coef *= sign_coef;
	if (i >= end)
	{
		t->coef = coef;
		t->expo = 0;
		return t;
	}
	else
	{
		i++;
		if (i >= end)
		{
			t->coef = coef;
			t->expo = 1;
			return t;
		}
		i++;
		while (i < end && arr[i] >= '0' && arr[i] <= '9')
		{
			expo = expo * 10 + (int)(arr[i] - '0');
			i++;
		}
		t->coef = coef;
		t->expo = expo;
		return t;
	}
}
