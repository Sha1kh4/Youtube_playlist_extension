# Youtube_playlist_extension

This Extension which would help you find total length of a playlist

#### To use it in your browser
1. Clone the repository or download the extension files.

    ```bash
    git clone https://github.com/Sha1kh4/Youtube_playlist_extension.git
    ```

2. Open Google Chrome and navigate to `chrome://extensions/`.

3. Enable "Developer mode" in the top right.

4. Click "Load unpacked" and select the extension directory.


## Usage

1. Open a Chrome tab with a YouTube playlist.

2. Click on the extension icon in the toolbar.

3. Click the "Find Length" button to retrieve and display the playlist summary.



# YouTube Playlist Summary API

This Flask application provides an API to retrieve summary information about a YouTube playlist. It calculates the total number of videos, average video length, and total playlist length. Additionally, it provides estimates for playlist lengths at different playback speeds.

## API Response

The API response will include the following information:

- Number of videos in the playlist
- Average length of a video
- Total length of the playlist
- Estimated lengths at different playback speeds (1.25x, 1.5x, 1.75x, 2.0x)

## CORS Support

This app supports Cross-Origin Resource Sharing (CORS) to allow requests from different domains. CORS is enabled using the `flask_cors` extension.

## Dependencies

- Flask
- Flask-CORS
- Requests


### Todo

- [x] Create the extension
- [x] Make it working on local environment
- [x] Make it working online

- [ ] Make it work for multiple playlists on a single page  
  - [ ] To show length next to the total no. of videos in a playlist(in the same div)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
