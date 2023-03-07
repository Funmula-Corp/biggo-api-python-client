# BigGo API Python Client
BigGo API Python Client is a video API written in python. We have two APIs included so far and will update more APIs and the function in each of them in the short future.  
**BigGo API Python Client currently support Python 3.9+.**

- [Getting Started](#getting-started)
  - [Installaiton](#installaiton)
  - [Initializing API Client](#initializing-api-client)
  - [Accessing BigGo API](#accessing-biggo-api)
- [Features](#features)
  - [Video API](#video-api)
  - [User API](#user-api)
- [API Reference](#api-reference)
- [LICENSE](#license)

## Getting Started
### Installaiton
Install `biggo-api` in virtual environment.
1. create and activate virtual environment
```bash
python3 -m venv <venv-name>
source <venv-name>/bin/activate
```
2. install `biggo-api` using pip
```bash
python3 -m pip install biggo-api
```
### Initializing API Client
Begin by importing the APIClient and ClientCredentials from biggo_api module:
```Python
>>> from biggo_api.clients import APIClient, ClientCredentials
```
Next, initialize an authorized API client using client credentials:
```Python
>>> credentials = ClientCredentials(
...     client_id='my_client_id', client_secret='my_client_secret',
... )
>>> api_client = APIClient(client_credentials=credentials)
```
### Accessing BigGo API
You can use a similar approach to access all BigGo API resources using the api client. Simply access the instance client of the desired resource. For example:
```Python
# access video api
>>> video_client = api_client.video
# get video information
>>> info = video_client.get(video_id='video_id')
# access /user api
>>> user_client = api_client.user
# get client's own videos at page 1
>>> own_videos = user_client.get_own_videos(page=1)
# Use other resources in a similar way...
```

## Features
This library currently supports the following BigGo APIs (see full usage guide in [docs folder](docs)):
- `/video` - [Video Api](./docs/api/video)
- `/user` - [User Api](./docs/api/user)
### Video API
- Uploading videos.
- Getting video information - Using video ID to get the information for both video and the uploader. (ex: user ID, description, etc. )
- Editing video settings - Editing video title, description, accessibility, etc.
- Deleting videos.
### User API
- Getting video information on all uploaded videos on the personal video list.

## API Reference
See [Sphinx-docs folder](Sphinx-docs/_build/markdown/index.md)  

## LICENSE
[MIT](LICENSE)

---
[ :arrow_up: Back to top](#biggo-api-python-client)  
