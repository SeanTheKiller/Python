import psycopg

conn_str = "postgresql://postgres:seansql211234@localhost:5432/postgres"

try:
    with psycopg.connect(conn_str) as conn:
        with conn.cursor() as cur:
            # 1. Define the data you want to add
            new_num = 42
            new_text = "Learning Python and Postgres in 2026!"

            # 2. Execute the INSERT command
            # Note: We use %s as placeholders and pass the data as a tuple
            cur.execute(
                "INSERT INTO test_table (num, data) VALUES (%s, %s) RETURNING id;", 
                (new_num, new_text)
            )

            # 3. Get the ID of the row we just created
            new_id = cur.fetchone()[0]
            
            # 4. IMPORTANT: Commit the transaction to save changes
            conn.commit()
            
            print(f"✅ Success! Added row with ID: {new_id}")

except Exception as e:
    print(f"❌ Error adding data: {e}")