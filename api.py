import requests

# The correct URL to fetch VATSIM network data
VATSIM_URL = "https://data.vatsim.net/v3/vatsim-data.json"

# Fetch the data from the VATSIM URL
response = requests.get(VATSIM_URL)

# Parse the JSON response
data = response.json()

# Access the number of unique online users
def online_user_count():
    online_users = data['general']['unique_users']
    return str(online_users)
    # print(f"There are currently {online_users} users online.")

# Access the number of active pilots
def online_pilots_count():
    online_pilots_count = len(data['pilots'])
    # print(f"{online_pilots_count} active pilots")
    return str(online_pilots_count)

# Access the number of active controllers
def online_controllers_count():
    online_controllers_count = len(data["controllers"])
    # print(f"{online_controllers_count} active controllers")
    return str(online_controllers_count)

# Access the list of online controllers and print them
def print_online_controllers():
    #list of acceptable suffix
    controller_suffix = ["_DEL" , "_GND" , "_TWR" , "_APP" , "_DEP" , "_CTR" , "_FSS"]

    # Extract the list of controllers and their callsigns
    online_controllers = [controller['callsign'] for controller in data['controllers'] if any(controller['callsign'].endswith(s) for s in controller_suffix)]

    online_controllers.sort()

    # Print the list of online controllers
    for callsign in online_controllers:
        print(callsign)

def get_metar_for_icao():
    icao_code = input("Enter the icao code for the airport you wish to check: ").upper()
    metar_url = f"https://metar.vatsim.net/{icao_code}"
    
    try:
        response_metar = requests.get(metar_url)
        
        metar_data = response_metar.text
        if "No METAR" not in metar_data:
            print(f"METAR: {metar_data}")
        else:
            print(f"No METAR data found for {icao_code}")
    except requests.exceptions.RequestException as e:
        return f"Error fetching METAR: {e}"
    
def online_sup_count():
    sup_suffix = [ "_SUP" ]

    online_sup_count = [controller['callsign'] for controller in data['controllers'] if any(controller['callsign'].endswith(s) for s in sup_suffix)]

    online_sup_count.sort()
    num_online_sups = len(online_sup_count)
    
    if num_online_sups > 0:
        print(f"There are currently {num_online_sups} Supervisors online.")
        print(f"In your time of need these are the supervisors online that will be ignoring your call for help:")
    else:
        print("There is no help coming your way, best of luck!")

    for callsign in online_sup_count:
        return callsign


def get_flights_for_icao(icao_code):

    response = requests.get(VATSIM_URL)
    data = response.json()

    # Extract the list of pilots
    online_pilots = data.get("pilots", [])
    inbound_flights = []
    outbound_flights = []


    # Filter flights based on the ICAO code
    for pilot in online_pilots:
        flight_plan = pilot.get("flight_plan")

        # Proceed only if flight_plan is not None
        if flight_plan:
            if flight_plan.get("arrival") == icao_code:
                inbound_flights.append({
                    "callsign": pilot.get("callsign"),
                    "departure": flight_plan.get("departure"),
                    "arrival": flight_plan.get("arrival"),
                })
            elif flight_plan.get("departure") == icao_code:
                outbound_flights.append({
                    "callsign": pilot.get("callsign"),
                    "departure": flight_plan.get("departure"),
                    "arrival": flight_plan.get("arrival"),
                })

    # Print inbound flights
    print(f"Inbound flights to {icao_code}:")
    for flight in inbound_flights:
        print(f"Callsign: {flight['callsign']}\n"
              f"Departure: {flight['departure']}\n"
              f"Arrival: {flight['arrival']}\n")


    # Print outbound flights
    print(f"\nOutbound flights from {icao_code}:")
    for flight in outbound_flights:
        print(f"Callsign: {flight['callsign']}\n"
              f"Departure: {flight['departure']}\n"
              f"Arrival: {flight['arrival']}\n")

    total_inbound_flights = len(outbound_flights) + len(inbound_flights)

    print(f"{len(inbound_flights)} flights inbound to {icao_code}\n"
            f"{len(outbound_flights)} flights outbound from {icao_code}\n"
            f"Total flights: {total_inbound_flights}")
