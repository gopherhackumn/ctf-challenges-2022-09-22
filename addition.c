#include <stdio.h>

int main(void) {
    int value, input, tries;

    value = 2000;
    tries = 5;

    while (tries > 0) {
        printf("Current value is: %d\n", value);
        printf("Enter how much to add: ");
        scanf("%d", &input);
        value += input;

        printf("\n");
        if (value == 1000) {
            printf("Correct! The flag is: %s\n", FLAG);
            break;
        }

        tries--;
    }
}
