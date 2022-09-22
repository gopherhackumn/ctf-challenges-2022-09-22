#include <stdio.h>

int main(void) {
    int value, input, tries;

    setvbuf(stdout, NULL, _IONBF, 0);

    value = 2000;
    tries = 5;

    while (tries > 0) {
        tries--;

        printf("Current value is: %d\n", value);
        printf("Enter how much to add: ");

        if (!scanf("%d", &input)) {
            printf("Please enter an integer. Try again\n");
            continue;
        }
        value += input;

        printf("\n");
        if (value == 1000) {
            printf("Correct! The flag is: %s\n", FLAG);
            break;
        }
    }
}
