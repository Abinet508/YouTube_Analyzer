import re, pandas as pd
import fake_useragent
from youtube_manager import YouTubeManager
import requests
from playwright.sync_api import sync_playwright

print("YouTube Analyzer is running...")

class youtube_analyzer:
    """ 
    This class is used to analyze the YouTube channel.
    """

    def __init__(self):
        """ 
        Initialize the class with the channel url and the path.
        """

        print("Initializing the YouTube Analyzer")
        self.yt = None
        self.playlist = None
        self.videos = None
        self.channel = None
        self.url = "https://www.youtube.com/watch?v=iqPbTak_0gU&list=UULFPUBgWSsvuYwyRsGQ_Vt8lg"
        self.path = "Videos/"
        

    def check_url(self, url: str):
        """
        Check if the URL is valid or not.

        Args:
            url: str: The URL to check.

        Returns:
            str: The status of the URL.
        """
        if not re.match(r'(https?://\S+)', url):
            return "The URL is not valid"
        else:
            try:
                headers = {'User-Agent': fake_useragent.UserAgent().random}
                response = requests.get(url=url,headers=headers).status_code
                if response == 200:
                    return "The URL is valid and the website is up and running with status code 200"
                else:
                    if self.run(url) == "The URL is valid and the website is up and running with status code 200":
                        return "The URL is valid and the website is up and running with status code 200"
                    else:
                        return "The URL is valid but the website is not up and running with status code {}".format(
                            response)
            except Exception as e:
                return "The URL is valid but the website is not up and running error: {}".format(e.__str__())

    def get_channel_playlist(self):
        """
        Get the playlist of the channel.

        Args:
            []

        Returns:
            list: The playlist of the channel.
        """

        self.yt = YouTubeManager()
        self.playlist = self.yt.get_playlist(self.url)
        self.videos = self.yt.get_playlist_videos(self.playlist)
        df = pd.DataFrame(columns=["Title", "YouTube URL", "Description URL", "Description URL Status"])
        for video in self.videos:
            title = video.title
            video_url = video.watch_url
            for contents in video.initial_data.get("contents", {}).get("twoColumnWatchNextResults", {})\
                    .get("results", {}).get("results", {}).get("contents", {}):
                if "videoSecondaryInfoRenderer" in contents.keys():
                    new_contents = contents.get("videoSecondaryInfoRenderer", None)
                    if new_contents.get("attributedDescription", None) is not None:
                        if new_contents.get("attributedDescription", None).get("content", None) is not None:
                            urls = re.findall(r'(https?://\S+)', new_contents
                                              .get("attributedDescription", None).get("content", None))
                            visited = []
                            for url in urls:
                                if url in visited:
                                    continue
                                if "https://www.supersqa.com/qa-automatio" in url:
                                    url = url.replace("https://www.supersqa.com/qa-automatio",
                                                      "https://www.supersqa.com/qa-automation-training-bundle")

                                print("Title: {}, YouTube URL: {}, Description URL: {}, Description URL Status: {}"
                                      .format(title, video_url, url, self.check_url(url)))
                                df = pd.concat([df, pd.DataFrame({"Title": [title], "YouTube URL": [video_url],
                                                                  "Description URL": [url],
                                                                  "Description URL Status": [self.check_url(url)]})],
                                                  ignore_index=True)
                                visited.append(url)
                            break
        df.reset_index(drop=True, inplace=True)

        df.to_excel("Videos/Description_URLs.xlsx", index=False)
        df.to_csv("Videos/Description_URLs.csv", index=False)
        return df



    def run(url) -> str:
        with sync_playwright() as playwright:
        
            browser = playwright.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()
            page.goto(url)
            page.wait_for_load_state("networkidle")
            if page.url == url:
                return "The URL is valid and the website is up and running with status code 200"
            else:
                return "The URL is valid but the website is not up and running with status code 404"

        # ---------------------
        context.close()
        browser.close()



if __name__ == '__main__':
    ya = youtube_analyzer()
    ya.get_channel_playlist()
