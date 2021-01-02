#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

typedef struct {
	int coef;
	int expo_x, expo_y;
} Term;

Term *recognize(char arr[]);
int main()
{
	char expr[30];
	int coef, exp_x, exp_y;
	scanf("%s", expr);
	Term *t = recognize(expr);
	printf("%d %d %d\n", t->coef, t->expo_x, t->expo_y);
	return 0;
}
Term *recognize(char arr[])
{
	Term *t = (Term*)malloc(sizeof(Term));
	int i = 0;
	int sign_coef = 1, coef = 0, expo_x = 0, expo_y=0;
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
		t->expo_x = 0;
		t->expo_y = 0;
		return t;
	}
	else
	{
		i++;
		if (i >= end)
		{
			if (arr[i-1] == 'x')
			{
				t->coef = coef;
				t->expo_x = 1;
				t->expo_y = 0;
				return t;
			}
			else if (arr[i-1] == 'y')
			{
				t->coef = coef;
				t->expo_x = 0;
				t->expo_y = 1;
				return t;
			}
		}
		if (arr[i-1] == 'x')
		{
			i++;
			if (arr[i-1] == 'y')
			{
				i++;
				if (i >= end)
				{
					t->coef = coef;
					t->expo_x = 1;
					t->expo_y = 1;
					return t;
				}
				else
				{
					while (i < end && arr[i] >= '0' && arr[i] <= '9')
					{
						expo_y = expo_y * 10 + (int)(arr[i] - '0');
						i++;
					}
					t->coef = coef;
					t->expo_x = 1;
					t->expo_y = expo_y;
					return t;
				}
			}
			else
			{
				while (i < end && arr[i] >= '0' && arr[i] <= '9')
				{
					expo_x = expo_x * 10 + (int)(arr[i] - '0');
					i++;
				}
			}
			if (i >= end)
			{
				t->coef = coef;
				t->expo_x = expo_x;
				t->expo_y = 0;
				return t;
			}
			else
			{
				i++;
				if (i >= end)
				{
					t->coef = coef;
					t->expo_x = expo_x;
					t->expo_y = 1;
					return t;
				}
				else
				{
					i++;
					while (i < end && arr[i] >= '0' && arr[i] <= '9')
					{
						expo_y = expo_y * 10 + (int)(arr[i] - '0');
						i++;
					}
				}
			}
		}
		else if (arr[i-1] == 'y')
		{
			i++;
			while (i < end && arr[i] >= '0' && arr[i] <= '9')
			{
				expo_y = expo_y * 10 + (int)(arr[i] - '0');
				i++;
			}
		}
		t->coef = coef;
		t->expo_x = expo_x;
		t->expo_y = expo_y;
		return t;
	}
}
