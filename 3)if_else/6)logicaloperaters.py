# evaluate multiple condition
# or for multiple condition
# and for all to be true
# not for condition not to be true

temp =20
is_ranning = False

if temp>30 or temp <0 or is_ranning:
    print("the show is canclled")

else:
    print("nothing is cancelled") 

is_sunny = True

if temp >= 28 and is_sunny:
    print("It is HOT outside 😡")
    print("It is SUNNY 🌞")
elif temp <= 0 and is_sunny:
    print("It is COLD outside 🥶")
    print("It is SUNNY 🌞")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside 🙂")
    print("It is SUNNY 🌞")
elif temp >= 28 and not is_sunny:
    print("It is HOT outside 😡")
    print("It is CLOUDY ☁️")
elif temp <= 0 and not is_sunny:
    print("It is COLD outside 🥶")
    print("It is CLOUDY ☁️")
elif 28 > temp > 0 and not is_sunny:
    print("It is WARM outside 🙂")
    print("It is CLOUDY ☁️")

           