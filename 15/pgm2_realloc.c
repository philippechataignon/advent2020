#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <assert.h>

int main(int argc, char* argv[]) {
    int* l;
    int N = 30000000;
    int maxl = 1 << 16;
    //int N = 2020;

    l = malloc(maxl * sizeof(int));
    for (int i = 0; i < maxl; i++) {
        l[i] = -1;
    }

    //int init[] = {0, 3, 6};
    int init[] = {1,0,18,10,19,6};

    int len_init = sizeof(init) / sizeof(int);

    for (int i=0; i < len_init; i++) {
        l[init[i]] = i;
    }

    int v = 0;
    for (int i = len_init; i < N; i++) {
        if (v > maxl) {
            maxl *= 2;
            printf("realloc %d\n", maxl);
            l = realloc(l, maxl * sizeof(int));
            assert(l != NULL);
            for (int i = maxl / 2; i < maxl; i++) {
                l[i] = -1;
            }
        }
        int m = l[v];
        int n = 0;
        if (m >= 0) {
            n = i - m;
        } else {
            n = 0;
        }
        l[v] = i;
        if (i == 2020 - 1)
            printf(">>> %d\n", v);
        if (i == N - 1)
            break;
        v = n;
    }
    printf(">>> %d\n", v);
}
