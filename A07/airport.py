import plotly
import plotly.graph_objects as go
from geo import mapbox_access_token
from geo import get_country_border
from geo import get_bbox
from geo import get_airports


if __name__ == '__main__':
    mapbox_style = "mapbox://styles/shaz13/cjiog1iqa1vkd2soeu5eocy4i"

    airLats,airLons = get_airports()

    airports = [go.Scattermapbox(
        lat=airLats,
        lon = airLons,
        mode = 'markers',
        marker=dict(
            size=6,
	    symbol = 'airport',
            color='green',
            opacity = 1,
        ),
        name='Airports'
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
    title = "Airports")

    fig = dict(data=airports, layout=layout)
    plotly.offline.plot(fig, filename='airport.html')