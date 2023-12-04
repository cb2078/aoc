#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

// r g b
int cubes[] = {12, 13, 14};

struct hint {
	int n;
	int i;
};

struct hint input[100];

int parse_colour(char *s)
{
	switch (s[0]) {
		case 'r':
			return 0;
		case 'g':
			return 1;
		case 'b':
			return 2;
		default:
			return -1;
	}
}

static char *colours[] = {
	"red",
	"green",
	"blue",
};

int parse_hint(char **sp, struct hint *h)
{
	char *s = *sp;

	if (s[0] == '\n')
		return 0;

	sscanf(s, "%d", &h->n);
	while (*s++ != ' '); // move to the colour

	h->i = parse_colour(s);
	assert(h->i != -1);
	s += strlen(colours[h->i]); // move past colour
	if (s[0] != '\n')
		s += 2; // ', '

	*sp = s;
	return 1;
}

bool is_valid(struct hint *h)
{
	return h->n <= cubes[h->i];
}

int possible(char *s)
{
	// skip 'Game n: '
	while (*s != ':')
		++s;
	s += 2;

	struct hint h = {0};
	while (parse_hint(&s, &h)) {
		bool result = is_valid(&h);
		// printf("%2d %s %d\n", h.n, colours[h.i], result);
		if (!result) {
			// printf("0\n\n");
			return 0;
		}
	}

	// printf("1\n\n");
	return 1;
}

int part2(char *s)
{
	// skip 'Game n: '
	while (*s != ':')
		++s;
	s += 2;

	int maxs[] = {0, 0, 0};
	struct hint h = {0};
	while (parse_hint(&s, &h)) {
		if (h.n > maxs[h.i])
			maxs[h.i] = h.n;
	}

	int result = maxs[0] * maxs[1] * maxs[2];
	// printf("%d x %d x %d = %d\n\n", maxs[0], maxs[1], maxs[2], result);
	return result;
}

int solve(int part)
{
	FILE *f = fopen("02.txt", "r");

	int sum = 0;
	char buf[200];
	for (int i = 1; fgets(buf, 200, f); ++i) {
		if (part == 1) {
			if (possible(buf))
				sum += i;
		}
		else if (part == 2)
			sum += part2(buf);
	}

	return sum;
}

int main(void)
{
	printf("%d\n%d\n", solve(1), solve(2));
}
