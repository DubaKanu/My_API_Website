Weather Application

Overview
The Weather Application provides real-time weather updates by fetching data from the OpenWeatherMap API. Users can search for weather conditions in any city worldwide and get details such as temperature, weather conditions, humidity, and wind speed. To ensure performance and scalability, the application is hosted on two web servers with a load balancer managing traffic distribution.


Features

Fetches and displays real-time weather data using the OpenWeatherMap API.
Allows users to search for weather updates by entering the city name.
Displays key weather details such as temperature, humidity, wind speed, and weather conditions.
Hosted on multiple web servers with a load balancer for better performance.
API Used
OpenWeatherMap API


Base URL: https://api.openweathermap.org/data/2.5
Endpoints Used:
GET /weather?q={city name}&appid={API key}: Fetches weather details for a specified city.
For more details on the API, visit the OpenWeatherMap API Documentation.


Installation Instructions
1. Clone the repository: 
 git clone https://github.com/DubaKanu/Weather-App.git  
cd Weather-App  


2. Set up environment variables:
Create a .env file in the root directory and add your OpenWeatherMap API key:
API_KEY=your_openweathermap_api_key  


3. Start the application:
If deployed locally, run:
npm start
The app will run http://localhost:5500

 
Deployment
The application is deployed on two web servers (Web01 and Web02) with a load balancer managing traffic between them.

Web01: 3.80.204.65
Web02: 3.80.117.108

How the Application Works

1. Fetching Weather Data
•	The app fetches weather information when a city is searched using the /weather endpoint:

const url = `${BASE_URL}/weather?q=${encodeURIComponent(city)}&appid=${API_KEY}&units=metric`;  
•	Data such as temperature, humidity, wind speed, and conditions are displayed dynamically.


2. Error Handling
•	If a city is not found or there’s an API issue, an error message is displayed to guide the user.

How to Access the Application
Once deployed, the application can be accessed via:

•	Web Server 1: http://localhost:5500

•	Web Server 2: http://localhost:5500

•	Load Balancer: https://www.josephinesuccess.tech

Demo Video:
Here is a short demo video showcasing how to use the application both locally and through the load balancer. It demonstrates the following:


•	How to search for cities from different countries around the world

•	How to know the current weather, current time, humidity, wind speed, temperature, and Fahrenheit from those cities

•	https://youtu.be/OrgwmYbB39M



Challenges Faced:

•	API Errors: Addressed scenarios like invalid city names or API downtime with user-friendly error messages.

•	Load Balancer Configuration: Learning to set up traffic distribution between servers was challenging but rewarding.

•	Scalability: Ensured the app handles increased user requests without delays by leveraging a load balancer.


Credits:
•	OpenWeatherMap API: For real-time weather data.

•	Hosting: The application is deployed online for user accessibility.




