import psycopg2

def my_select():
    conn = None
    cur = None
    rows = []

    try:
        conn = psycopg2.connect(
            host="127.0.0.1",
            port=5432,
            dbname="ct526",
            user="test",          
            password="password"   
        )

        cur = conn.cursor()
        cur.execute("""
            SELECT mid, m_name, release_date, genre, country
            FROM movie
            ORDER BY mid;
        """)

        rows = cur.fetchall()

    except Exception as e:
        print("DB Error:", e)

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

    return rows
