from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from datetime import timedelta
import datetime
import isodate
import json
import re
import requests
import os
from dotenv import load_dotenv

load_dotenv()

APIS = os.getenv('API')

URL1 = 'https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults=50&fields=items/contentDetails/videoId,nextPageToken&key={}&playlistId={}&pageToken='
URL2 = 'https://www.googleapis.com/youtube/v3/videos?&part=contentDetails&id={}&key={}&fields=items/contentDetails/duration'

# To get the playlistId from the link
def get_id(playlist_link: str) -> str:
    p = re.compile('^([\S]+list=)?([\w_-]+)[\S]*$')
    m = p.match(playlist_link)
    if m:
        return m.group(2)
    else:
        return 'invalid_playlist_link'


# To parse the datetime object into readable time
def parse(a: timedelta) -> str:
    ts, td = a.seconds, a.days
    th, tr = divmod(ts, 3600)
    tm, ts = divmod(tr, 60)
    ds = ''
    if td:
        ds += ' {} day{},'.format(td, 's' if td != 1 else '')
    if th:
        ds += ' {} hour{},'.format(th, 's' if th != 1 else '')
    if tm:
        ds += ' {} minute{},'.format(tm, 's' if tm != 1 else '')
    if ts:
        ds += ' {} second{}'.format(ts, 's' if ts != 1 else '')
    if ds == '':
        ds = '0 seconds'
    return ds.strip().strip(',')


# find if a time lies between two other times
def todayAt(hr: int, min: int = 0, sec: int = 0, micros: int = 0) -> datetime.datetime:
    now = datetime.datetime.now()
    return now.replace(hour=hr, minute=min, second=sec, microsecond=micros)


# find out which time slice an time lies in, to decide which API key to use
def find_time_slice() -> int:
    timeNow = datetime.datetime.now()
    time_slice = 0
    if todayAt(0) <= timeNow < todayAt(4):
        time_slice = 1
    elif todayAt(4) <= timeNow < todayAt(8):
        time_slice = 2
    if todayAt(8) <= timeNow < todayAt(12):
        time_slice = 3
    if todayAt(12) <= timeNow < todayAt(16):
        time_slice = 4
    if todayAt(16) <= timeNow < todayAt(20):
        time_slice = 5
    return time_slice


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/summary")
async def home(url: str = Query(..., title="YouTube Playlist URL")):
    playlist_id = get_id(url)

    next_page = ''
    cnt = 0
    a = timedelta(0)
    tsl = find_time_slice()
    display_text = []

    while True:
        vid_list = []

        try:
            results = json.loads(requests.get(URL1.format(APIS.strip("'"), playlist_id) + next_page).text)

            for x in results['items']:
                vid_list.append(x['contentDetails']['videoId'])

        except KeyError:
            return JSONResponse(content={"error": results['error']['message']}, status_code=400)

        url_list = ','.join(vid_list)
        cnt += len(vid_list)

        try:
            op = json.loads(requests.get(URL2.format(url_list, APIS.strip("'"))).text)

            for x in op['items']:
                a += isodate.parse_duration(x['contentDetails']['duration'])

        except KeyError:
            return JSONResponse(content={"error": results['error']['message']}, status_code=400)

        if 'nextPageToken' in results and cnt < 500:
            next_page = results['nextPageToken']
        else:
            if cnt >= 500:
                display_text = ['No of videos limited to 500.']
            display_text = {
                "No of videos ": str(cnt),
                "Average length of video": parse(a / cnt),
                "Total length of playlist ": parse(a),
                "At 1.25x ": parse(a / 1.25),
                "At 1.50x ": parse(a / 1.5),
                "At 1.75x ": parse(a / 1.75),
                "At 2.00x ": parse(a / 2)
            }
            break

    return JSONResponse(content=display_text)
