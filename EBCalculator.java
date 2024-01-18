import java.util.Scanner;

class EBConsumer {
    int consumerNumber;
    String consumerName;
    int previousMonthReading;
    int currentMonthReading;
    int unitsConsumed;
    boolean isDomestic = false;
    double billAmount;

    public void displayDomesticFare() {
        System.out.println("Domestic Fare Details");
        System.out.println("***");
        System.out.println("First 100 units - Rs. 1 per unit");
        System.out.println("101-200 units - Rs. 2.50 per unit");
        System.out.println("201-500 units Rs. 4 per unit");
        System.out.println(">501 units Rs. 6 per unit");
    }

    public void displayCommercialFare() {
        System.out.println("Commercial Fare Details");
        System.out.println("*****");
        System.out.println("First 100 units Rs. 2 per unit");
        System.out.println("101-200 units- Rs. 4.50 per unit");
        System.out.println("201-500 units Rs. 6 per unit");
        System.out.println(">501 units Rs. 7 per unit");
    }

    public void getDetails() {
        Scanner inputs = new Scanner(System.in);
        System.out.println("Welcome To EB Calculator\n");
        System.out.println("Please Enter Your Name: ");
        this.consumerName = inputs.next();
        System.out.println("Please Enter Your Consumer Number: ");
        this.consumerNumber = inputs.nextInt();
        System.out.println("Please Enter Your Previous Month Reading: ");
        this.previousMonthReading = inputs.nextInt();
        System.out.println("Please Enter Your Current Month Reading: ");
        this.currentMonthReading = inputs.nextInt();
        System.out.println("Is this domestic Connection (yes/no): ");
        if (inputs.next().equals("yes"))
            this.isDomestic = true;
    }

    public void generateBill() {
        int numberOfUnitsConsumed = this.currentMonthReading - this.previousMonthReading;
        this.unitsConsumed = numberOfUnitsConsumed;
        double sum = 0;

        if (isDomestic) {
            for (int i = 0; i < numberOfUnitsConsumed; i++) {
                if (i < 100)
                    sum += 1;
                else if (i >= 100 && i <= 200)
                    sum += 2.5;
                else if (i > 200 && i <= 500)
                    sum += 4;
                else
                    sum += 6;
            }
        } else {
            for (int i = 0; i < numberOfUnitsConsumed; i++) {
                if (i <= 100)
                    sum += 2;
                else if (i > 100 && i <= 200)
                    sum += 4.5;
                else if (i > 200 && i <= 500)
                    sum += 6;
                else
                    sum += 7;
            }
        }
        this.billAmount = sum;
    }

    public void displayBill() {
        generateBill();
        System.out.println("The EB Bill Details");
        System.out.println("***");
        System.out.println("Consumer Number: " + this.consumerNumber);
        System.out.println("Consumer Name: " + this.consumerName);
        System.out.println("Consumer Units Consumed: " + this.unitsConsumed);

        if (this.isDomestic)
            System.out.println("You are a Domestic Consumer. Fare Details");
        else
            System.out.println("You are a Commercial Consumer. Fare Details");

        System.out.println("Amount Payable is Rs. " + this.billAmount);
    }
}

public class Main {
    public static void main(String[] args) {
        EBConsumer consumer = new EBConsumer();
        consumer.getDetails();
        consumer.displayBill();
    }
}