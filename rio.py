import requests
from decimal import *
from operator import itemgetter, attrgetter
import ipywidgets
import urllib
import pandas as pd

txts1 = ipywidgets.widgets.Text(
 placeholder='region',
 value='eu',
 description='Region:'
 )
txts2 = ipywidgets.widgets.Text(
 placeholder='realm',
 value='Blackrock',
 description='Realm:'
 )
txts3 = ipywidgets.widgets.Text(
 placeholder='name',
 value='Bäãäm',
 description='Charname:'
 )

display(txts1)
display(txts2)
display(txts3)

reg=urllib.parse.quote_plus(txts1.value)
real=urllib.parse.quote_plus(txts2.value)
user=urllib.parse.quote_plus(txts3.value)

url1="https://raider.io/api/v1/characters/profile?region="+str(reg)+"&realm="+str(real)+"&name="+str(user)+"&fields=mythic_plus_best_runs"
url2="https://raider.io/api/v1/characters/profile?region="+str(reg)+"&realm="+str(real)+"&name="+str(user)+"&fields=mythic_plus_alternate_runs"

bestKeys = requests.get(url1)
altKeys = requests.get(url2)
#"https://raider.io/api/v1/characters/profile?region=eu&realm=Blackrock&name=B%C3%A4%C3%A3%C3%A4m&fields=mythic_plus_alternate_runs")

keystone = []
for i in altKeys.json()['mythic_plus_alternate_runs']:
    #getcontext().prec = 4
    #score = Decimal(i['score'])*Decimal(0.5)
    array=i['short_name'],i['mythic_level'],round(i['score']*0.5,2),i['affixes'][0]['name']
    keystone.append(array)

for i in bestKeys.json()['mythic_plus_best_runs']:
    #getcontext().prec = 5
    #score = Decimal(i['score'])*Decimal(1.5)
    array=i['short_name'],i['mythic_level'],round(i['score']*1.5,2),i['affixes'][0]['name']
    keystone.append(array)

a=sorted(keystone, key=itemgetter(0,3))

keylist = {
    (a[0][1],  a[0][2],  a[1][1],  a[1][2],  (a[0][2]  +a[1][2])),
    (a[2][1],  a[2][2],  a[3][1],  a[3][2],  (a[2][2]  +a[3][2])),
    (a[4][1],  a[4][2],  a[5][1],  a[5][2],  (a[4][2]  +a[5][2])),
    (a[6][1],  a[6][2],  a[7][1],  a[7][2],  (a[6][2]  +a[7][2])),
    (a[8][1],  a[8][2],  a[9][1],  a[9][2],  (a[8][2]  +a[9][2])),
    (a[10][1], a[10][2], a[11][1], a[11][2], (a[10][2] +a[11][2])),
    (a[12][1], a[12][2], a[13][1], a[13][2], (a[12][2] +a[13][2])),
    (a[14][1], a[14][2], a[15][1], a[15][2], (a[14][2] +a[15][2]))
}

b=pd.DataFrame(keylist, index=["AA","AV","COS","HOV","NO","RLP","SBG","TJS"], columns=["lvl Fortified", "Score","lvl Tyranical", "Score", "Sum Score"])

df1=pd.DataFrame(bestKeys.json()['mythic_plus_best_runs'])
df2=pd.DataFrame(altKeys.json()['mythic_plus_alternate_runs'])

df=pd.concat([df1,df2])
df.drop(columns=['map_challenge_mode_id','url','zone_id','completed_at'])




