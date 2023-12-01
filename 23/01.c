#include <assert.h>
#include <stdio.h>
#include <string.h>

int part;

char *nums[] = {
	"one",
	"two",
	"three",
	"four",
	"five",
	"six",
	"seven",
	"eight",
	"nine",
};

int val(char *str)
{
	if ('0' <= str[0] && str[0] <= '9')
		return str[0] - '0';
	if (part == 2) for (int i = 0; i < 9; ++i) {
		if (0 == strncmp(str, nums[i], strlen(nums[i])))
			return i + 1;
	}
	return 0;
}

int search(char *buf, int len, int dir)
{
	for (int i = 0; i < len; ++i) {
		int x = val(&buf[dir == 1 ? i : len - 1 - i]);
		if (x != 0)
			return x;
	}
	return -1;
}

int solve(int p)
{
	part = p;
	FILE *input = fopen("01.txt", "r");

	int sum = 0;
	char buf[64] = {0};
	while (fgets(buf, 64, input)) {
		int len = 0;
		while (len < 64 && buf[len] != '\n')
			++len;

		int l = search(buf, len, 1);
		int r = search(buf, len, -1);
		assert(l != -1 && r != -1);
		int n = l * 10 + r;
		sum += n;

		// printf("%d: %d %d\t%s", n, l, r, buf);
	}

	fclose(input);
	return sum;
}

int main(void)
{
	printf("%d\n%d\n", solve(1), solve(2));
	return 0;
}
