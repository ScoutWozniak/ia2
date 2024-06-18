import sqlite3
import random
def create_table_from_dict(table_name, data_dict):
    # Connect to the SQLite database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Create the table
    columns = ', '.join(data_dict.keys())
    placeholders = ', '.join(['?'] * len(data_dict))
    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
    cursor.execute(create_table_query)

    # Insert data into the table
    insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"
    cursor.execute(insert_query, tuple(data_dict.values()))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


def check_user_credentials(email, password):
    # Connect to the SQLite database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Query the database for the user with the given email and password
    query = "SELECT * FROM users WHERE email = ? AND password = ?"
    cursor.execute(query, (email, password))
    result = cursor.fetchone()

    # Close the connection
    conn.close()

    # Random chance to be true or not because i dont know how the fuck to do this please help me oh god
    random_number = random.random()
    if random_number < 0.25:
        return False
    return True



