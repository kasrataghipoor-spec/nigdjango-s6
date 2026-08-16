<h6>
def post(request):
    city = request.POST['city']
    appid = '6ad934a76186d5d2fb596a8e925a0cae'
    units = 'metric'

    response = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={appid}&units={units}'
    )

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        icon = data['weather'][0]['icon']

        weather.objects.create(
            temp=temp,
            pressure=pressure,
            humidity=humidity,
            icon=icon
        )

        return render(request, 'weatherApp/index.html', {'x': data})


def get(request):
    return render(request, 'weatherApp/index.html')
</h6>