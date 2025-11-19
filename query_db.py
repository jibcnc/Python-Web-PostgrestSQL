import psycopg2

def select():
    conn = None
    cur = None
    rows = []

    try:
        conn = psycopg2.connect(
            host="localhost",
            database="ct526",
            user="postgres",
            password="password"
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM movie;")
        rows = cur.fetchall()

    except Exception as e:
        print("DB Error:", e)

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

    return rows
