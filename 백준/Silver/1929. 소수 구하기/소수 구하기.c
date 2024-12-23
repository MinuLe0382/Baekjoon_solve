#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define size 1000001

int num[size] = { 0 };
int main(void)
{
	int m, n;
	int i, j;
	int tmp = 0;

	for (i = 2; i < size; i++)
	{
		num[i] = i;
	}

	scanf("%d %d", &m, &n);
	tmp = (int)sqrt(n);
	for (i = 2; i <= tmp; i++)
	{
		if (num[i] == 0)
		{
			continue;
		}
		else
		{
			for (j = i + 1; j <= n; j++)
			{
				if (num[j] == 0)
					continue;
				if (num[j] % i == 0)
					num[j] = 0;
			}
		}
	}
	for (i = m; i <= n; i++)
	{
		if (num[i] != 0)
		{
			printf("%d\n", num[i]);
		}
	}
	return 0;
}