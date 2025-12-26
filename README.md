# Ex04 Places Around Me
# Date:25/11/2025
# AIM
To develop a website to display details about the places around my house.

# DESIGN STEPS
## STEP 1
Create a Django admin interface.

## STEP 2
Download your city map from Google.

## STEP 3
Using <map> tag name the map.

## STEP 4
Create clickable regions in the image using <area> tag.

## STEP 5
Write HTML programs for all the regions identified.

## STEP 6
Execute the programs and publish them.

# CODE
```
views.py

from django.shortcuts import render

def govt(request):
    return render(request, 'govt.html')

def map(request):
    return render(request, 'map.html')

def show(request):
    return render(request, 'show.html')

def station(request):
    return render(request, 'station.html')

def theatre(request):
    return render(request, 'theatre.html')
```
```
urls.py

from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('korna.html', views.govt, name='korna'),
    path('Rajasthan/', views.map, name='Rajasthan'),
    path('Luni/', views.show, name='Luni'),
    path('Mogra/', views.station, name='Mogra'),
    path('Jodhpur/', views.theatre, name='jodhpur'),
]
```
```
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>Map</title>

    <!-- Internal CSS -->
    <style>
         h1{text-align: center;color:rgb(42, 138, 165);}
        img{
            display: block;
            margin-left:auto;
            margin-right:auto;
            width: 700px;
            height:250;
            border-radius: 20px;
        }
        body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            text-align: center;
        }

        h2 {
            color: red;
            font-weight: bold;
            margin-top: 20px;
        }

        h3 {
            color: blue;
            font-weight: bold;
            margin-top: 5px;
            margin-bottom: 20px;
        }

        img {
            max-width: 100%;
            height: auto;
        }

        /* Optional: add a border around the image map */
        .map-container {
            display: inline-block;
            border: 2px solid #000;
            padding: 5px;
        }


<!DOCTYPE html>
<html>
<head>
    <title>Jodhpur</title>

    <style>
        h1{text-align: center;color:brown;}
        img{
            display: block;
            margin-left:auto;
            margin-right:auto;
            width: 700px;
            height:250;
            border-radius: 20px;
        }
        /* Page background & font */
        body {
            margin: 0;
            padding: 20px;
            font-family: Arial, sans-serif;
            background: yellow;
            color: #333;
            line-height: 1.7;
        }

        /* Main heading */
        h2 {
            text-align: center;
            font-size: 36px;
            margin-top: 0;
            font-weight: bold;
            text-transform: uppercase;
            color: #b36b00; /* dark brown/yellow */
        }

        /* Sub heading */
        h3 {
            text-align: center;
            font-size: 22px;
            margin-top: 0;
            font-weight: normal;
            color: #804000;
            opacity: 0.9;
        }

        /* Horizontal line */
        hr {
            width: 60%;
            margin: 10px auto;
            border: 0;
            height: 2px;
            background: #804000;
            opacity: 0.6;
        }

        /* Paragraph styling */
        p {
            font-size: 18px;
            max-width: 900px;
            margin: 20px auto;
            background: rgba(255, 255, 255, 0.6);
            padding: 15px 20px;
            border-radius: 10px;
            
        }
    </style>

</head>

<body>
    <img src="{% static 'Umaid.jpg' %}" alt="umaid" usemap="#imap" >
    <h2>Jodhpur</h2>
    <h3>Palace</h3>
    <hr>

    <p>
        Jodhpur's palaces include Umaid Bhawan Palace, one of the world's largest 
        private residences, which is partly a hotel, a museum, and a royal residence. 
        Other
    </p>

</body>
</html>


    </style>
</head>
<body>

    <h2>Jodhpur</h2>

    <h3>Himadri (25011498)</h3>

    <div class="map-container">
        <img src="{% static 'jodhpur.png' %}" usemap="#image-map" alt="jodhpur map">
    </div>

    <map name="image-map">

        <!-- Rectangle -->
        <area alt="food" 
              title="Jodhpur Food"
              href="jodhpur.html"
              shape="rect" 
              coords="944,253,1064,318">

        <!-- Circle -->
        <area alt="Mogra"
              title="Mogra"
              href="mogra.html"
              shape="circle" 
              coords="940,587,40">

        <!-- Circle -->
        <area alt="Luni"
              title="Luni Fort"
              href="luni.html"
              shape="circle" 
              coords="648,653,50">

        <!-- Polygon -->
        <area alt="Korna"
              title="Korna"
              href="korna.html"
              shape="poly" 
              coords="640,665,288,431,300,600,500,700">

    </map>

</body>
</html>


<!DOCTYPE html>
<html>
<head>
    <title>Rajasthan</title>
    <style>
         h1{text-align: center;color:rgb(165, 42, 142);}
        img{
            display: block;
            margin-left:auto;
            margin-right:auto;
            width: 700px;
            height:250;
            border-radius: 20px;
        }
        /* Page background & text */
        body {
            margin: 0;
            padding: 20px;
            font-family: Arial, sans-serif;
            background: pink;
            color: #333;
            line-height: 1.7;
        }

        /* Main heading */
        h2 {
            text-align: center;
            font-size: 36px;
            margin-top: 0;
            font-weight: bold;
            text-transform: uppercase;
            color: #b30059;
        }

        /* Sub heading */
        h3 {
            text-align: center;
            font-size: 22px;
            margin-top: 0;
            font-weight: normal;
            color: #800040;
            opacity: 0.9;
        }

        /* Horizontal line styling */
        hr {
            width: 60%;
            margin: 10px auto;
            border: none;
            height: 2px;
            background: #800040;
            opacity: 0.6;
        }

        /* Paragraph styling */
        p {
            font-size: 18px;
            max-width: 800px;
            margin: 20px auto;
            text-align: justify;
            background: rgba(255, 255, 255, 0.4);
            padding: 15px 20px;
            border-radius: 10px;
        }
    </style>

</head>

<body>
    <img src="{% static 'Luni-Tourism-1.jpg' %} alt="jodhpur" usemap="#imap" >
    <h2>Rajasthan</h2>
    <h3>Luni</h3>
    <hr>

    <p>
        Luni is famous for its heritage hotel Fort Chanwa, which is cocooned in regal ambiance.
        Its interiors beautifully reflect the royalty of the bygone era. The in-house restaurants 
        of the hotel serve mouth-watering Rajasthani, Indian, Chinese and Continental cuisine.
    </p>

</body>
</html>


<!DOCTYPE html>
<html>
<head>
    <title>Mogra</title>
    <style>
        h1{text-align: center;color:rgb(42, 165, 61);}
        img{
            display: block;
            margin-left:auto;
            margin-right:auto;
            width: 700px;
            height:250;
            border-radius: 20px;
        }
        /* Page background & font */
        body {
            margin: 0;
            padding: 20px;
            font-family: Arial, sans-serif;
            background: purple;
            color: white;
            line-height: 1.7;
        }

        /* Main heading */
        h2 {
            text-align: center;
            font-size: 36px;
            margin-top: 0;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        /* Sub heading */
        h3 {
            text-align: center;
            font-size: 22px;
            margin-top: 0;
            font-weight: normal;
            opacity: 0.9;
        }

        /* Horizontal line styling */
        hr {
            width: 60%;
            margin: 10px auto;
            border: none;
            height: 2px;
            background: white;
            opacity: 0.7;
        }

        /* Paragraph styling */
        p {
            font-size: 18px;
            max-width: 800px;
            margin: 20px auto;
            text-align: justify;
            background: rgba(255, 255, 255, 0.2);
            padding: 15px 20px;
            border-radius: 10px;
        }
    </style>

</head>

<body>
    <img src={% static 'mogra.jpeg' %}" alt="jodhpur" usemap="#imap" >
    <h2>Mogra</h2>
    <h3>Jasmine Flower</h3>
    <hr>

    <p>
        "Mogra" most likely refers to the fragrant jasmine flower (Jasminum sambac), 
        which is commonly known as Mogra in India. "RJ" likely stands for Rajasthan, 
        given the user's location hint and search results mentioning a business called 
        "Mogra Cement And Sanitary in Udaipur-Rajasthan".
    </p>

</body>
</html>


<!DOCTYPE html>
<html>
<head>
    <title>Rajasthan</title>

    <style>
         h1{text-align: center;color:rgb(165, 144, 42);}
        img{
            display: block;
            margin-left:auto;
            margin-right:auto;
            width: 700px;
            height:250;
            border-radius: 20px;
        }
        /* Page background & font */
        body {
            margin: 0;
            padding: 20px;
            font-family: Arial, sans-serif;
            background: blue;
            color: white;
            line-height: 1.7;
        }

        /* Main heading */
        h2 {
            text-align: center;
            font-size: 36px;
            margin-top: 0;
            font-weight: bold;
            text-transform: uppercase;
        }

        /* Sub heading */
        h3 {
            text-align: center;
            font-size: 22px;
            margin-top: 0;
            font-weight: normal;
            opacity: 0.9;
        }

        /* Horizontal line */
        hr {
            width: 60%;
            margin: 10px auto;
            border: 0;
            height: 2px;
            background: white;
            opacity: 0.6;
        }

        /* Paragraph styling */
        p {
            font-size: 18px;
            max-width: 800px;
            margin: 20px auto;
            text-align: justify;
        }
    </style>

</head>

<body>
    <img src={% static 'korna.jpeg' %} alt="jodhpur" usemap="#imap" >
    <h2>Korna</h2>
    <h3>Village</h3>
    <hr>

    <p>
        Korna, a village in the Barmer district of Rajasthan, is primarily famous for 
        being a significant wintering ground for the Demoiselle Crane migratory birds 
        and for its historic Korna Fort.
    </p>

</body>
</html>

```
# OUTPUT
![alt text](<Screenshot (16).png>)
![alt text](<Screenshot 2025-12-07 225353.png>)
![alt text](<Screenshot 2025-12-07 005302.png>)
![alt text](<Screenshot 2025-12-07 011437.png>)
![alt text](<Screenshot (17).png>)
```

# RESULT
The program for implementing image maps using HTML is executed successfully.
