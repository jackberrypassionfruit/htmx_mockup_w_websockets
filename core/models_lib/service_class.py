from django.db import connection
import polars as pl

def get_df_from_sproc_cursor(cursor):
    columns = [col[0] for col in cursor.description]
    data = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
    # return pl.DataFrame(data)
    return data

def test_call_sproc(job_number):
    with connection.cursor() as cursor:
        cursor.execute(
            "EXEC dbo.TestUpdateUser @job_number=%s",
            [job_number]
        )
        
        print(get_df_from_sproc_cursor(cursor))
        
def test_get_view(job_number=''):
    with connection.cursor() as cursor:
        job_number = '%'+job_number+'%'
        cursor.execute(        
            """
            SELECT
                job_number
                ,COUNT(*) AS qty_parts
            FROM [Cores2.Serialize.Master]
            WHERE scrapped IS NULL
            AND job_number LIKE %s
            GROUP BY job_number
            """,
            [job_number]
        )
        
        return get_df_from_sproc_cursor(cursor)
    
    
def test_get_serial_parts(job_number=''):
    with connection.cursor() as cursor:
        job_number = '%'+job_number+'%'
        cursor.execute(        
            """
            SELECT
                part_id
                ,job_number
            FROM [Cores2.Serialize.Master]
            WHERE scrapped IS NULL
            AND job_number LIKE %s
            """,
            [job_number]
        )
        
        return get_df_from_sproc_cursor(cursor)