#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
    int* l;
    int N = 30000000;
    //int N = 2020;

    l = calloc(N, sizeof(int));
    for (int i = 0; i < N; i++) {
        l[i] = -1;
    }

    //int init[] = {0, 3, 6};
    int init[] = {1,0,18,10,19,6};

    int len_init = sizeof(init) / sizeof(int);

    for (int i=0; i < len_init; i++) {
        l[init[i]] = i;
    }

    int v = 0;
    int lv = 0;

    for (int i = len_init; i < N; i++) {
        int m = l[v];
        int n = 0;
        if (m >= 0) {
            n = i - m;
        } else {
            n = 0;
        }
        l[v] = i;
        lv = v;
        v = n;
        if (i == 2020 - 1)
            printf(">>> %d\n", lv);
    }
    printf(">>> %d\n", lv);
}
