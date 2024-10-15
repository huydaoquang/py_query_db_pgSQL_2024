cursor = conn.cursor()

    **delete:**
    delete_query = "DELETE FROM employees WHERE name = %s;"
    name_to_delete = ('Alice Smith',)  

    cursor.execute(delete_query, name_to_delete)

    conn.commit()

    **update:**
    update_query = "UPDATE employees SET salary = %s WHERE name = %s;"
    new_salary = 890000
    name_to_update = 'Alice Smith'

    cursor.execute(update_query, (new_salary, name_to_update))

    conn.commit()

    **limit:**
    select_query = "SELECT * FROM employees LIMIT 10;"

    cursor.execute(select_query)

    records = cursor.fetchall()
