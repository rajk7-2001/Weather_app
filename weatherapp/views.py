from django.shortcuts import render
import requests
# Create your views here.
def weatherview(request):
    context={
        'image':"static/search.png",
        'weather':"Search city to view the result",
        'temp':'0'
    }
    if request.method=="POST":
        city_name=request.POST.get('city','').upper()
        URL=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=30e0bce414bfe787fbc624c7356daa97"
        resp=requests.get(url=URL)
        if resp.status_code==200:
            weather=resp.json()['weather'][0]['main'].lower()
            print(weather)
            temp_cal=resp.json()['main']['temp']-273.15
            temp=round(temp_cal)
            wind=resp.json()['wind']
            weather_url={
                'clear':'static/cute smiling.png',
                'rain':'static/rainy.png',
            }
            for i in weather_url:
                if i==weather:
                    image_url=weather_url[i]
                    break
            else:
                image_url=weather_url['clear']

            context={
                'city':city_name,
                'weather':weather,
                'temp':temp,
                'wind':wind,
                'image':image_url,

            }
            return render(request,'index.html',context)
        else:
            context={
                'error':'city not found. please! try again or Enter some othe city '
            }
            return render(request,'index.html',context)
    return render(request,'index.html',context)