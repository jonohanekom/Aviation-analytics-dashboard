import customtkinter as ctk

from api import online_user_count, online_pilots_count, online_controllers_count, \
                print_online_controllers, get_metar_for_icao, online_sup_count, \
                get_flights_for_icao

def display_online_users():
    label_online_users.configure(text=f"There are currently {online_user_count()} users online. \n"
                                    f"{online_controllers_count()} Controllers \n"
                                    f"{online_pilots_count()} Pilots\n")

def display_online_controllers():
    print_online_controllers()

def display_metar():
    icao_code = entry_icao.get().upper()
    get_metar_for_icao(icao_code)

def display_supervisors():
    online_sup_count()

def display_flights():
    icao_code = entry_icao.get().upper()
    get_flights_for_icao(icao_code)

# Initialize the main window
root = ctk.CTk()
root.geometry("1200x800")
root.title("Aviation Analytics Dashboard")

# Online Users Button
btn_online_users = ctk.CTkButton(root, text="Show online users", command=display_online_users)
btn_online_users.pack(pady=10)

# Online Users output
label_online_users = ctk.CTkLabel(root, text="", wraplength=350)  # wraplength keeps text within the width
label_online_users.pack(pady=10)

# Online Controllers Button
btn_online_controllers = ctk.CTkButton(root, text="Show Online Controllers", command=display_online_controllers)
btn_online_controllers.pack(pady=10)

# METAR Label and Entry
label_icao = ctk.CTkLabel(root, text="Enter ICAO Code for METAR:")
label_icao.pack(pady=10)
entry_icao = ctk.CTkEntry(root)
entry_icao.pack(pady=5)

# METAR Button
btn_metar = ctk.CTkButton(root, text="Get METAR", command=display_metar)
btn_metar.pack(pady=10)

# Supervisors Button
btn_supervisors = ctk.CTkButton(root, text="Show Online Supervisors", command=display_supervisors)
btn_supervisors.pack(pady=10)

# Flights Button
btn_flights = ctk.CTkButton(root, text="Show Flights for ICAO Code", command=display_flights)
btn_flights.pack(pady=10)

# Run the application
root.mainloop()
