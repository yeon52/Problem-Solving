#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define MAX_POLYS 100

struct term {
	int coef;
	int exp_x, exp_y;
	struct term *next;
};
typedef struct term Term;

typedef struct polynomial {
	char name;
	Term *first;
	int size;
} Polynomial;

Polynomial *polys[MAX_POLYS];
int n = 0;
Term *create_term_instance();
Polynomial *create_polynomial_instance(char name);
Polynomial *create_by_parse_polynomial(char name, char *body);
Polynomial *create_by_add_two_polynomials(char name, char f, char g);
int parse_and_add_term(char *expr, int begin, int end, Polynomial *p_poly);
void add_term(int c, int e, Polynomial *poly);
int eval(Polynomial *poly, int x, int y);
int eval_(Term *term, int x, int y);
void print_poly(Polynomial *p);
void print_term(Term *pTerm);
void handle_definition(char *expression);
void insert_polynomial(Polynomial *ptr_poly);
void destroy_polynomial(Polynomial *ptr_poly);
int main()
{
	char order[10], buf[100], f_name, num1, num2;
	while (1)
	{
		scanf("%s", order);
		if (strcmp(order, "def") == 0)
		{
			fgets(buf, sizeof(buf), stdin);
			handle_definition(buf);
		}
		else if (strcmp(order, "calc") == 0)
		{
			scanf("%c %d %d", &f_name, &num1, &num2);

			for (int i = 0; i < n; i++)
			{
				if (polys[i]->name == f_name)
				{
					printf("%d", eval(polys[i], num1, num2));
					return;
				}
			}
		}
		else if (strcmp(order, "print") == 0)
		{
			scanf("%c", &f_name);
			for (int i = 0; i < n; i++)
			{
				if (polys[i]->name == f_name)
				{
					print_poly(polys[i]);
					return;
				}
			}
		}
		else if (strcmp(order, "list") == 0)
		{
			for (int i = 0; i < n; i++)
			{
				print_poly(polys[i]);
			}
		}
		else if (strcmp(order, "exit") == 0)
			break;
	}
	return 0;
}
Term *create_term_instance()
{
	Term *t = (Term*)malloc(sizeof(Term));
	t->coef = 0;
	t->exp_x = 0;
	t->exp_y = 0;
	t->next = NULL;
	return t;
}
Polynomial *create_polynomial_instance(char name)
{
	Polynomial *ptr_poly = (Polynomial *)malloc(sizeof(Polynomial));
	ptr_poly->name = name;
	ptr_poly->size = 0;
	ptr_poly->first = NULL;
	n++;
	return ptr_poly;
}
void add_term(int c, int e_x, int e_y, Polynomial *poly)
{
	if (c == 0)
		return;
	Term *p = poly->first, *q = NULL;
	while (p != NULL && p->exp_x > e_x)
	{
		q = p;
		p = p->next;
	}
	if (p != NULL && p->exp_x == e_x)
	{
		while (p != NULL && p->exp_y > e_y)
		{
			q = p;
			p = p->next;
		}
		p->coef += c;
		if (p->coef == 0)
		{
			if (q == NULL)
				poly->first = p->next;
			else
				q->next = p->next;
			poly->size--;
			free(p);
		}
		return;
	}
	Term *term = create_term_instance();
	term->coef = c;
	term->exp_x = e_x;
	term->exp_y = e_y;

	if (q == NULL)
	{
		term->next = poly->first;
		poly->first = term;
	}
	else
	{
		term->next = p;
		q->next = term;
	}
	poly->size++;
}
Polynomial *create_by_parse_polynomial(char name, char *body)
{
	Polynomial *ptr_poly = create_polynomial_instance(name);
	int i = 0, begin_term = 0;
	while (i < strlen(body))
	{
		if (body[i] == '+' || body[i] == '-')
			i++;
		while (i < strlen(body) && body[i] != '+'&&body[i] != '-')
			i++;
		int result = parse_and_add_term(body, begin_term, i, ptr_poly);
		if (result == 0)
		{
			destroy_polynomial(ptr_poly);
			return NULL;
		}
		begin_term = i;
	}
	return ptr_poly;
}
int parse_and_add_term(char *expr, int begin, int end, Polynomial *p_poly)
{
	int i = begin;
	int sign_coef = 1, coef = 0, expo_x = 1, expo_y = 1;
	if (expr[i] == '+')
		i++;
	else if (expr[i] == '-')
	{
		sign_coef = -1;
		i++;
	}
	while (i < end&&expr[i] >= 0 && expr[i] <= 9)
	{
		coef = coef * 10 + (int)(expr[i] - '0');
		i++;
	}
	if (coef == 0)
		coef = sign_coef;
	else
		coef *= sign_coef;

	if (i >= end) 
	{
		add_term(coef, 0, 0, p_poly);
		return 1;
	}
	i++;
	if (i >= end)
	{
		if(expr[i]=='x')
			add_term(coef, 1, 0, p_poly);
		else if(expr[i]=='y')
			add_term(coef, 0, 1, p_poly);
		return 1;
	}
	i++;
	if (expr[i] == '^')
	{
		i++;
		expo_x = 0;
		while (i < end&&expr[i] >= '0' && expr[i] <= '9')
		{
			expo_x = expo_x * 10 + (int)(expr[i] - '0');
			i++;
		}
		i++;
		if (i >= end)
			expo_y = 0;
		else
		{
			i++;
			if (i >= end)
				expo_y = 1;
			else
			{
				expo_y = 0;
				while (i < end&&expr[i] >= '0' && expr[i] <= '9')
				{
					expo_y = expo_y * 10 + (int)(expr[i] - '0');
					i++;
				}
			}
		}
	}
	else if (expr[i] == 'y')
	{
		i++;
		if (i >= end)
			add_term(coef, 1, 1, p_poly);
		i++;
		expo_y = 0;
		while (i < end&&expr[i] >= '0' && expr[i] <= '9')
		{
			expo_y = expo_y * 10 + (int)(expr[i] - '0');
			i++;
		}
	}
	add_term(coef, expo_x, expo_y, p_poly);
	return 1;
}
int eval(Polynomial *poly, int x, int y)
{
	int result = 0;
	Term *t = poly->first;
	while (t != NULL)
	{
		result += eval_(t, x, y);
		t = t->next;
	}
	return result;
}
int eval_(Term *term, int x, int y)
{
	int result = term->coef;
	for (int i = 0; i < term->exp_x; i++)
		result *= x;
	for (int i = 0; i < term->exp_y; i++)
		result *= y;
	return result;
}
void print_poly(Polynomial *p)
{
	printf("%c=", p->name);
	Term *t = p->first;
	while (t != NULL)
	{
		print_term(t);
		printf("+");
		t = t->next;
	}
}
void print_term(Term *pTerm)
{
	printf("%dx^%dy^%d", pTerm->coef, pTerm->exp_x, pTerm->exp_y);
}
void handle_definition(char *expression)
{
	char *f_name = strtok(expression, "=");
	char *exp_body = strtok(NULL, "=");
	if (exp_body[0] >= 'a'&&exp_body[0] <= 'z'&&exp_body[0] != 'x')
	{
		char *former = strtok(exp_body, "+");
		char *later = strtok(NULL, "+");
		Polynomial *pol = create_by_add_two_polynomials(f_name[0], former[0], later[0]);
		insert_polynomial(pol);
	}
	else
	{
		Polynomial *pol = create_by_parse_polynomial(f_name[0], exp_body);
		insert_polynomial(pol);
	}
}
void insert_polynomial(Polynomial *ptr_poly)
{
	for (int i = 0; i < n; i++)
	{
		if (polys[i]->name == ptr_poly->name)
		{
			destroy_polynomial(polys[i]);
			polys[i] = ptr_poly;
			return;
		}
	}
	polys[n++] = ptr_poly;
}
void destroy_polynomial(Polynomial *ptr_poly)
{
	if (ptr_poly == NULL)
		return;
	Term *t = ptr_poly->first, *tmp;
	while (t != NULL)
	{
		tmp = t;
		t = t->next;
		free(tmp);
	}
	free(ptr_poly);
}
Polynomial *create_by_add_two_polynomials(char name, char f, char g)
{
	Polynomial *ptr_poly = create_polynomial_instance(name);
	Polynomial *p = (Polynomial*)malloc(sizeof(Polynomial));
	Polynomial *q = (Polynomial*)malloc(sizeof(Polynomial));
	Term *t = ptr_poly->first;
	for (int i = 0; i < n; i++)
	{
		if (polys[i]->name == f)
			p = polys[i];
	}
	while (p != NULL)
	{
		t->coef = p->first->coef;
		t->exp_x = p->first->exp_x;
		t->exp_y = p->first->exp_y;
		t = t->next;
	}
	for (int i = 0; i < n; i++)
	{
		if (polys[i]->name == g)
			q = polys[i];
	}
	while (q != NULL)
	{
		t->coef = p->first->coef;
		t->exp_x = p->first->exp_x;
		t->exp_y = p->first->exp_y;
		t = t->next;
	}
	return ptr_poly;
}