import requests

# The correct URL to fetch VATSIM network data
vatsim_url = "https://data.vatsim.net/v3/vatsim-data.json"

vatsim_metar_url = "https://metar.vatsim.net/:" 

# Fetch the data from the VATSIM URL
response = requests.get(vatsim_url)

response_metar = requests.get(vatsim_metar_url)


# Parse the JSON response
data = response.json()

# Access the number of unique online users
def online_user_count():
    online_users = data['general']['unique_users']
    print(f"There are currently {online_users} users online.")

# Access the number of active pilots
def online_pilots_count():
    online_pilots_count = len(data['pilots'])
    print(f"{online_pilots_count} active pilots")

# Access the number of active controllers
def online_controllers_count():
    online_controllers_count = len(data["controllers"])
    print(f"{online_controllers_count} active controllers")

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
  
  icao_code = input("Enter airport ICAO code: ")
  
  metar = f"{response}{icao_code}"
  
  print(metar)
  
get_metar_for_icao()

def main_program_loop():

    print(str("-" * 40))
    print("1. Print the number of online users\n"
          "2. Print a list of online controllers\n")

    choice = input('Choose an option: \n')

    print(str("-" * 40))

    while True:
        if choice == "1":
            online_user_count()
            online_controllers_count()
            online_pilots_count()
            break
        elif choice == "2":
            print_online_controllers()
            break
        else:
            break

main_program_loop()