# Create a Temperature class. Make two methods :
# 1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
# 2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.


class Temperature:
    def __repr__(self):
        return "A class that does temperature conversions:\n" \
               "    - convertToFahrenheit\n" \
               "    - convertToCelcius"

    # Convert Celcius to Fahrenheit
    # (0°C × 9 / 5) + 32 = 32°F
    def convertToFahrenheit(self, celcius_temp):
        return (celcius_temp * 9 / 5) + 32

    # Convert Fahrenheit to Celcius
    # (32°F − 32) × 5/9 = 0°C
    def convertToCelcius(self, fahrenheit_temp):
        return (fahrenheit_temp - 32) * 5 / 9


temp = Temperature()
print(temp.convertToCelcius(32))
print(temp.convertToFahrenheit(0))
print(temp)
