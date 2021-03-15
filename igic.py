import requests
import os
import time
red="\033[31m"
green="\033[32m"
yellow="\033[33m"
blue="\033[34m"
purple="\033[35m"
cyan="\033[36m"
white="\033[37m"
ae_url = 'https://www.instagram.com/accounts/edit/?__a=1'
os.system("clear")
print(green,"""      ,~~.
     (  9 )-_,
(\___ )=='-'
 \ .   ) )
  \ `-' /
   `~j-'   REISS CLAN
     "=:""")
time.sleep(2)
os.system("clear")

print(blue,"""  ___ ____ ___ ____ 
 |_ _/ ___|_ _/ ___|
  | | |  _ | | |    
  | | |_| || | |___ 
 |___\____|___\____|
                    """)

print("\n\n")

ae_headers = {
"accept":"*/*",
"user-agent":"Mozilla/5.0 (Linux; Android 10; SM-A217F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36",
"save-data":"on",
"x-csrftoken":"c73NEUodrtEC9VugfHviUXhKzcK5xDfh",
"x-ig-app-id":"1217981644879628",
"origin":"https://www.instagram.com",
"sec-fetch-site":"same-origin",
"sec-fetch-mode":"cors",
"sec-fetch-dest":"empty",
"referer":"https://www.instagram.com/accounts/edit/",
"accept-encoding":"gzip, deflate, br",
"accept-language":"ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"

}


us_input=(purple+"ENTER THE TARGET: "+cyan)
user = input(us_input)

url = (f"https://instagram.com/{user}/?__a=1")

vv = requests.get(url, headers=ae_headers)

full_name = str(vv.json()['graphql']['user'].get('full_name'))


user_id = str(vv.json()["graphql"]["user"]["id"])


bio = str(vv.json()['graphql']['user'].get('biography'))


followers= str(vv.json()['graphql']['user'].get('edge_followed_by').get('count'))

pic = str(vv.json()['graphql']['user'].get('profile_pic_url'))

is_privatq= str(vv.json()['graphql']['user']['is_private'])

followed = str(vv.json()['graphql']['user']['edge_follow']['count'])

is_businessq = str(vv.json()['graphql']['user']['is_business_account'])

joined_recently = str(vv.json()['graphql']['user']['is_joined_recently'])

pic_url = requests.get(pic)

ph = pic_url.headers['last-modified']

bio_url= str(vv.json()['graphql']['user']['external_url'])
 
hl_count = str(vv.json()['graphql']['user']['highlight_reel_count'])
if bio_url=="None":
	bio_url="NO LINK IN BIO"
print(green)
info=f"""
FULL NAME: {full_name}
<><><><><><><><><><><><><><><>
USER ID: {user_id}
<><><><><><><><><><><><><><><>
BIO: {bio}
<><><><><><><><><><><><><><><>
THE FOLLOWERS: {followers}
<><><><><><><><><><><><><><><>
FOLLOWING: {followed}
<><><><><><><><><><><><><><><>
PHOTO STATUES:DOWNLOAD SUCESSFULY
<><><><><><><><><><><><><><><>
IS THE ACCOUNT PRIVATE?: {is_privatq}
<><><><><><><><><><><><><><><>
IS THE ACCOUNT BUSNESS?: {is_businessq}
<><><><><><><><><><><><><><><>
NEW_ACCOUNT?: {joined_recently}
<><><><><><><><><><><><><><><>
LAST TIME CHANGED PHOTO: {ph}
<><><><><><><><><><><><><><><>
LINK IN BIO: {bio_url}
<><><><><><><><><><><><><><><>
HIGHLIGHT COUNT: {hl_count}
"""

print(info)
photodn=("{} PHOTO.png".format(user))
with open (photodn,"wb") as image:
	image.write(pic_url.content)
	print("done")
print("\n\n")

print("CODED BY REVENGE~REISS CLAN, INSTAGRAM: rvng.py")