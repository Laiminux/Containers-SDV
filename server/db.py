import psycopg2
from flask import current_app

def get_db():
    con = psycopg2.connect(host='db',
                          user='postgres',
                          password='admin',
                          database=current_app.config['DATABASE'])


    return con

def parse_sql(filename):
    data = open(filename, 'r').readlines()
    stmts = []
    DELIMITER = ';'
    stmt = ''

    for lineno, line in enumerate(data):
        if not line.strip():
            continue

        if line.startswith('--'):
            continue

        if 'DELIMITER' in line:
            DELIMITER = line.split()[1]
            continue

        if (DELIMITER not in line):
            stmt += line.replace(DELIMITER, ';')
            continue

        if stmt:
            stmt += line
            stmts.append(stmt.strip())
            stmt = ''
        else:
            stmts.append(line.strip())
    return stmts

def init_db():
    con = get_db()
    stmts = parse_sql("schema.sql")
    with con.cursor() as cursor:
        for stmt in stmts:
            print(stmt+"\n")
            stmt = stmt.replace("$$",";")
            print(stmt)
            cursor.execute(stmt)
