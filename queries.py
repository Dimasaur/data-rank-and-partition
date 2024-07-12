# pylint:disable=C0111,C0103

import sqlite3


def order_rank_per_customer(db):
    query = """
    SELECT
	Orders.OrderID,
	Orders.CustomerID,
	Orders.OrderDate,
        RANK () OVER (
	    PARTITION BY Orders.CustomerID
	    ORDER BY Orders.OrderDate
    ) AS order_rank
    FROM Orders
    """
    conn = sqlite3.connect('data/ecommerce.sqlite')
    db = conn.cursor()
    db.execute(query)
    results = db.fetchall()
    print(results)
    return results


def order_cumulative_amount_per_customer(db):
    query = """
    WITH output_ AS (
    SELECT
	    Orders.OrderID,
	    Orders.CustomerID,
	    Orders.OrderDate,
    SUM(OrderDetails.UnitPrice * OrderDetails.Quantity) OVER (
	    PARTITION BY Orders.CustomerID
	    Order BY Orders.OrderDate) AS  OrderCumulativeAmount
    FROM
	    Orders
    JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
    )

    SELECT DISTINCT output_.OrderID,
	    output_.CustomerID,
	    output_.OrderDate,
	    output_.OrderCumulativeAmount
    FROM output_

    """
    conn = sqlite3.connect('data/ecommerce.sqlite')
    db = conn.cursor()
    db.execute(query)
    results = db.fetchall()
    print(results)
    return results
