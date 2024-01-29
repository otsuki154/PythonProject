import os
import google.auth
from google.auth.transport.requests import Request
from google.auth.transport.requests import AuthorizedSession
from google.oauth2.credentials import Credentials
# from google.oauth2.credentials import flow_from_clientsecrets
from oauth2client.client import flow_from_clientsecrets
from oauth2client.tools import run_flow
from oauth2client.file import Storage

# File JSON chứa thông tin xác thực của ứng dụng (tạo từ Google Cloud Console)
CLIENT_SECRETS_FILE = 'client_secret_228180543332-ok2qj2apb46aei3tiuras0j5jv7odpoe.apps.googleusercontent.com.json'

# Tên của ứng dụng
APPLICATION_NAME = 'My YouTube Uploader'

# Phạm vi truy cập
SCOPES = ['https://www.googleapis.com/auth/youtube.upload', 'https://www.googleapis.com/auth/youtube.force-ssl']

def get_authenticated_service():
    credentials = None

    # Kiểm tra xem có thông tin xác thực trong file token.json hay không
    if os.path.exists('token.json'):
        credentials = Credentials.from_authorized_user_file('token.json')

    # Nếu không có hoặc hết hạn, yêu cầu người dùng xác thực
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            # Tạo một đối tượng Storage
            storage = Storage(CLIENT_SECRETS_FILE)
            flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE, SCOPES)
            # credentials = flow.run_local_server(port=0)
            credentials = run_flow(flow, storage)

        # Lưu thông tin xác thực lại để sử dụng lần sau
        with open('token.json', 'w') as token:
            token.write(credentials.to_json())

    # Trả về đối tượng YouTube
    return AuthorizedSession(credentials)

def upload_video(youtube, file_path, title, description, playlist_id=None):
    request_body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': ['tag1', 'tag2'],  # Thêm các tag của video
        },
        'status': {
            'privacyStatus': 'private',  # Có thể là "public", "private", "unlisted"
        },
    }

    if playlist_id:
        request_body['snippet']['playlistId'] = playlist_id

    response = youtube.post(
        'https://www.googleapis.com/upload/youtube/v3/videos',
        data={'uploadType': 'media', 'part': 'snippet,status'},
        files={'media_body': (file_path, open(file_path, 'rb'))},
        json=request_body,
    )

    video_id = response.json().get('id')
    print(f'Video uploaded successfully! Video ID: {video_id}')

    return video_id

def create_playlist(youtube, title, description):
    request_body = {
        'snippet': {
            'title': title,
            'description': description,
        },
        'status': {
            'privacyStatus': 'private',  # Có thể là "public", "private", "unlisted"
        },
    }

    response = youtube.post(
        'https://www.googleapis.com/youtube/v3/playlists',
        json=request_body,
        params={'part': 'snippet,status'},
    )

    playlist_id = response.json().get('id')
    print(f'Playlist created successfully! Playlist ID: {playlist_id}')

    return playlist_id

def add_video_to_playlist(youtube, video_id, playlist_id):
    request_body = {
        'snippet': {
            'playlistId': playlist_id,
            'position': 0,  # Thêm video vào đầu playlist
            'resourceId': {
                'kind': 'youtube#video',
                'videoId': video_id,
            },
        },
    }

    youtube.post(
        'https://www.googleapis.com/youtube/v3/playlistItems',
        json=request_body,
        params={'part': 'snippet'},
    )

if __name__ == '__main__':
    # Tạo đối tượng YouTube
    youtube = get_authenticated_service()

    # Đường dẫn đến file video/audio
    file_path = '1.mp4'

    # Upload video
    video_id = upload_video(youtube, file_path, 'My Video Title', 'Video description', playlist_id='your_playlist_id')

    # Tạo playlist
    playlist_id = create_playlist(youtube, 'My Playlist', 'Playlist description')

    # Thêm video vào playlist
    add_video_to_playlist(youtube, video_id, playlist_id)
