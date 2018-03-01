import spotipy
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy import util
import pandas as pd
import sys
from IPython.display import clear_output

client_credentials_manager = SpotifyClientCredentials(client_id="<client_id>",client_secret="<client_secret>")
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
df = pd.read_csv("spotify_uri.txt") #csv containing all the spotify tracks
print(len(df))
df = df.drop_duplicates()
print(len(df))
import csv

from random import uniform
import time
from IPython.display import display, clear_output
#column names for the csv
fieldnames = ['uri', 'acousticness','danceability','duration_ms','energy','instrumentalness','key','liveness','loudness','mode','speechiness','tempo','time_signature','valence']
#spotify limits 50 songs per api call, limiting 50 songs per query
startvalue =0
processedCount = 0
endvalue=startvalue+50
with open('Spotify Track Features.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    while endvalue<len(df)-1:
        lsst = df.iloc[startvalue:endvalue].values.tolist()
        lst = [item for sublist in lsst for item in sublist]
        print(len(lst))
        try:
        	results = sp.audio_features(lst)
        except:
        	spleep(10)
        	results = sp.audio_features(lst)
        for result in results:
            clear_output()
            sys.stdout.write('processedCount '+str(processedCount))
            sys.stdout.flush()
            processedCount+=1
            if(result!=None):
                print('success')
            else:
                print('error')
                break
            try:
            	writer.writerow( { your_key: result[your_key] for your_key in fieldnames })
            except:
            	pass
        startvalue+=50
        endvalue+=50
print("done")