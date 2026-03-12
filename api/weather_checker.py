import requests
import datetime
import os

# Configuration (Change to your preferred default city coordinates)
LAT = "12.97" 
LON = "77.59"

def get_weather():
    url = f"https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&current_weather=true"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temp = data['current_weather']['temperature']
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Ensure the file exists in the root
            log_entry = f"[{time}] Temp: {temp}°C | Lat: {LAT}, Lon: {LON}\n"
            
            log_file = os.path.join(os.path.dirname(__file__), "..", "weather_log.txt")
            with open(log_file, "a") as f:
                f.write(log_entry)
            print(f"Successfully logged: {temp}°C")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_weather()
