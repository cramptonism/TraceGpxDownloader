# TraceGpxDownloader
Python script for downloading all GPX files from Trace. The website is dying and only supports 1-by-1 exports.

## Usage

This script assumes some familiarity with cookies and Python script execution.

### Get your authenticated session cookie

This allows the script to use an authenticated session to fetch your GPX files. I did this by logging into the Trace website (regular login no longer works for me, I had to use Facebook login which is what I initially created my account with), and then using Chrome developer tools to get the cookie.

![Cookie Example](https://github.com/cramptonism/TraceGpxDownloader/raw/main/images/cookie-example.png)

### Set your cookie

Open `cookie.txt` and paste the cookie in there.

### Run the script

Open a terminal and run `./trace-gpx-downloader.py`.

It takes a few seconds per visit, in my experience. GPX files will be found in the `gpx` subdirectory.

![Script Example](https://github.com/cramptonism/TraceGpxDownloader/raw/main/images/script-example.png)
