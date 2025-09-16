import mysql.connector
from geopy.distance import geodesic

# Connect to the database
connection = mysql.connector.connect(
    port=3306,
    host="localhost",
    database="flight_game",
    user="root",
    password="1q2w3e",
    autocommit=True
)

def get_airport_coordinates(icao_code):
    sql = "SELECT name, latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    cursor = connection.cursor()
    cursor.execute(sql, (icao_code,))
    result = cursor.fetchone()
    cursor.close()
    if result:
        return {
            "name": result[0],
            "coords": (result[1], result[2])
        }
    else:
        return None

def calculate_distance():
    code1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ")
    code2 = input("Anna toisen lentokentän ICAO-koodi: ")
    airport1 = get_airport_coordinates(code1)
    airport2 = get_airport_coordinates(code2)
    if not airport1 or not airport2:
        print("Väärä ICAO-koodi.")
        return

    distance_km = geodesic(airport1["coords"], airport2["coords"]).kilometers
    print(f"'{airport1['name']}' ja '{airport2['name']}' välillä on {distance_km:.2f} km.")

calculate_distance()