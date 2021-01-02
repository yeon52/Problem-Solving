#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXLEN 100

typedef struct { /* 하나의 단어와 그 단어의 빈도수를 저장하기 위한 구조체 */

	char *word;
	int freq;

} Item;
struct node { /* 연결리스트의 노드의 구조를 정의하는 구조체 */

	Item *data;
	struct node *next;

};
typedef struct node Node;
Node *insert(Node *, char buf[]);
int main()
{
	char buf[MAXLEN];
	Node *head = NULL; /* head는 지역변수이다. */
	while (1) {
		scanf("%s", buf);
		if (strcmp(buf, "EOF") == 0) break; /* 문자열 “EOF”를 입력하면 종료 */
		head = insert(head, buf); /* 입력된 문자열을 연결리스트에 반영 */
	}
	Node *p = head;

	while (p != NULL) {
		printf("%s:%d\n", p->data->word, p->data->freq);
		p = p->next;
	}
	return 0;
}
Node *insert(Node *head, char buf[]) {

	Node *p = head;
	int chk = 0;
	if (p == NULL)
	{
		Node *tmp = (Node*)malloc(sizeof(Node));
		tmp->data = (Item*)malloc(sizeof(Item) * 10);
		tmp->data->word = strdup(buf);
		tmp->data->freq = 1;
		tmp->next = NULL;
		p = tmp;
		return p;
	}
	while (p != NULL)
	{
		if (strcmp(p->data->word, buf) == 0)
		{
			p->data->freq++;
			return head;
		}
		p = p->next;
	}
	p = head;
	Node *q = p->next;
	if (strcmp(p->data->word, buf) > 0)
	{
		Node *tmp = (Node*)malloc(sizeof(Node));
		tmp->data = (Item*)malloc(sizeof(Item) * 10);
		tmp->data->word = strdup(buf);
		tmp->data->freq = 1;
		tmp->next = p;
		p = tmp;
		return p;
	}
	while (q != NULL)
	{
		if (strcmp(q->data->word, buf) > 0)
		{
			Node *tmp = (Node*)malloc(sizeof(Node));
			tmp->data = (Item*)malloc(sizeof(Item) * 10);
			tmp->data->word = strdup(buf);
			tmp->data->freq = 1;
			p->next = tmp;
			tmp->next = q;
			chk = 1;
			return head;
		}
		p = p->next;
		q = q->next;
	}
	if (p != NULL && chk == 0)
	{
		Node *tmp = (Node*)malloc(sizeof(Node));
		tmp->data = (Item*)malloc(sizeof(Item) * 10);
		tmp->data->word = strdup(buf);
		tmp->data->freq = 1;
		tmp->next = NULL;
		p->next = tmp;
	}
	return head;
}