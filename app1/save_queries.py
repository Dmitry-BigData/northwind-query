import psycopg2
import csv
import time
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


def create_and_fill_db():
    connection = psycopg2.connect(database=os.getenv('POSTGRES_DATABASE'), user=os.getenv('POSTGRES_USER'), password=os.getenv('POSTGRES_PASSWORD'), port=os.getenv('POSTGRES_PORT'), host=os.getenv('POSTGRES_HOST'))
    cursor = connection.cursor()
    northwind_string = ''
    northwind_text = ''

    with open("northwind_script.sql", "r") as northwind_script_file:
        while northwind_string != '-- PostgreSQL database dump complete':
            northwind_string = northwind_script_file.readline().strip()
            if northwind_string.startswith('--') is False and northwind_string.strip() != '':
                northwind_text += northwind_string + '\n'

    cursor.execute(northwind_text)
    connection.commit()
    connection.close()
    cursor.close()


def make_query():
    connection = psycopg2.connect(database=os.getenv('POSTGRES_DATABASE'), user=os.getenv('POSTGRES_USER'), password=os.getenv('POSTGRES_PASSWORD'), port=os.getenv('POSTGRES_PORT'), host=os.getenv('POSTGRES_HOST'))
    cursor = connection.cursor()
    query_string = ''
    query_text = ''

    with open("sql_query.sql", "r") as my_query:
        while query_string != '-- END OF QUERY':
            query_string = my_query.readline().strip()
            if query_string.startswith('--') is False and query_string.strip() != '':
                query_text += query_string + '\n'

    cursor.execute(query_text)
    result = cursor.fetchall()

    with open('query_result.csv', 'w') as query_result_csv:
        writer = csv.writer(query_result_csv)
        for row in result:
            writer.writerow(row)

    cursor.close()
    connection.close()


def main():
    create_and_fill_db()
    make_query()
    time.sleep(60)


if __name__ == '__main__':
    main()


