import mysql.connector

# Connect to the database
connection = mysql.connector.connect(
    port=3306,
    host="localhost",
    database="flight_game",
    user="root",
    password="1q2w3e",
    autocommit=True
)

def get_icao_code():
    code = input("Enter ICAO code: ")
    sql = "SELECT name FROM airport WHERE ident = %s"
    cursor = connection.cursor()
    cursor.execute(sql, (code,))
    result = cursor.fetchone()
    if result:
        return result[0]
    return "Ei löydy"

print(get_icao_code())