#include <stdio.h>

int main() {
    int alice[3], bob[3];
    for (int i = 0; i < 3; i++) {
        scanf("%d", &alice[i]);
    }
    for (int i = 0; i < 3; i++) {
        scanf("%d", &bob[i]);
    }
    int aliceScore = 0, bobScore = 0;
    for (int i = 0; i < 3; i++) {
        if (alice[i] > bob[i]) {
            aliceScore++;
        } else if (alice[i] < bob[i]) {
            bobScore++;
        }
    }
    printf("%d %d \n", aliceScore, bobScore);
    return 0;
}
