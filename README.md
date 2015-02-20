# HUAWEI 4G ROUTER STATS

This project is a simple Django based project I've put together that records the stats from a HUAWEI 4G router over time and displays them as a graph.
I developed it primarily so I could see what times of the day the router was getting more use, and to ensure my usage stayed below the limits on my data plan.

Open sourced in case anyone else finds it useful, although I imagine it's a bit of a specific use case!

Project is written in Python 3, but probably works with Python 2.7+

## Setup

Check out the code and run ```./manage.py migrate```.

Stats are collected using the ```./manage.py collectstat``` command, on my setup I have this working as a cronjob every half an hour.

## Viewing Stats

Run the Django webserver with ```./manage.py runserver 0.0.0.0:8000``` then go to ```http://localhost:8000``` in your browser to view a line graph showing your upstream and downstream over time.

Simple as that!