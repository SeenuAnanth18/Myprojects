#include <stdio.h>
#include <string.h>

// Structure to represent monthly expenses
struct MonthlyExpenses {
    float rent, groceries, utilities, entertainment, healthcare, transportation, total;
};

// Function to compare expenses for two months
void compareExpenses(struct MonthlyExpenses expenses1, struct MonthlyExpenses expenses2) {
    printf("\n************* Comparison Results *************\n");
    if (expenses1.total > expenses2.total) {
        printf("  Expenses for month 1 are higher than month 2.\n");
    } else if (expenses1.total < expenses2.total) {
        printf("  Expenses for month 2 are higher than month 1.\n");
    } else {
        printf("  Expenses for both months are equal.\n");
    }
    printf("**********************************************\n");
}

int main() {
    // Create instances of MonthlyExpenses structure for two months
    struct MonthlyExpenses month1, month2;

    // Input expenses for month 1
    printf("Enter expenses for month 1:\n");
    printf("Rent: ");
    scanf("%f", &month1.rent);
    printf("Groceries: ");
    scanf("%f", &month1.groceries);
    printf("Utilities: ");
    scanf("%f", &month1.utilities);
    printf("Entertainment: ");
    scanf("%f", &month1.entertainment);
    printf("Healthcare: ");
    scanf("%f", &month1.healthcare);
    printf("Transportation: ");
    scanf("%f", &month1.transportation);

    // Calculate total expenses for month 1
    month1.total = month1.rent + month1.groceries + month1.utilities +
                   month1.entertainment + month1.healthcare + month1.transportation;

    // Input expenses for month 2
    printf("\nEnter expenses for month 2:\n");
    printf("Rent: ");
    scanf("%f", &month2.rent);
    printf("Groceries: ");
    scanf("%f", &month2.groceries);
    printf("Utilities: ");
    scanf("%f", &month2.utilities);
    printf("Entertainment: ");
    scanf("%f", &month2.entertainment);
    printf("Healthcare: ");
    scanf("%f", &month2.healthcare);
    printf("Transportation: ");
    scanf("%f", &month2.transportation);

    // Calculate total expenses for month 2
    month2.total = month2.rent + month2.groceries + month2.utilities +
                   month2.entertainment + month2.healthcare + month2.transportation;

    // Compare expenses for two months
    compareExpenses(month1, month2);

    return 0;
}