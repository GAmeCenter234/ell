from time import strftime
import eel
import pyowm

city= "Perm, Russia"

owm = pyowm.OWM("57ce3cdbaaba85c3ff9e217e6b0c39b5")
mgr = owm.weather_manager()

observation = mgr.weather_at_place(city)
w = observation.weather

temp = w.temperature('celsius')['temp']

print("В городе " + city + " сейчас " + str(temp) + " градусов!")

if(temp <= 10):
    print("Ппц холодно")

#eel.init("web")
#eel.start("main.html", size=("700, 700"))