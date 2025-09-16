import mysql.connector


connection = mysql.connector.connect(
    port=3306,
    host="localhost",
    database="flight_game",
    user="root",
    password="1q2w3e",
    autocommit=True
)


def count_airport_types_by_country():
    country = input("Enter country code: ")

    sql = """
          SELECT type, COUNT(*) AS count
          FROM airport
          WHERE iso_country = %s
          GROUP BY type
          ORDER BY count DESC \
          """

    cursor = connection.cursor()
    cursor.execute(sql, (country,))
    results = cursor.fetchall()
    cursor.close()

    if results:
        print(f"\nAirport types in {country}:")
        for airport_type, count in results:
            print(f"{airport_type}: {count}")
    else:
        print("Ei löydy")

count_airport_types_by_country()