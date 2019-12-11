import plotly
import plotly.graph_objects as go
from geo import mapbox_access_token
from geo import get_country_border
from geo import get_bbox
from geo import get_ufos

if __name__ == '__main__':
    mapbox_style = "mapbox://styles/shaz13/cjiog1iqa1vkd2soeu5eocy4i"
    ufoLats, ufoLons = get_ufos()

    ufos = [go.Scattermapbox(
        lat=ufoLats,
        lon = ufoLons,
        mode = 'markers',
        marker=dict(
            size=6,
	    symbol = 'ufo',
            color='blue',
            opacity = 1,
        ),
        name='Ufo_Sightings'
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
    title = "Ufo_Sightings")

    fig = dict(data=ufos, layout=layout)
    plotly.offline.plot(fig, filename='ufos.html')