from datetime import timedelta
from flask import Flask, Response, request, render_template
from flask_cors import CORS  # Import CORS from flask_cors
import datetime
import isodate
import json
import re
import requests
import os
from dotenv import load_dotenv


load_dotenv()
APIS =os.getenv('API')

URL1 = 'https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults=50&fields=items/contentDetails/videoId,nextPageToken&key={}&playlistId={}&pageToken='
URL2 = 'https://www.googleapis.com/youtube/v3/videos?&part=contentDetails&id={}&key={}&fields=items/contentDetails/duration'


# To get the playlistId from the link
def get_id(playlist_link):
    p = re.compile('^([\S]+list=)?([\w_-]+)[\S]*$')
    m = p.match(playlist_link)
    if m:
        return m.group(2)
    else:
        return 'invalid_playlist_link'


# To parse the datetime object into readable time
def parse(a):
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
def todayAt(hr, min=0, sec=0, micros=0):
    now = datetime.datetime.now()
    return now.replace(hour=hr, minute=min, second=sec, microsecond=micros)


# find out which time slice an time lies in, to decide which API key to use
def find_time_slice():
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


app = Flask(__name__)

CORS(app)  
@app.route("/summary")
def home():
        playlist_link = request.args.get('url', '')
        # get playlist link/id as input from the form
        playlist_id = get_id(playlist_link)

        # initializing variables
        next_page = ''  # to hold next_page token, empty for first page
        cnt = 0  # stores number of videos in playlist
        a = timedelta(0)  # to store total length of playlist
        tsl = find_time_slice()
        display_text = []  # list to contain final text to be displayed, one item per line

        print(APIS)
        # when we make requests, we get the response in pages of 50 items
        # which we process one page at a time
        while True:
            vid_list = []

            try:
                # make first request to get list of all video_id one page of response
                print(URL1.format(APIS.strip("'"), playlist_id))
                results = json.loads(requests.get(URL1.format(APIS.strip("'"), playlist_id) + next_page).text)

                # add all ids to vid_list
                for x in results['items']:
                    vid_list.append(x['contentDetails']['videoId'])

            except KeyError:
                display_text = [results['error']['message']]
                break

            # now vid_list contains list of all videos in playlist one page of response
            url_list = ','.join(vid_list)
            # updating counter
            cnt += len(vid_list)

            try:
                # now to get the durations of all videos in url_list
                op = json.loads(requests.get(URL2.format(url_list, APIS.strip("'"))).text)

                # add all the durations to a
                for x in op['items']:
                    a += isodate.parse_duration(x['contentDetails']['duration'])

            except KeyError:
                display_text = [results['error']['message']]
                break

            # if 'nextPageToken' is not in results, it means it is the last page of the response
            # otherwise, or if the cnt has not yet exceeded 500
            if 'nextPageToken' in results and cnt < 500:
                next_page = results['nextPageToken']
            else:
                if cnt >= 500:
                    display_text = ['No of videos limited to 500.']
                display_text = {
                    "No of videos ":  str(cnt),
                    "Average length of video" :   parse(a / cnt),
                    "Total length of playlist ":  parse(a),
                    "At 1.25x ":  parse(a / 1.25),
                    "At 1.50x ":   parse(a / 1.5),
                    "At 1.75x ":   parse(a / 1.75),
                    "At 2.00x ":   parse(a / 2)
                }
                break

        return json.dumps(display_text)

if __name__ == '__main__':
    app.run()