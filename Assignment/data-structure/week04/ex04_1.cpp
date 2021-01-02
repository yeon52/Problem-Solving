#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define MAX 200

typedef struct {
	int year, month, day, hour, minute, second;
} MyDate;
MyDate dates[MAX];

int array_date(int date, int month, int year, int date2, int month2, int year2);
int array_time(int hour, int minute, int second, int hour2, int minute2, int second2);
int change_month(char month[]);
char *strdup(char *s);
int main(void)
{
	char arr[MAX][50], *year_[MAX], *month_[MAX], *day_[MAX], *hour_[MAX], *minute_[MAX], *second_[MAX];
	int n;

	scanf("%d", &n);
	getchar();
	for (int i = 0; i < n; i++)
		fgets(arr[i], sizeof(arr[i]), stdin);

  for (int i = 0; i < n; i++)
	{
		day_[i] = strtok(arr[i], "[/");
		month_[i] = strtok(NULL, "/");
		year_[i] = strtok(NULL, "/:");
		hour_[i] = strtok(NULL, ":");
		minute_[i] = strtok(NULL, ":");
		second_[i] = strtok(NULL, "]");
	}
	
	for (int i = 0; i < n; i++)
	{
		dates[i].day = atoi(day_[i]);
		dates[i].month = change_month(month_[i]);
		dates[i].year = atoi(year_[i]);
		dates[i].hour = atoi(hour_[i]);
		dates[i].minute = atoi(minute_[i]);
		dates[i].second = atoi(second_[i]);
	}
	int z = n, tmp = 0;
	while (z > 0)
	{
		for (int j = 0; j < z - 1; j++)
		{
			if (array_date(dates[j].day, dates[j].month, dates[j].year, dates[j+1].day, dates[j+1].month, dates[j+1].year) == 1)
			{
				tmp = dates[j].day;
				dates[j].day = dates[j + 1].day;
				dates[j + 1].day = tmp;

				tmp = dates[j].month;
				dates[j].month = dates[j + 1].month;
				dates[j + 1].month = tmp;

				tmp = dates[j].year;
				dates[j].year = dates[j + 1].year;
				dates[j + 1].year = tmp;

				tmp = dates[j].hour;
				dates[j].hour = dates[j + 1].hour;
				dates[j + 1].hour = tmp;

				tmp = dates[j].minute;
				dates[j].minute = dates[j + 1].minute;
				dates[j + 1].minute = tmp;

				tmp = dates[j].second;
				dates[j].second = dates[j + 1].second;
				dates[j + 1].second = tmp;
			}
			else if (array_date(dates[j].day, dates[j].month, dates[j].year, dates[j + 1].day, dates[j + 1].month, dates[j + 1].year) == 2) //날짜가 같은경우 시분초
			{
				if (array_time(dates[j].hour, dates[j].minute, dates[j].second, dates[j + 1].hour, dates[j + 1].minute, dates[j + 1].second) == 1)
				{
					tmp = dates[j].day;
					dates[j].day = dates[j + 1].day;
					dates[j + 1].day = tmp;

					tmp = dates[j].month;
					dates[j].month = dates[j + 1].month;
					dates[j + 1].month = tmp;

					tmp = dates[j].year;
					dates[j].year = dates[j + 1].year;
					dates[j + 1].year = tmp;

					tmp = dates[j].hour;
					dates[j].hour = dates[j + 1].hour;
					dates[j + 1].hour = tmp;

					tmp = dates[j].minute;
					dates[j].minute = dates[j + 1].minute;
					dates[j + 1].minute = tmp;

					tmp = dates[j].second;
					dates[j].second = dates[j + 1].second;
					dates[j + 1].second = tmp;
				}
			}
		}
		z--;
	}
	for (int i = 0; i < n; i++)
		printf("%02d-%02d-%02d:%02d:%02d:%02d\n", dates[i].year, dates[i].month, dates[i].day, dates[i].hour, dates[i].minute, dates[i].second);
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
char *strdup(char *s)
{
	char *p;
	p = (char *)malloc(strlen(s) + 1);
	if (p != NULL)
		strcpy(p, s);
	return p;
}
