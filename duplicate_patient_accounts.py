import mysql.connector

def update_table(table_name, old_value, new_value):
    try:
        connection = mysql.connector.connect(
            host='18.130.135.78',
            user='DB_Portal_Dev',
            password='CTq8NqPtWIm.O2u1GMSx!dYP',
            database='puk-dev'
        )

        cursor = connection.cursor()

        sql_query = f"UPDATE {table_name} SET {table_name}.patient = %s WHERE {table_name}.patient = %s;"
        cursor.execute(sql_query, (new_value, old_value))
        connection.commit()

        print(f"Rows updated in {table_name}: {cursor.rowcount}")

    except mysql.connector.Error as error:
        print(f"Error: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == '__main__':
    old_value = input("Enter the old value: ")
    new_value = input("Enter the new value: ")

    tables_to_update = ['notes', 'prescriptions', 'tasks', 'appointments', 'invoices', 'invoice_items']

    for table in tables_to_update:
        update_table(table, old_value, new_value)
