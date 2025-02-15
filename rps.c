/* This is a C program that plays rock paper scissors
   Author: Ja'Quis Franklin
   Date: 2/9/2025 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>
#include <string.h>

const char *choice()
{
    const char *table[] = {"Rock", "Paper", "Scissors"};
    return table[rand() % 3];
}

int main()
{
    srand(time(NULL));

    printf("Welcome to the Rock Paper Scissors Game!!\n");
    printf("[R]ock\n");
    printf("[P]aper\n");
    printf("[S]cissors\n");

    bool end = false;
    while (!end)
    {
        char userInput[10];
        char userChoice[10];

        printf("\nSHOOT: ");
        fgets(userInput, sizeof(userInput), stdin);

        switch (userInput[0])
        {
        case 'r':
        case 'R':
            strcpy(userChoice, "Rock");
            break;
        case 'p':
        case 'P':
            strcpy(userChoice, "Paper");
            break;
        case 's':
        case 'S':
            strcpy(userChoice, "Scissors");
            break;
        default:
            printf("Invalid choice. Try again.\n");
            continue;
        }

        const char *cpuChoice = choice();
        printf("The CPU chose: %s\n", cpuChoice);

        if ((strcmp(cpuChoice, "Paper") == 0 && strcmp(userChoice, "Rock") == 0) ||
            (strcmp(cpuChoice, "Scissors") == 0 && strcmp(userChoice, "Paper") == 0) ||
            (strcmp(cpuChoice, "Rock") == 0 && strcmp(userChoice, "Scissors") == 0))
        {
            printf("You Lose.\n");
            end = true;
        }
        else if ((strcmp(cpuChoice, "Rock") == 0 && strcmp(userChoice, "Paper") == 0) ||
                 (strcmp(cpuChoice, "Paper") == 0 && strcmp(userChoice, "Scissors") == 0) ||
                 (strcmp(cpuChoice, "Scissors") == 0 && strcmp(userChoice, "Rock") == 0))
        {
            printf("You Win!!!\n");
            end = true;
        }
        else
        {
            printf("It's a tie! Choose again.\n");
        }
    }

    return 0;
}
