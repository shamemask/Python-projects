import requests
import json
import datetime

now = datetime.datetime.now()
API_KEY = "980858c5e0664ae5c32d2c7d620458f3"

longitude = 45.0355  # долгота
latitude  = 38.9753  # широта

pressure_arr = []
temperature_morn = 0
temperature_night = 0
temp_difference = 0


api_response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&exclude=minutely,alerts&appid={API_KEY}&units=metric").text
print(api_response)
json_response = json.loads(api_response)
print(json_response)
temp_difference = abs(abs(temperature_morn) - abs(temperature_night))
day=1
for i in range(5):    
    pressure_arr.append(json_response["daily"][i]["pressure"])
    print(pressure_arr)
    print(temperature_morn)
    print(temperature_night)
    temperature_morn = json_response["daily"][i]["temp"]["morn"]
    temperature_night = json_response["daily"][i]["temp"]["night"]
    if abs(abs(temperature_morn) - abs(temperature_night)) < temp_difference:
        temp_difference = temperature_morn - temperature_night
        day = i
    print(abs(abs(temperature_morn) - abs(temperature_night)))
    print(json_response["daily"][i]["temp"]["morn"])

print("Максимальное давление за пять дней равно", max(pressure_arr),
      "\nМинимальная разницей температуры между днем и ночью будет",
      int(now.strftime("%d"))-1+day, "числа" )


