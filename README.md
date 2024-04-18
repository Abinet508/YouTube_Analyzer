# YouTube Analyzer

> This Python script is used to analyze a YouTube channel. It checks the validity of a YouTube URL and performs various operations on the channel.

## Dependencies

> > The script uses the following Python libraries:

> - `re` for regular expressions
> - `pandas` for data manipulation
> - `fake_useragent` for generating fake user agents
> - `requests` for making HTTP requests
> - `playwright` for browser automation
> - `youtube_manager` (a custom module)

## How to Run

> 1. Ensure you have all the necessary dependencies installed. You can install them using pip:

```bash
pip install pandas fake_useragent requests playwright
```
> 2. Run the script using Python:

```
python Youtube_analyzer.py
```
## Class: youtube_analyzer

> This class is used to analyze a YouTube channel.

### Methods

#### __init__

> > This method initializes the class with the channel URL and the path.

#### check_url(url: str) -> str

> > This method checks if a URL is valid or not. It takes a string argument url and returns a string indicating the status of the URL.

## Note

> > This script is currently set to analyze the channel at the URL `https://www.youtube.com/watch?v=iqPbTak_0gU&list=UULFPUBgWSsvuYwyRsGQ_Vt8lg`. To analyze a different channel, change the self.url attribute in the __init__ method of the youtube_analyzer class.
