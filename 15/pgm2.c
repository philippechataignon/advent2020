#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

int rfind(int* array, int narray, int value) {
    int ret = -1;
    for(int i = 0; i < narray; i++) {
        if (array[narray - 1 - i] == value) {
            ret = i + 1;
            break;
        }
    }
    return ret;
}

int main(int argc, char* argv[]) {
    int* l;
    l = calloc(30000000, sizeof(int));
    l[0] = 1;
    l[1] = 0;
    l[2] = 18;
    l[3] = 10;
    l[4] = 19;
    l[5] = 6;
    int len_l = 6;
    int k = len_l;
    int v = 0;

    for (int i = 0; i < 30000000 - len_l; i++) {
        int ret = rfind(l, k, v);
        int n = 0;
        if (ret >= 0) {
            n = ret;
        }
        l[k++] = v;
        v = n;
    }
    k--;
    //for(int i=2010; i<2025; i++)
    //    printf("%d %d\n", i, l[i]);
    printf("%d %d\n", l[k], k);
}
