from flask import Flask, render_template, request
from datetime import datetime
import pytz
import requests

# Create Flask application instance
app = Flask(__name__)

# Home route to handle the form submission and display weather
@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    if request.method == "POST":
        city = request.form.get("city", "").strip()  # Get the city from the form
        
        if city:
             # API call to fetch weather data
            response = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=99c5a5ad5661ba99ab13d0183a18155e&units=metric"
            )
            if response.status_code == 200:
                data = response.json()

                # Get timezone offset in seconds
                timezone = data["timezone"]

                # Get the local time in the city's timezone
                local_time = datetime.now(pytz.utc).astimezone(pytz.timezone("Etc/GMT%+d" % (-timezone // 3600)))
                # Calculate the timezone offset in hours
                timezone_offset_hours = timezone // 3600  # convert seconds to hours
                timezone_str = f"GMT {timezone_offset_hours:+d}"

                # Format the local time as per your requirement
                local_time_str = local_time.strftime("%I:%M %p")  # Example: 02:07 AM


                 # Put everything together
                weather_data = {
                    "name": data["name"],
                    "temp": data["main"]["temp"],
                    "condition": data["weather"][0]["description"].capitalize(),
                    "humidity": data["main"]["humidity"],
                    "wind_speed": data["wind"]["speed"],
                    "local_time": f"{local_time_str} ({timezone_str})",
                }
            
    return render_template("index.html", weather_data=weather_data)

if __name__ == "__main__":
    app.run(debug=True)

