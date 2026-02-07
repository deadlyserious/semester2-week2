"""
Pierre Frizelle, Student ID: 201767850

This is where you should write your code and this is what you need to upload to Gradescope for autograding.

You must NOT change the function definitions (names, arguments).

You can run the functions you define in this file by using test.py (python test.py)
Please do not add any additional code underneath these functions.
"""

import sqlite3


def customer_tickets(conn, customer_id):
    # SQL query
    query = """
        SELECT f.film_title, s.screen, t.price
        FROM customers c
        JOIN tickets t ON c.customer_id = t.customer_id
        JOIN screenings s ON s.screening_id = t.screening_id
        JOIN films f ON f.film_id = s.film_id
        WHERE c.customer_id = ?
        ORDER BY f.film_title ASC
    """
    # Executes the query on the connection and returns a list of tuples
    results = conn.execute(query, (customer_id,))
    return results.fetchall()


def screening_sales(conn):
    # SQL query
    query = """
        SELECT COUNT(t.ticket_id) AS tickets_sold, f.film_title, s.screen
        FROM screenings s 
        JOIN films f ON s.film_id = f.film_id
        LEFT JOIN tickets t ON s.screening_id = t.screening_id
        GROUP BY s.screening_id, f.film_title
        ORDER BY tickets_sold DESC
    """
    # Executes the query on the connection and returns a list of tuples
    results = conn.execute(query)
    return results.fetchall()


def top_customers_by_spend(conn, limit):
    # SQL query
    query = """
        SELECT c.customer_name, SUM(t.price) AS total_spent
        FROM customers c
        JOIN tickets t ON c.customer_id = t.customer_id
        GROUP BY c.customer_name
        ORDER BY total_spent DESC
        LIMIT ?
    """
    # Executes the query on the connection and returns a list of tuples
    results = conn.execute(query, (limit,))
    return results.fetchall()