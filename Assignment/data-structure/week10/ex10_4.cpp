#include <stdio.h>
#include <string.h>

int is_floor(int data[], int cur);
int is_ceiling(int data[], int cur);
int K,N;
int main()
{
	int data[100];
	scanf("%d", &N);
	int cur_f = N - 1, cur_c = 0;
	for (int i = 0; i < N; i++)
		scanf("%d", &data[i]);
	scanf("%d", &K);
	printf("%d %d", is_floor(data, cur_f), is_ceiling(data, cur_c));
	return 0;
}
int is_floor(int data[], int cur)
{
	if (cur == 0)
		return -1;

	if (data[cur] >= K)
	{
		cur--;
		return is_floor(data, cur);
	}
	else if (data[cur] < K)
	{
		return data[cur];
	}
	return 0;
}
int is_ceiling(int data[], int cur)
{
	if (cur == N)
		return -1;

	if (data[cur] <= K)
	{
		cur++;
		return is_ceiling(data, cur);
	}
	else if (data[cur] > K)
	{
		return data[cur];
	}
	return 0;
}