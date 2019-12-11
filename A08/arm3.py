import pymongo
import plotly
import plotly.graph_objects as go

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["armageddon"]

mapbox_access_token = "pk.eyJ1IjoibmFnYXN1Ymhhc2giLCJhIjoiY2syOXl4YWNxMTR6MzNucGJlMGhiNDlkbCJ9.qm1OyhFtkSJsOEgI-QY_sA"
mapbox_style = "mapbox://styles/nagasubhash/ck3z69qlo05re1cp7pof2peby"

crashes = db["plane_crashes"]

Lats_1 = []
Lats_2 = []
Lats_3 = []
Lats_4 = []

Lons_1 = []
Lons_2 = []
Lons_3 = []
Lons_4 = []

for obj in crashes.find():
    if obj["TotalFatalInjuries"] != '  ' and obj["TotalFatalInjuries"] is not None:
        if int(obj["TotalFatalInjuries"]) >= 300:
            Lats_1.append(obj["Latitude"])
            Lons_1.append(obj["Longitude"])
        elif int(obj["TotalFatalInjuries"]) <300 and int(obj["TotalFatalInjuries"]) >= 200:
            Lats_2.append(obj["Latitude"])
            Lons_2.append(obj["Longitude"])
        elif int(obj["TotalFatalInjuries"]) <200 and int(obj["TotalFatalInjuries"]) >= 100:
            Lats_3.append(obj["Latitude"])
            Lons_3.append(obj["Longitude"])
        else:
            Lats_4.append(obj["Latitude"])
            Lons_4.append(obj["Longitude"])
    else:
        Lats_4.append(obj["Latitude"])
        Lons_4.append(obj["Longitude"])

L4 = [go.Scattermapbox(
        lat=Lats_1,
        lon =Lons_1,
        mode = 'markers',
        marker=dict(
            size=20,
            color='red',
            opacity = 1,
        ),
        name="Greater than 300"
    )]

L3 = [go.Scattermapbox(
        lat=Lats_2,
        lon =Lons_2,
        mode = 'markers',
        marker=dict(
            size=15,
            color='orange',
            opacity = 1,
        ),
        name="300-200"
    )]

L2 = [go.Scattermapbox(
        lat=Lats_3,
        lon =Lons_3,
        mode = 'markers',
        marker=dict(
            size=10,
            color='yellow',
            opacity = 1,
        ),
        name="200-100"
    )]

L1 = [go.Scattermapbox(
        lat=Lats_4,
        lon =Lons_4,
        mode = 'markers',
        marker=dict(
            size=5,
            color='blue',
            opacity = 1,
        ),
        name="Below 100"
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
    title = "Armageddon3")

output = dict(data=L1+L2+L3+L4, layout=layout)
plotly.offline.plot(output, filename='Arm3.html')