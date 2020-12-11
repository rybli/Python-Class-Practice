# Create a Time class and initialize it with hours and minutes.
# 1. Make a method addTime which should take two time object and add them.
#       E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
# 2. Make a method displayTime which should print the time.
# 3. Make a method DisplayMinute which should display the total minutes in the Time.
#       E.g.- (1 hr 2 min) should display 62 minute.


class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, time_obj):
        tx = Time(0, 0)
        if self.minutes + time_obj.minutes > 60:
            tx.hours = int((self.minutes + time_obj.minutes) / 60)
            tx.minutes = (self.minutes + time_obj.minutes) % 60
        tx.hours += self.hours + time_obj.hours
        return f"{tx.hours} hr(s) {tx.minutes} min(s)"

    def displayTime(self):
        return f"{self.hours} hr(s) {self.minutes} min(s)"

    def DisplayMinute(self):
        return self.hours * 60 + self.minutes


t1 = Time(2, 50)
t2 = Time(1, 20)
print(t1.addTime(t2))
print(t1.displayTime())
print(t1.DisplayMinute())
