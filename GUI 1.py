import customtkinter as ctk

# Initialize CustomTkinter settings
ctk.set_appearance_mode("Dark")  # Can be "Light" or "Dark"
ctk.set_default_color_theme("blue")  # Can be "blue", "dark-blue", or "green"

# Create the main window
root = ctk.CTk()
root.title("Custom Tkinter Dropdown Example")

# Set window size
root.geometry("1000x400")  # Adjust the size as needed

# Create a frame for the left section (possibly for content or display)
left_frame = ctk.CTkFrame(root, width=500, height=400)
left_frame.grid(row=0, column=0, padx=10, pady=10)

# Create a frame for the right section (for labels and text boxes)
right_frame = ctk.CTkFrame(root,width=1000, height=1000)
right_frame.grid(row=0, column=1, padx=10, pady=10)
timezone_options = [
    "Pacific/Midway (UTC-11:00)", 
    "America/Adak (UTC-10:00)", 
    "Pacific/Honolulu (UTC-10:00)", 
    "America/Anchorage (UTC-09:00)", 
    "America/Los_Angeles (UTC-08:00)", 
    "America/Denver (UTC-07:00)", 
    "America/Chicago (UTC-06:00)", 
    "America/New_York (UTC-05:00)", 
    "America/Caracas (UTC-04:30)", 
    "America/Santiago (UTC-04:00)", 
    "Atlantic/Bermuda (UTC-04:00)", 
    "America/St_Johns (UTC-03:30)", 
    "America/Argentina/Buenos_Aires (UTC-03:00)", 
    "America/Sao_Paulo (UTC-03:00)", 
    "Atlantic/South_Georgia (UTC-02:00)", 
    "Atlantic/Azores (UTC-01:00)", 
    "Europe/London (UTC±00:00)", 
    "Africa/Abidjan (UTC±00:00)", 
    "Europe/Berlin (UTC+01:00)", 
    "Europe/Paris (UTC+01:00)", 
    "Europe/Rome (UTC+01:00)", 
    "Africa/Lagos (UTC+01:00)", 
    "Europe/Athens (UTC+02:00)", 
    "Europe/Istanbul (UTC+02:00)", 
    "Africa/Cairo (UTC+02:00)", 
    "Asia/Jerusalem (UTC+02:00)", 
    "Asia/Baghdad (UTC+03:00)", 
    "Asia/Kuwait (UTC+03:00)", 
    "Europe/Moscow (UTC+03:00)", 
    "Asia/Tehran (UTC+03:30)", 
    "Asia/Dubai (UTC+04:00)", 
    "Asia/Baku (UTC+04:00)", 
    "Asia/Kabul (UTC+04:30)", 
    "Asia/Karachi (UTC+05:00)", 
    "Asia/Kolkata (UTC+05:30)", 
    "Asia/Kathmandu (UTC+05:45)", 
    "Asia/Dhaka (UTC+06:00)", 
    "Asia/Yangon (UTC+06:30)", 
    "Asia/Bangkok (UTC+07:00)", 
    "Asia/Shanghai (UTC+08:00)", 
    "Asia/Tokyo (UTC+09:00)", 
    "Australia/Sydney (UTC+10:00)", 
    "Pacific/Guadalcanal (UTC+11:00)", 
    "Pacific/Fiji (UTC+12:00)", 
    "Pacific/Auckland (UTC+13:00)"
]

# List of major airports
airport_options = [
    "ATL - Hartsfield-Jackson Atlanta International Airport (USA)",
    "PEK - Beijing Capital International Airport (China)",
    "LAX - Los Angeles International Airport (USA)",
    "DXB - Dubai International Airport (UAE)",
    "HND - Tokyo Haneda Airport (Japan)",
    "ORD - O'Hare International Airport (USA)",
    "LHR - London Heathrow Airport (UK)",
    "CDG - Charles de Gaulle Airport (France)",
    "DFW - Dallas/Fort Worth International Airport (USA)",
    "AMS - Amsterdam Schiphol Airport (Netherlands)",
    "FRA - Frankfurt am Main Airport (Germany)",
    "SIN - Singapore Changi Airport (Singapore)",
    "ICN - Incheon International Airport (South Korea)",
    "SYD - Sydney Kingsford Smith Airport (Australia)",
    "JFK - John F. Kennedy International Airport (USA)",
    "SFO - San Francisco International Airport (USA)",
    "CAN - Guangzhou Baiyun International Airport (China)",
    "PVG - Shanghai Pudong International Airport (China)",
    "HKG - Hong Kong International Airport (Hong Kong)",
    "KUL - Kuala Lumpur International Airport (Malaysia)",
    "BKK - Suvarnabhumi Airport (Thailand)",
    "MUC - Munich Airport (Germany)",
    "DEL - Indira Gandhi International Airport (India)",
    "MAD - Adolfo Suárez Madrid–Barajas Airport (Spain)",
    "GRU - São Paulo–Guarulhos International Airport (Brazil)",
    "BCN - Barcelona-El Prat Airport (Spain)",
    "YYZ - Toronto Pearson International Airport (Canada)",
    "MEX - Mexico City International Airport (Mexico)",
    "IST - Istanbul Airport (Turkey)",
    "ZRH - Zurich Airport (Switzerland)",
    "DOH - Hamad International Airport (Qatar)",
    "JNB - O.R. Tambo International Airport (South Africa)",
    "EZE - Ministro Pistarini International Airport (Argentina)",
    "SEA - Seattle-Tacoma International Airport (USA)",
    "MIA - Miami International Airport (USA)",
    "LAS - McCarran International Airport (USA)",
    "MNL - Ninoy Aquino International Airport (Philippines)",
    "BOM - Chhatrapati Shivaji Maharaj International Airport (India)",
    "CPT - Cape Town International Airport (South Africa)",
    "VIE - Vienna International Airport (Austria)",
    "OSL - Oslo Gardermoen Airport (Norway)",
    "ARN - Stockholm Arlanda Airport (Sweden)",
    "HEL - Helsinki-Vantaa Airport (Finland)",
    "BRU - Brussels Airport (Belgium)",
    "DME - Moscow Domodedovo Airport (Russia)",
    "SVO - Sheremetyevo International Airport (Russia)",
    "CUN - Cancun International Airport (Mexico)",
    "FCO - Leonardo da Vinci–Fiumicino Airport (Italy)",
    "NRT - Narita International Airport (Japan)",
    "GIG - Rio de Janeiro–Galeão International Airport (Brazil)",
    "LIM - Jorge Chávez International Airport (Peru)",
    "SCL - Arturo Merino Benítez International Airport (Chile)",
    "DUB - Dublin Airport (Ireland)",
    "HNL - Daniel K. Inouye International Airport (USA)",
    "PRG - Václav Havel Airport Prague (Czech Republic)",
    "WAW - Warsaw Chopin Airport (Poland)",
    "VCE - Venice Marco Polo Airport (Italy)",
    "TLV - Ben Gurion Airport (Israel)",
    "ATH - Athens International Airport (Greece)",
    "MEL - Melbourne Airport (Australia)",
    "AKL - Auckland Airport (New Zealand)",
    "CGK - Soekarno–Hatta International Airport (Indonesia)",
    "LIS - Humberto Delgado Airport (Portugal)"
]

# List of flight models
flight_model_options = [
    "Boeing 737",
    "Airbus A320",
    "Boeing 777",
    "Airbus A380",
    "Embraer E190",
    "Boeing 787 Dreamliner",
]
# Dropdown for Start (adjusting width)
start_label = ctk.CTkLabel(right_frame, text="Start")
start_label.grid(row=0, column=0, sticky="w", pady=5)

start_dropdown = ctk.CTkOptionMenu(right_frame, values=airport_options, width=300)
start_dropdown.grid(row=0, column=1, pady=5)

# Dropdown for End (adjusting width)
end_label = ctk.CTkLabel(right_frame, text="End")
end_label.grid(row=1, column=0, sticky="w", pady=5)

end_dropdown = ctk.CTkOptionMenu(right_frame, values=airport_options, width=300)
end_dropdown.grid(row=1, column=1, pady=5)

# Text entries for other fields
fields = ["Area", "Time", "ICAO24"]
entries = []  # To store the text entries if needed later

# Timezone Dropdown (adjusted to fit with the other fields)
timezone_label = ctk.CTkLabel(right_frame, text="Time Zone")
timezone_label.grid(row=len(fields)+3, column=0, sticky="w", pady=5)

timezone_dropdown = ctk.CTkOptionMenu(right_frame, values=timezone_options, width=300)
timezone_dropdown.grid(row=len(fields)+3, column=1, pady=5)
# Dropdown for Flight Model (adjusting width)
flight_model_label = ctk.CTkLabel(right_frame, text="Flight Model")
flight_model_label.grid(row=len(fields)+2, column=0, sticky="w", pady=5)

flight_model_dropdown = ctk.CTkOptionMenu(right_frame, values=flight_model_options, width=300)
flight_model_dropdown.grid(row=len(fields)+2, column=1, pady=5)

for i, field in enumerate(fields):
    label = ctk.CTkLabel(right_frame, text=field)
    label.grid(row=i+2, column=0, sticky="w", pady=5)
    
    entry = ctk.CTkEntry(right_frame)
    entry.grid(row=i+2, column=1, pady=5)
    entries.append(entry)  # Store each entry box



# Add the Search button below the last entry
search_button = ctk.CTkButton(right_frame, text="Search", command=lambda: search_function(start_dropdown, end_dropdown, entries, flight_model_dropdown))
search_button.grid(row=len(fields)+4, columnspan=2, pady=20)

# Search button callback function
def search_function(start_dropdown, end_dropdown, entries, flight_model_dropdown):
    # Get the selected value from dropdowns
    start_value = start_dropdown.get()
    end_value = end_dropdown.get()
    flight_model_value = flight_model_dropdown.get()
    time_zone = timezone_dropdown.get()
    print(f"Start: {start_value}")
    print(f"End: {end_value}")
    print(f"Flight Model: {flight_model_value}")
    print(f"Time Zone: {time_zone}")
    # Example: Print the content of each remaining entry
    for i, entry in enumerate(entries):
        print(f"{fields[i]}: {entry.get()}")

# Start the Tkinter event loop
root.mainloop()