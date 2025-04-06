rain_list = []
wind_list = []

def avg_rain(rainlist):
    if len(rainlist) == 0:
        return 0
    return sum(rainlist) / len(rainlist)

def avg_wind(windlist):
    if len(windlist) == 0:
        return 0
    return sum(windlist) / len(windlist)

def weather_severity(rain_avg, wind_avg):
    return (rain_avg *10) + wind_avg

print("Enter rain and wind separated by a space. Enter '-1.0' to stop.")
while True:
    data = input("Enter data: ")

    if data == "-1.0":
        break

    if " " in data:
        values = data.split()
        if len(values) == 2:
            rain_num = float(values[0])
            wind_num = float(values[1])

            rain_list.append(rain_num)
            wind_list.append(wind_num)
        else:
            print("Invalid input. Please enter exactly two numbers separated by a space.")
    else:
        print("Invalid input. Please enter two numbers separated by a space.")


average_rain = avg_rain(rain_list)
average_wind = avg_wind(wind_list)
days = len(rain_list)
severity = weather_severity(average_rain, average_wind)

print("The average rain is", round(average_rain, 1), "inches")
print("The average wind is", round(average_wind, 1), "mph")
print("The weather severity for these", days, "readings is:", round(severity, 1))
