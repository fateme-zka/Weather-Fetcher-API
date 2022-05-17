import requests


API_KEY = "19a3b749336622570ba40d7107581f71"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter your city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
# Well we put the url first,
# Then after ? we write the queries and data
# And we put & because we want to add another query to our url.

response = requests.get(request_url)
# We send a get request to this url and what we will achieve , would store in response variable.
# And the response would contain some data and the data is information that assosiated with our city.

# Check if we did not recieve any error:
if response.status_code == 200:
    data = response.json()
    # # print(data)
    # for i,j in data.items():
    #     print(i,":",j)

    print("<<<<<<<<<<<<<<<<")
    print("City Name:", city.upper())
    print("Country:", data["sys"]["country"].upper())
    # print("Weather:")
    print("Main:", data["weather"][0]["main"])

    temp_min = format((data["main"]["temp_min"] - 273.15), ".2f")  # C = K - 273.15
    temp_max = format((data["main"]["temp_max"] - 273.15), ".2f")
    print(f"Temperature Range:( {temp_min}C to {temp_max}C )")

    print("Wind Speed:", data["wind"]["speed"])
    print("Humidity:", data["main"]["humidity"])
    print("Timezone:", data["timezone"])
    print("Sunrise:", data["sys"]["sunrise"])
    print("Sunset:", data["sys"]["sunset"])
    print(">>>>>>>>>>>>>>>>")

else:
    print(f"An error accurred.(Error:{response.status_code})")
