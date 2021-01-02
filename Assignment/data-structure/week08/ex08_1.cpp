#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INIT_CAPACITY 100

struct stack_type {
	char *contents[INIT_CAPACITY];
	int top;
	int size;
	char *name;
};
typedef struct stack_type *Stack;
Stack stack[INIT_CAPACITY];

Stack push(Stack s, char i[]);
char *pop(Stack s);
Stack find_stack(char ch[], int index);
Stack create(int index, char name[]);

int main()
{
	char order[10], s_name[10], input[100];
	int index = 0;
	while (1)
	{
	  printf("$ ");
		scanf("%s", order);
		if (strcmp(order, "create") == 0)
		{
			scanf("%s", s_name);
			stack[index] = create(index, s_name);
			index++;
		}
		else if (strcmp(order, "push") == 0)
		{
			scanf("%s %s", s_name, input);
			push(find_stack(s_name, index), input);
		}
		else if (strcmp(order, "pop") == 0)
		{
			scanf("%s", s_name);
			printf("%s", pop(find_stack(s_name, index)));
		}
		else if (strcmp(order, "list") == 0)
		{
			scanf("%s", s_name);
			for (int i = find_stack(s_name, index)->size-1; i >= 0; i--)
			{
				printf("%s\n", find_stack(s_name, index)->contents[i]);
			}
		}
		else if (strcmp(order, "exit") == 0)
			return 0;
	}
	return 0;
}

Stack create(int index, char name[])
{
	Stack s = (Stack)malloc(sizeof(struct stack_type));
	s->contents[0] = (char*)malloc(INIT_CAPACITY * sizeof(char));
	s->top = -1;
	s->size = 0;
	s->name = strdup(name);
	return s;
}

Stack push(Stack s, char i[])
{
	s->top++;
	s->contents[s->top] = strdup(i);
	s->size++;
	return s;
}
char* pop(Stack s)
{
	s->top--;
	s->size--;
	return s->contents[s->top + 1];
}

Stack find_stack(char s_name[], int index)
{
	for (int i = 0; i < index; i++)
	{
		if (strcmp(stack[i]->name, s_name) == 0)
			return stack[i];
	}
	return 0;
}