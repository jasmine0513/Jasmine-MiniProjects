"""
Jasmine Carrion
jasmine.carrion73@myhunter.cuny.edu
"""
def check_aqi():
    try:
        aqi = int(input("Enter AQI value: "))
        if 0 <= aqi <= 50:
            print("Good Air Quality")
        elif 51 <= aqi <= 100:
            print("Moderate Air Quality")
        elif 101 <= aqi <= 150:
            print("Unhealthy for Sensitive Groups")
        elif 151 <= aqi <= 200:
            print("Unhealthy Air Quality")
        elif aqi > 200:
            print("Very Unhealthy Air Quality")
        else:
            print("Invalid AQI value (negative number)")
    except ValueError:
        print("Please enter a valid integer for the AQI value.")
if __name__ == "__main__":
    check_aqi()
