import pymongo
import plotly
import plotly.graph_objects as go

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["armageddon"]

mapbox_access_token = "pk.eyJ1IjoibmFnYXN1Ymhhc2giLCJhIjoiY2syOXl4YWNxMTR6MzNucGJlMGhiNDlkbCJ9.qm1OyhFtkSJsOEgI-QY_sA"
mapbox_style = "mapbox://styles/nagasubhash/ck3z69qlo05re1cp7pof2peby"

volcanos = db["volcanos"]

worstPEIs = []
Geo = []
Names = []

for obj in volcanos.find():
    if len(worstPEIs) < 3:
        worstPEIs.append(float(obj["properties"]["PEI"]))
        Geo.append((float(obj['geometry']['coordinates'][1]), float(obj['geometry']['coordinates'][0])))
        Names.append(obj["properties"]["V_Name"])
    else:
        for x in range(3):
            if obj["properties"]["PEI"] > worstPEIs[x]:
                worstPEIs[x] = obj["properties"]["PEI"]
                Geo[x] = (float(obj['geometry']['coordinates'][1]), float(obj['geometry']['coordinates'][0]))
                Names[x] = obj["properties"]["V_Name"]
                break

ranking = []

if worstPEIs[0] >= worstPEIs[1] and worstPEIs[0] >= worstPEIs[2]:
    ranking.append(0)
    if worstPEIs[1] >= worstPEIs[2]:
        ranking.append(1)
        ranking.append(2)
    else:
        ranking.append(2)
        ranking.append(1)
elif worstPEIs[1] >= worstPEIs[2]:
    ranking.append(1)
    if worstPEIs[0] >= worstPEIs[2]:
        ranking.append(0)
        ranking.append(2)
    else:
        ranking.append(2)
        ranking.append(0)
else:
    ranking.append(2)
    if worstPEIs[0] >= worstPEIs[1]:
        ranking.append(0)
        ranking.append(1)
    else:
        ranking.append(1)
        ranking.append(0)

nLat, nLon = Geo[ranking[0]]
worstLat = []
worstLon = []
worstLat.append(nLat)
worstLon.append(nLon)
worst_1 = [go.Scattermapbox(
        lat=worstLat,
        lon =worstLon,
        mode = 'markers',
        marker=dict(
            size=30,
            color='red',
            opacity = 1,
        ),
        name=Names[ranking[0]]
    )]

nLat, nLon = Geo[ranking[1]]
worstLat = []
worstLon = []
worstLat.append(nLat)
worstLon.append(nLon)
Worst_2 = [go.Scattermapbox(
        lat=worstLat,
        lon =worstLon,
        mode = 'markers',
        marker=dict(
            size=20,
            color='orange',
            opacity = 1,
        ),
        name=Names[ranking[1]]
    )]

nLat, nLon = Geo[ranking[2]]
worstLat = []
worstLon = []
worstLat.append(nLat)
worstLon.append(nLon)
Worst_3 = [go.Scattermapbox(
        lat=worstLat,
        lon =worstLon,
        mode = 'markers',
        marker=dict(
            size=10,
            color='yellow',
            opacity = 1,
        ),
        name=Names[ranking[2]]
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
    title = "Armageddon2")

figure = dict(data=worst_1+Worst_2+Worst_3, layout=layout)
plotly.offline.plot(figure, filename='arm2.html')