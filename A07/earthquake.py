import plotly
import plotly.graph_objects as go
from geo import mapbox_access_token
from geo import get_country_border
from geo import get_bbox
from geo import get_earthquakes

if __name__ == '__main__':
    mapbox_style = "mapbox://styles/shaz13/cjiog1iqa1vkd2soeu5eocy4i"
    earthLats, earthLons = get_earthquakes()

    earthquakes = [go.Scattermapbox(
        lat = earthLats,
        lon = earthLons,
        mode = 'markers',
        marker=dict(
            size=6,
            color='orange',
            opacity = 1,
        ),
        name='Earthquakes'
    )]
    layout = go.Layout(autosize=True,
    mapbox = dict(accesstoken= mapbox_access_token,
    bearing=0,
    pitch=0,
    zoom=5,
    center=dict(lat=0,lon=0),
    style=mapbox_style),
    width=1500,
    height=1080,
    title = "Earthquakes")

    fig = dict(data=earthquakes, layout=layout)
    plotly.offline.plot(fig, filename='earthquake.html')
