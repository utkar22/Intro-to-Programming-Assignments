# Supermarket Application

This application simulates an interactive supermarket scenario. It allows customers to make purchases, calculates costs, applies discounts and taxes, and provides a final summary of the transaction. The supermarket offers a range of items across three categories: Apparels, Electronics, and Eatables.

## Getting Started

To run the supermarket application, follow these steps:

1. Clone the repository to your local machine.
2. Open the terminal and navigate to the project directory.
3. Run the application using the command `python supermarket.py`.

## Application Flow

1. Greeting: The application greets the customer and displays the available items.
2. Order Type: The customer is asked to choose between a bulk order or a regular order.
3. Order Input: The customer provides their order details based on the chosen order type.
4. Order Summary: A summary of the customer's order is displayed.
5. Category-wise Cost: The application calculates and displays the cost of each category.
6. Discounts: Any applicable discounts are automatically applied and displayed.
7. Taxes: The application calculates and displays the taxes for each category.
8. Coupon Code: The customer is prompted to enter a coupon code (if available).
9. Final Costs: The application calculates and displays the final costs after applying discounts and taxes.
10. Farewell: The application says goodbye to the customer.

## Item List

| Item Code | Item Name   | Price | Category   |
| --------- | ----------- | ----- | ---------- |
| 0         | Tshirt      | 500   | Apparels   |
| 1         | Trousers    | 600   | Apparels   |
| 2         | Scarf       | 250   | Apparels   |
| 3         | Smartphone  | 20000 | Electronics|
| 4         | iPad        | 30000 | Electronics|
| 5         | Laptop      | 50000 | Electronics|
| 6         | Eggs        | 5     | Eatables   |
| 7         | Chocolate   | 10    | Eatables   |
| 8         | Juice       | 100   | Eatables   |
| 9         | Milk        | 45    | Eatables   |

## Requirements

- Python 3.x

## License

This project is licensed under the [MIT License](LICENSE).
