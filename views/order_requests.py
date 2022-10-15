import sqlite3
import json
from models import Order, Style, Size, Metal
from views import metal_requests
ORDERS = [
    {
            "id": 1,
            "metalId": 3,
            "sizeId": 2,
            "styleId": 3,
            "timestamp": 1614659931693
        }
]

def get_all_orders():
    # Open a connection to the database
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.metal_id,
            a.style_id,
            a.size_id,
            a.timestamp,
            m.metal,
            m.price metal_price,
            s.style,
            s.price style_price,
            z.carets,
            z.price size_price
            
        FROM orders a
        JOIN Metals m ON m.id = a.metal_id
        JOIN Styles s ON s.id = a.style_id
        JOIN Sizes z ON z.id = a.size_id
        """)

        # Initialize an empty list to hold all order representations
        orders = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an order instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # order class above.
            order = Order(row['id'], row['metal_id'], row['style_id'], row['size_id'], row['timestamp'])
            style = Style(row['style_id'], row['style'], row['style_price'])
            size = Size(row['size_id'], row['carets'], row['size_price'])
            metal = Metal(row['metal_id'], row['metal'], row['metal_price'])
            
            order.style = style.__dict__
            order.size = size.__dict__
            order.metal = metal.__dict__

            orders.append(order.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(orders)


# Function with a single parameter
def get_single_order(id):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.metal_id,
            a.style_id,
            a.size_id,
            a.timestamp
        FROM orders a
        WHERE a.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an order instance from the current row
        order = Order(data['id'], data['metal_id'], data['style_id'], data['size_id'], data['timestamp'])

        return json.dumps(order.__dict__)

def create_order(new_order):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO orders
            ( metal_id, style_id, size_id, timestamp )
        VALUES
            ( ?, ?, ?, ?);
        """, (new_order['metal_id'], new_order['style_id'],
              new_order['size_id'], new_order['timestamp'], ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the order dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_order['id'] = id


    return new_order

def delete_order(id):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM orders
        WHERE id = ?
        """, (id, ))
        
def update_order(id, new_order):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE orders
            SET
                metal_id = ?,
                style_id = ?,
                size_id = ?,
                timestamp = ?
        WHERE id = ?
        """, (new_order['metal_id'], new_order['style_id'],
              new_order['size_id'], new_order['timestamp'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True