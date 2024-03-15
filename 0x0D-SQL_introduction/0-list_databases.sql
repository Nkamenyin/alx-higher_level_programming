import mysql.connector

def list_databases(host, username, password):
    try:
        # Establish connection to MySQL server
        connection = mysql.connector.connect(
            host=host,
            user=username,
            password=password
        )

        # Create a cursor object
        cursor = connection.cursor()

        # Execute SQL query to list databases
        cursor.execute("SHOW DATABASES")

        # Fetch all database names
        databases = cursor.fetchall()

        # Print the list of databases
        print("List of databases:")
        for database in databases:
            print(database[0])

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Replace the placeholders with your MySQL server details
host = 'localhost'
username = 'your_username'
password = 'your_password'

# Call the function to list databases
list_databases(host, username, password)
