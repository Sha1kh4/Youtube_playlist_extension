# Youtube_playlist_extension

This Extension which would help you find total length of a playlist

#### To use it on local environment 
 
**Step 1 : Clone the repository**
run the following command in terminal
```
$ git clone https://github.com/Sha1kh4/Youtube_playlist_extension.git
```

**Step 2 : Change the directory to project folder**
run the following command in terminal
```
$ cd project-2
```
**Step 3 : install required packages**
run the following command in terminal
```
$ pip install -r req.txt
```
**step 4 : Get YouTube Data API v3 API key**


To get API key enable YouTube Data API v3 (if not done already) ,
To do so goto [YouTube Data API v3](https://console.cloud.google.com/apis/library/youtube.googleapis.com) and active the api,
then create the api key from [Google Credentials page](https://console.cloud.google.com/apis/credentials)
your api key may look like "uTvo3vHKpSQGOUj40f7kZLRmIkHn1qDc5Hv89Gt"
you may refer to [this video](https://www.youtube.com/watch?v=N18czV5tj5o) if an problem occur

**Step 5 : Add the api key to app.py file**

in app.py file replace "# Enter Api here to use the extension" with your api key(PS: add double codes before and after the api key)
ie replace 
```python
APIS = # Enter Api here to use the extension
```

with 
```python
APIS = "uTvo3vHKpSQGOUj40f7kZLRmIkHn1qDc5Hv89Gt"
```

**Step 6 : Load Your Extension in Chrome:**

Open Chrome and go to [chrome://extensions/](chrome://extensions/). Enable "Developer mode" and click on "Load unpacked." Select the directory containing your Chrome extension files (HTML, CSS, JavaScript). Your extension should now be loaded in Chrome.
you may refer to [this video](https://youtu.be/B8Ihv3xsWYs?si=ZCb_PcFU7wOG-PBx&t=595) if an problem occur


**Step 7 : Run using flask run**
run the following command in terminal
```
$ flask run
```

Done : now you can use extension 


### Todo

- [x] Create the extension
- [x] Make it working on local environment

- [ ] Make it work for multiple playlists on a single page  
  - [ ] To show length next to the total no. of videos in a playlist(in the same div)

- [ ] Make it working online