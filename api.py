import requests

url = "https://data.vatsim.net/v3/vatsim-data.json"

response = requests.get(url)


online_users =  response.json()['general']['unique_users']
print(f"There are currently {online_users} users online.")

online_controllers = response.json()['controllers']['callsign']
print(f"The following controllers are currently online: {', '.join(online_controllers)}")