import requests

baseURL = "http://api.openweathermap.org/data/2.5/weather?"
API_Key = "77dfab831ab1d75b105490db937aea04"
city = input("Enter City Name: ")
complete_URL = baseURL + "appid=" + API_Key + "&q=" + city
response = requests.get(complete_URL,{"units": "metric"})
data = response.json()

if data["cod"] != "404":
    storedData = data["main"]
    current_temperature = storedData["temp"]
    current_pressure = storedData["pressure"]
    current_humidity = storedData["humidity"]

    print(" Temperature = " +
          str(current_temperature) + "°C"
          "\n atmospheric pressure (in hPa unit) = " +
          str(current_pressure) +
          "\n humidity (in percentage) = " +
          str(current_humidity) +
          "\n description = " + data["weather"][0]["description"])
else:
    print(" City Not Found ")