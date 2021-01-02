#pragma warning (disable:4996)
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define MAX 1500
int isdate(int date[], int month[], int year[]);
int change_month(char month[]);
int array_date(int date, int month, int year, int date2, int month2, int year2);
int array_time(int hour, int minute, int second, int hour2, int minute2, int second2);
char *strdup(char *s);
int main()
{
	char arr[MAX][200], order[10], option[10], *ip[MAX], *time[MAX], *url[MAX], *status[MAX], input_ip[20], input_date[2][20], *year_[3], *month_[3], *date_[3], *ip_array[100];
	int compare_date[3], compare_month[3], compare_year[3], ip_cnt[100] = { 0 }, ip_all_cnt = 0;
	char *time2[100], *url2[100], *status2[100], *hour[MAX], *minute[MAX], *second[MAX], *hour2[100], *minute2[100], *second2[100];
	int i = 0, q = 0, r = 0, date2_int[100], month2_int[100], year2_int[100], hour2_int[100], minute2_int[100], second2_int[100];
	char *time_[MAX], *year[MAX], *month[MAX], *date[MAX], *date2[100], *month2[100], *year2[100], *ip2[100];
	FILE *fp = fopen("webLog.csv", "r");

	fgets(arr[i], sizeof(arr[i]), fp);
	i = 0;
	while (!feof(fp))
	{
		fgets(arr[i], sizeof(arr[i]), fp);
		i++;
	}
	i--;
	fclose(fp);
	ip[0] = strtok(arr[0], ",");
	time[0] = strtok(NULL, ",[]");
	url[0] = strtok(NULL, ",");
	status[0] = strtok(NULL, ",");

	for (int n = 1; n<i; n++)
	{
		ip[n] = strtok(arr[n], ",");
		time[n] = strtok(NULL, ",[]");
		url[n] = strtok(NULL, ",");
		status[n] = strtok(NULL, ",");
	}
	for (int j = 0; j < i; j++)
		time_[j] = strdup(time[j]);

	for (int j = 0; j < i; j++)
	{
		date[j] = strtok(time[j], "/");
		month[j] = strtok(NULL, "/");
		year[j] = strtok(NULL, ":");
		hour[j] = strtok(NULL, ":");
		minute[j] = strtok(NULL, ":");
		second[j] = strtok(NULL, ":");
	}

	while (1)
	{
		printf("$");
		scanf("%s", order);
		if (strcmp(order, "exit") == 0)
			return 0;

		if (strcmp(order, "search") == 0)
		{
			scanf("%s", option);
			if (strcmp(option, "-date") == 0)
			{
				scanf("%s %s", input_date[0], input_date[1]);

				date_[0] = strtok(input_date[0], "/");
				month_[0] = strtok(NULL, "/");
				year_[0] = strtok(NULL, "/");

				date_[1] = strtok(input_date[1], "/");
				month_[1] = strtok(NULL, "/");
				year_[1] = strtok(NULL, "/");

				for (int j = 0; j < i; j++)
				{
					date_[2] = strdup(date[j]);
					month_[2] = strdup(month[j]);
					year_[2] = strdup(year[j]);

					for (int k = 0; k < 3; k++)
					{
						compare_date[k] = atoi(date_[k]);
						compare_month[k] = change_month(month_[k]);
						compare_year[k] = atoi(year_[k]);
					}
					int chk = 0;
					if (isdate(compare_date, compare_month, compare_year) == 1)
					{
						for (int p = 0; p < q; p++)
						{
							if (strcmp(ip[j], ip_array[p]) == 0)
							{
								ip_cnt[p]++;
								chk = 1;
							}
						}
						if (chk == 0)
						{
							ip_array[q++] = strdup(ip[j]);
							ip_all_cnt++;
						}
					}
				}
				int z = q;
				char *temp = NULL;
				while (z > 0)
				{
					for (int j = 0; j < z - 1; j++)
					{
						if (ip_cnt[j] < ip_cnt[j + 1])
						{
							temp = strdup(ip_array[j]);
							ip_array[j] = strdup(ip_array[j + 1]);
							ip_array[j + 1] = strdup(temp);

							int tmp = ip_cnt[j];
							ip_cnt[j] = ip_cnt[j + 1];
							ip_cnt[j + 1] = tmp;
						}
						else if (ip_cnt[j] == ip_cnt[j + 1])
						{
							if (strcmp(ip_array[j], ip_array[j + 1]) > 0)
							{
								temp = strdup(ip_array[j]);
								ip_array[j] = strdup(ip_array[j + 1]);
								ip_array[j + 1] = strdup(temp);
							}
						}
					}
					z--;
				}
				printf(" %d ips found:\n", ip_all_cnt);
				for (int p = 0; p < q; p++)
					printf("   %s: %d\n", ip_array[p], ip_cnt[p] + 1);
			}

			else if (strcmp(option, "-ip") == 0)
			{
				scanf("%s", input_ip);
				for (int j = 0; j < i; j++)
				{
					if (strcmp(input_ip, ip[j]) == 0)
					{
						ip2[r] = strdup(ip[j]);
						time2[r] = strdup(time_[j]);
						url2[r] = strdup(url[j]);
						status2[r] = strdup(status[j]);
						hour2[r] = strdup(hour[j]);
						minute2[r] = strdup(minute[j]);
						second2[r] = strdup(second[j]);
						date2[r] = strdup(date[j]);
						month2[r] = strdup(month[j]);
						year2[r] = strdup(year[j]);
						r++;
					}
				}
				for (int j = 0; j < r; j++)
				{
					date2_int[j] = atoi(date2[j]);
					month2_int[j] = change_month(month2[j]);
					year2_int[j] = atoi(year2[j]);
					hour2_int[j] = atoi(hour2[j]);
					minute2_int[j] = atoi(minute2[j]);
					second2_int[j] = atoi(second2[j]);
				}
				int z = r, tmp = 0;
				char *temp = NULL;
				while (z > 0)
				{
					for (int j = 0; j < z - 1; j++)
					{
						if (array_date(date2_int[j], month2_int[j], year2_int[j], date2_int[j + 1], month2_int[j + 1], year2_int[j + 1]) == 1)
						{
							temp = strdup(ip2[j]);
							ip2[j] = strdup(ip2[j + 1]);
							ip2[j + 1] = strdup(temp);

							temp = strdup(time2[j]);
							time2[j] = strdup(time2[j + 1]);
							time2[j + 1] = strdup(temp);

							temp = strdup(url2[j]);
							url2[j] = strdup(url2[j + 1]);
							url2[j + 1] = strdup(temp);

							temp = strdup(status2[j]);
							status2[j] = strdup(status2[j + 1]);
							status2[j + 1] = strdup(temp);

							tmp = date2_int[j];
							date2_int[j] = date2_int[j + 1];
							date2_int[j + 1] = tmp;

							tmp = month2_int[j];
							month2_int[j] = month2_int[j + 1];
							month2_int[j + 1] = tmp;

							tmp = year2_int[j];
							year2_int[j] = year2_int[j + 1];
							year2_int[j + 1] = tmp;

							tmp = hour2_int[j];
							hour2_int[j] = hour2_int[j + 1];
							hour2_int[j + 1] = tmp;

							tmp = minute2_int[j];
							minute2_int[j] = minute2_int[j + 1];
							minute2_int[j + 1] = tmp;

							tmp = second2_int[j];
							second2_int[j] = second2_int[j + 1];
							second2_int[j + 1] = tmp;
						}
						else if (array_date(date2_int[j], month2_int[j], year2_int[j], date2_int[j + 1], month2_int[j + 1], year2_int[j + 1]) == 2) //날짜가 같은경우 시분초
						{
							if (array_time(hour2_int[j], minute2_int[j], second2_int[j], hour2_int[j + 1], minute2_int[j + 1], second2_int[j + 1]) == 1)
							{
								temp = strdup(ip2[j]);
								ip2[j] = strdup(ip2[j + 1]);
								ip2[j + 1] = strdup(temp);

								temp = strdup(time2[j]);
								time2[j] = strdup(time2[j + 1]);
								time2[j + 1] = strdup(temp);

								temp = strdup(url2[j]);
								url2[j] = strdup(url2[j + 1]);
								url2[j + 1] = strdup(temp);

								temp = strdup(status2[j]);
								status2[j] = strdup(status2[j + 1]);
								status2[j + 1] = strdup(temp);

								tmp = date2_int[j];
								date2_int[j] = date2_int[j + 1];
								date2_int[j + 1] = tmp;

								tmp = month2_int[j];
								month2_int[j] = month2_int[j + 1];
								month2_int[j + 1] = tmp;

								tmp = year2_int[j];
								year2_int[j] = year2_int[j + 1];
								year2_int[j + 1] = tmp;

								tmp = hour2_int[j];
								hour2_int[j] = hour2_int[j + 1];
								hour2_int[j + 1] = tmp;

								tmp = minute2_int[j];
								minute2_int[j] = minute2_int[j + 1];
								minute2_int[j + 1] = tmp;

								tmp = second2_int[j];
								second2_int[j] = second2_int[j + 1];
								second2_int[j + 1] = tmp;
							}
						}
					}
					z--;
				}
				printf(" %d logs found\n", r);
				for (int j = 0; j < r; j++)
					printf("   [%s],%s,%s", time2[j], url2[j], status2[j]);
			}

		}
	}
}

int isdate(int date[], int month[], int year[])
{
	if (year[2] > year[0] && year[2] < year[1])
		return 1;
	else if ((year[2] == year[0]) && (year[2] < year[1]))
	{
		if (month[2] > month[0])
			return 1;
		else if ((month[2] == month[0]) && (date[2] >= date[0]))
			return 1;
	}
	else if ((year[2] > year[0]) && (year[2] == year[1]))
	{
		if (month[2] < month[1])
			return 1;
		else if ((month[2] == month[1]) && (date[2] <= date[1]))
			return 1;
	}
	else if ((month[2] == month[0]) && (month[2] < month[1]))
	{
		if (date[2] >= date[0])
			return 1;
	}
	else if ((month[2] > month[0]) && (month[2] == month[1]))
	{
		if (date[2] <= date[1])
			return 1;
	}
	else if ((date[2] >= date[0] && date[2] <= date[1]))
		return 1;
	return 0;
}
int change_month(char month[])
{
	if (strcmp(month, "Jan") == 0)
		return 1;
	else if (strcmp(month, "Feb") == 0)
		return 2;
	else if (strcmp(month, "Mar") == 0)
		return 3;
	else if (strcmp(month, "Apr") == 0)
		return 4;
	else if (strcmp(month, "May") == 0)
		return 5;
	else if (strcmp(month, "Jun") == 0)
		return 6;
	else if (strcmp(month, "Jul") == 0)
		return 7;
	else if (strcmp(month, "Aug") == 0)
		return 8;
	else if (strcmp(month, "Sep") == 0)
		return 9;
	else if (strcmp(month, "Oct") == 0)
		return 10;
	else if (strcmp(month, "Nov") == 0)
		return 11;
	else if (strcmp(month, "Dec") == 0)
		return 12;
	else
		return 0;
}
int array_date(int date, int month, int year, int date2, int month2, int year2)
{
	if (year > year2)
		return 1;
	else if ((year == year2) && (month > month2))
		return 1;
	else if ((year == year2) && (month == month2) && (date > date2))
		return 1;
	else if ((year == year2) && (month == month2) && (date == date2))
		return 2;
	return 0;
}
int array_time(int hour, int minute, int second, int hour2, int minute2, int second2)
{
	if (hour > hour2)
		return 1;
	else if ((hour == hour2) && (minute > minute2))
		return 1;
	else if ((hour == hour2) && (minute == minute2) && (second > second2))
		return 1;
	else if ((hour == hour2) && (minute == minute2) && (second == second2))
		return 2;
	return 0;
}
char *strdup(char *s)
{
	char *p;
	p = (char *)malloc(strlen(s) + 1);
	if (p != NULL)
		strcpy(p, s);
	return p;
}