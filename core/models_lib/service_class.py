from django.db import connection
import polars as pl

def get_df_from_sproc_cursor(cursor):
    columns = [col[0] for col in cursor.description]
    data = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
    return pl.DataFrame(data)

def test_call_sproc(job_number):
    with connection.cursor() as cursor:
        cursor.execute(
            "EXEC dbo.TestUpdateUser @job_number=%s",
            [job_number]
        )
        
        print(get_df_from_sproc_cursor(cursor))