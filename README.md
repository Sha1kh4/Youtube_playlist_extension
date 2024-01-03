# Youtube_playlist_extension


## Description

This project is a FastAPI application that provides a high-performance RESTful API.This Extension which would help you find total length of a playlist

## Getting Started

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
## API Response

The API response will include the following information:

- Number of videos in the playlist
- Average length of a video
- Total length of the playlist
- Estimated lengths at different playback speeds (1.25x, 1.5x, 1.75x, 2.0x)

### Dependencies

- Python 3.6+
- FastAPI
- Uvicorn


### Todo

- [x] Create the extension
- [x] Make it working on local environment
- [x] Make it working online

- [ ] Make it work for multiple playlists on a single page  
  - [ ] To show length next to the total no. of videos in a playlist(in the same div)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
