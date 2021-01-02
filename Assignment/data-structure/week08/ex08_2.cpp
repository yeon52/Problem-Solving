#include <stdio.h>
#include <string.h>

#define MAX_LENGTH 100
char stack[MAX_LENGTH];
int top = -1;
int is_open(char ch);
int is_paren(char ch);
void push(char ch);
char pop();
int main()
{
	char expr[MAX_LENGTH], ch;
	scanf("%s", expr);
	int cnt_open = 0, cnt_close;
	for (int i = 0; i < strlen(expr); i++)
	{
		if (is_paren(expr[i]) == 1)
		{
			ch = expr[i];
		}
		else
			continue;
		if (is_open(ch) == 1)
		{
			cnt_open++;
			push(cnt_open);
			printf("%d", cnt_open);
		}
		else if (is_open(ch) != 1)
		{
			printf("%d",pop());
		}
	}
	return 0;
}
int is_open(char ch)
{
	if (ch == '(')
		return 1;
	else
		return 0;
}
void push(char ch)
{
	top++;
	stack[top] = ch;
}
char pop()
{
	char tmp = stack[top];
	top--;
	return tmp;
}
int is_paren(char ch)
{
	if (ch == '(' || ch == ')')
		return 1;
	else
		return 0;
}