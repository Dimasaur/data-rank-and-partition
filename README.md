## Description

The objective here to exemplify the use of Window functions in SQL, such as like `RANK` or `SUM` with the `OVER` keyword.

Using `OVER` clause with:
- `PARTITION BY` to select the scoped rows
- `ORDER BY` to define the order of the rows in which the window function should be applied

## Data
Using `ecommerce.sqlite` file in `data` directory.

### Order rank per customer

- Implementing `order_rank_per_customer` to rank the orders of each customer according to the order date.
- For each customer, the orders are ranked in the chronological order.
- This function returns a list of tuples like (`OrderID`, `CustomerID`, `OrderDate`, `OrderRank`).

### Order cumulative amount per customer

- Implementing `order_cumulative_amount_per_customer` to compute the cumulative amount (in USD) of the orders of each customer according to the order date.
- For each customer, the orders are ranked in the chronological order.
- This function returns list of tuples like (`OrderID`, `CustomerID`, `OrderDate`, `OrderCumulativeAmount`).
