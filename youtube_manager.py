from pytube import YouTube, Channel, Playlist, Stream, Caption, Search
from moviepy.editor import *
from google.oauth2 import service_account
from googleapiclient.discovery import build
import os

class YouTubeManager:
    """
    Class for managing youtube videos and playlists.
    """

    def __init__(self, url=None, path=None):
        self.channel = None
        self.url = url
        self.path = path
        if url:
            self.yt = self.get_youtube(self.url)
            self.pl = self.get_playlist(self.url)
        if path:
            self.create_path(self.path)
        self.streams = None
        self.captions = None
        self.video = None
        self.playlist = None
        self.stream = None
        self.caption = None
        self.stream_query = None
        self.caption_query = None
        
        self.service_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'credentials',
                                              'Service_credentials.json')
        os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'credentials'), exist_ok=True)
        self.service = self.get_service()

    def get_service(self):
        """
        Get the service.
        """
        credentials = service_account.Credentials.from_service_account_file(self.service_file_path, scopes=[
            "https://www.googleapis.com/auth/youtube.force-ssl",
            "https://www.googleapis.com/auth/youtubepartner",
            "https://www.googleapis.com/auth/youtube",
            "https://www.googleapis.com/auth/youtube.readonly",
            "https://www.googleapis.com/auth/youtube.upload",
            "https://www.googleapis.com/auth/youtubepartner-channel-audit"])
        return build("youtube", "v3", credentials=credentials)

    def get_youtube(self, url):
        """
        Get the youtube object.
        """
        self.yt = YouTube(url,use_oauth=True,allow_oauth_cache=True)
        return self.yt

    #download video using moviepy
    def download_video_moviepy(self, url, filename):
        """
        Download the video.

        :param url: str
        :param path: str
        """

        download_webfile(url=url, filename=filename, overwrite=True)

        return "Downloaded Successfully"
    def get_playlist(self, url):
        """
        Get the playlist object.
        """
        self.pl = Playlist(url)
        return self.pl

    def get_channel(self, url):
        """
        Get the channel object.
        """
        self.channel = Channel(url)
        return self.channel

    def get_streams(self):
        """
        Get the streams.
        """
        self.streams = self.yt.streams
        return self.streams

    def get_captions(self):
        """
        Get the captions.
        """
        if isinstance(self.yt, YouTube):
            self.captions = self.yt.captions
            return self.captions

    def get_video(self, yt):
        """
        Get the video.

        :param yt: YouTube object
        """
        if isinstance(yt, YouTube):
            self.video = yt.video
            return self.video
        else:
            self.video = self.yt.video
            return self.video

    def get_yt_view_count(self, yt):
        """
        Get the view count.

        :param yt: YouTube object
        """
        if isinstance(yt, YouTube):
            return yt.views
        else:
            return self.yt.views

    def get_yt_title(self, yt):
        """
        Get the title.

        :param yt: YouTube object
        """
        if isinstance(yt, YouTube):
            return yt.title
        else:
            return self.yt.title

    def get_yt_description(self, yt):
        """
        Get the description.

        :param yt: YouTube object
        """
        if isinstance(yt, YouTube):
            return yt.description
        else:
            return self.yt.description

    def get_yt_rating(self, yt):
        """
        Get the rating.

        :param yt: YouTube object
        """
        if isinstance(yt, YouTube):
            return yt.rating
        else:
            return self.yt.rating

    def get_yt_length(self, yt):
        """
        Get the length.

        :param yt: YouTube object
        """
        if isinstance(yt, YouTube):
            return yt.length
        else:
            return self.yt.length

    def get_yt_author(self, yt):
        """
        Get the author.

        :param yt: YouTube object
        """
        if isinstance(yt, YouTube):
            return yt.author
        else:
            return self.yt.author

    def get_yt_publish_date(self, yt):
        """
        Get the publish date.

        :param yt: YouTube object
        """
        if isinstance(yt, YouTube):
            return yt.publish_date
        else:
            return self.yt.publish_date

    def get_yt_keywords(self, yt):
        """
        Get the keywords.

        :param yt: YouTube object
        """
        if isinstance(yt, YouTube):
            return yt.keywords
        else:
            return self.yt.keywords

    def get_yt_thumbnail_url(self, yt):
        """
        Get the thumbnail url.

        :param yt: YouTube object
        """
        if isinstance(yt, YouTube):
            return yt.thumbnail_url
        else:
            return self.yt.thumbnail_url

    def get_yt_video_url(self, yt):
        """
        Get the video url.

        :param yt: YouTube object
        """
        if isinstance(yt, YouTube):
            return yt.video_url
        else:
            return self.yt.video_url

    def get_yt_video(self, yt):
        """
        Get the video.

        :param yt: YouTube object
        """
        if isinstance(yt, YouTube):
            return yt.video
        else:
            return self.yt.video

    def get_yt_video_id(self, yt):
        """
        Get the video id.

        :param yt: YouTube object
        """
        if isinstance(yt, YouTube):
            return yt.video_id
        else:
            return self.yt.video_id

    def get_yt_stream(self, yt, itag):
        """
        Get the stream.

        :param yt: YouTube object
        :param itag: int
        """
        if isinstance(yt, YouTube):
            self.stream = yt.streams.get_by_itag(itag)
            return self.stream
        else:
            return self.yt.streams.get_by_itag(itag)

    def get_yt_caption(self, yt, lang):
        """
        Get the caption.

        :param yt: YouTube object
        :param lang: str
        """
        if isinstance(yt, YouTube):
            self.caption = yt.captions.get_by_language_code(lang)
            return self.caption
        else:
            return self.yt.captions.get_by_language_code(lang)

    def get_channel_url(self, channel):
        """
        Get the channel url.

        :param channel: Channel object
        """
        if isinstance(channel, Channel):
            return channel.channel_url
        else:
            return self.channel.channel_url

    def get_channel_id(self, channel):
        """
        Get the channel id.

        :param channel: Channel object
        """
        if isinstance(channel, Channel):
            return channel.channel_id
        else:
            return self.channel.channel_id

    def get_channel_title(self, channel):
        """
        Get the channel title.

        :param channel: Channel object
        """
        if isinstance(channel, Channel):
            return channel.title
        else:
            return self.channel.title

    def get_channel_thumbnail_url(self, channel):
        """
        Get the channel thumbnail url.

        :param channel: Channel object
        """
        if isinstance(channel, Channel):
            return channel.thumbnail_url
        else:
            return self.channel.thumbnail_url

    def get_channel_description(self, channel):
        """
        Get the channel description.

        :param channel: Channel object
        """
        if isinstance(channel, Channel):
            return channel.description
        else:
            return self.channel.description

    def get_comments_from_google_api(self, video_id=None, channel_id=None, part="snippet", search_query=None, order="relevance",
                                     max_results=10):
        """
        Get comments from google api.

        :param video_id: str
        :param channel_id: str
        :param part: str
        :param search_query: str
        :param order: str
        :param max_results: int

        """
        if video_id:
            request = self.service.commentThreads().list(
                part=part,
                videoId=video_id,
                order=order,
                maxResults=max_results
            )
            response = request.execute()
            return response
        elif channel_id:
            request = self.service.commentThreads().list(
                part=part,
                channelId=channel_id,
                order=order,
                maxResults=max_results
            )
            response = request.execute()
            return response
        elif search_query:
            request = self.service.commentThreads().list(
                part=part,
                search_query=search_query,
                order=order,
                maxResults=max_results
            )
            response = request.execute()
            return response
        else:
            return "Please provide video_id, channel_id or search_query"

    def filtering_by_streaming_method(self, yt, method="Adaptive"):
        """
        Filtering by streaming method.

        :param yt: YouTube object
        :param method: str
        """
        if isinstance(yt, YouTube):
            if method == "Adaptive":
                return yt.streams.filter(adaptive=True)
            elif method == "Progressive":
                return yt.streams.filter(progressive=True)
            else:
                return yt.streams
        else:
            if method == "Adaptive":
                return self.yt.streams.filter(adaptive=True)
            elif method == "Progressive":
                return self.yt.streams.filter(progressive=True)
            else:
                return self.yt.streams

    def filtering_by_resolution(self, yt, resolution="720p"):
        """
        Filtering by resolution.

        :param yt: YouTube object
        :param resolution: str
        """
        if isinstance(yt, YouTube):
            return yt.streams.filter(res=resolution)
        else:
            return self.yt.streams.filter(res=resolution)

    def filtering_by_file_extension(self, yt, file_extension="mp4"):
        """
        Filtering by file extension.

        :param yt: YouTube object
        :param file_extension: str
        """
        if isinstance(yt, YouTube):
            return yt.streams.filter(file_extension=file_extension)
        else:
            return self.yt.streams.filter(file_extension=file_extension)

    def filtering_by_mime_type(self, yt, mime_type="video/mp4"):
        """
        Filtering by mime type.

        :param yt: YouTube object
        :param mime_type: str
        """
        if isinstance(yt, YouTube):
            return yt.streams.filter(mime_type=mime_type)
        else:
            return self.yt.streams.filter(mime_type=mime_type)

    def filtering_by_audio_only(self, yt, audio_only=True):
        """
        Filtering by audio only.

        :param yt: YouTube object
        :param audio_only: bool
        """
        if isinstance(yt, YouTube):
            return yt.streams.filter(only_audio=audio_only)
        else:
            return self.yt.streams.filter(only_audio=audio_only)

    def filtering_by_video_only(self, yt, video_only=True):
        """
        Filtering by video only.

        :param yt: YouTube object
        :param video_only: bool
        """
        if isinstance(yt, YouTube):
            return yt.streams.filter(only_video=video_only)
        else:
            return self.yt.streams.filter(only_video=video_only)

    def download_video(self, stream, path=None):
        """
        Download the video.

        :param stream: Stream object
        :param path: str
        """
        if not path:
            path = self.path
        if isinstance(stream, Stream):
            stream.download(path)
            return "Downloaded Successfully"
        else:
            self.stream.download(path)
            return "Downloaded Successfully"

    def get_lowest_resolution(self, video):
        """
        Args:
            video:

        Returns:

        """

        if isinstance(video, YouTube):
            return video.streams.get_lowest_resolution()
        else:
            return self.video.streams.get_lowest_resolution()

    def get_highest_resolution(self, video):
        """
        Args:
            video:

        Returns:

        """
        if isinstance(video, YouTube):
            return video.streams.get_highest_resolution()
        else:
            return self.video.streams.get_highest_resolution()

    def order_by_resolution(self, video, order="desc"):
        """
        Args:
            video:
            order:

        Returns:

        """
        if isinstance(video, YouTube):
            return video.streams.order_by('resolution', order)
        else:
            return self.video.streams.order_by('resolution', order)

    def download_caption(self, caption, path):
        """
        Download the caption.

        :param caption: Caption object
        :param path: str
        """
        if isinstance(caption, Caption):
            caption.download(path)
        else:
            self.caption.download(path)

    def download_playlist(self, playlist, path):
        """
        Download the playlist.

        :param playlist: Playlist object
        :param path: str
        """
        if isinstance(playlist, Playlist):
            for video in playlist.videos:
                self.download_video(video.streams.get_highest_resolution(), path)
        else:
            for video in self.pl.videos:
                self.download_video(video.streams.get_highest_resolution(), path)

    def download_all(self, path):
        """
        Download all.

        :param path: str
        """
        self.download_playlist(self.pl, path)

    def get_playlist_videos(self, playlist):
        """
        Get playlist videos.

        :param playlist: Playlist object
        """
        if isinstance(playlist, Playlist):
            return playlist.videos
        else:
            return self.pl.videos

    def get_subscribers_from_google_api(self, channel_id):
        """
        Get subscribers from google api.

        :param channel_id: str
        """
        ch_request = self.service.channels().list(
            part='statistics',
            id='Enter Channel ID')
        ch_response = ch_request.execute()
        subscriber_count = ch_response['items'][0]['statistics']['subscriberCount']
        return subscriber_count

    def get_channel_videos_count_from_google_api(self, channel_id):
        """
        Get channel videos count from google api.

        :param channel_id: str
        """
        ch_request = self.service.channels().list(
            part='statistics',
            id='Enter Channel ID')
        ch_response = ch_request.execute()
        if "items" not in ch_response:
            return "Channel ID is not valid"
        
        video_count = ch_response['items'][0]['statistics']['videoCount']
        return video_count

    def get_channel_views_count_from_google_api(self, channel_id):
        """
        Get channel views count from google api.

        :param channel_id: str
        """
        ch_request = self.service.channels().list(
            part='statistics',
            id='Enter Channel ID')
        ch_response = ch_request.execute()
        if "items" not in ch_response:
            return "Channel ID is not valid"
        view_count = ch_response['items'][0]['statistics']['viewCount']
        return view_count

    def get_channel_videos_from_google_api(self, channel_id):
        """
        Get channel videos from google api.

        :param channel_id: str
        """
        request = self.service.search().list(
            part="snippet,contentDetails",
            channelId=channel_id,
            type="video"
        )
        response = request.execute()
        return response

    def get_channel_playlists_from_google_api(self, channel_id):
        """
        Get channel playlists from google api.

        :param channel_id: str
        """
        request = self.service.playlists().list(
        part="snippet,contentDetails,status",
        channelId=channel_id,
        maxResults=25
        )
        response = request.execute()
        return response
    
    def get_playlist_videos_from_google_api(self, playlist_id):
        """
        Get playlist videos from google api.

        :param playlist_id: str
        """
        request = self.service.playlistItems().list(
            part="snippet",
            playlistId=playlist_id,
            maxResults=25
        )
        response = request.execute()
        return response

    
    def search(self, query):
        """
        Search.

        :param query: str
        """
        self.stream_query = Search(query)
        return self.stream_query.results

    def search_get_next(self, stream_query):
        """
        Search get next.
        """
        if isinstance(stream_query, Search):
            return stream_query.get_next_results()
        else:
            return self.stream_query.get_next_results()

    def search_completion_suggestions(self, query):
        """
        Search completion suggestions.

        :param query: str
        """
        self.stream_query = Search(query)
        return self.stream_query.completion_suggestions

    @staticmethod
    def get_video_by_url(url):
        """
        Get video by url.

        :param url: str
        """
        return YouTube(url)

    def create_path(self, path=None):
        """
        Create path.

        :param path: str
        """
        try:
            current_path = os.path.dirname(os.path.abspath(__file__))
            if path:
                path = os.path.join(current_path, path)
            else:
                if self.path:
                    path = os.path.join(current_path, self.path)
                else:
                    path = os.path.join(current_path, 'Videos')
            os.makedirs(path, exist_ok=True)
            return path
        except OSError as error:
            return error



