# online-video-platform
An online video sharing platform

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone "repo-link"
$ cd online-video-platform
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python3 -m venv video-platform
$ source video-platform/bin/activate
```

Then install the dependencies:

```sh
(video-platform)$ pip install -r requirements.txt
```
Note the `(video-platform)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `python3 -m venv video-platform`.

Once `pip` has finished downloading the dependencies:
```sh
(video-platform)$ cd online_video_platform
# Create the media folder
(video-platform)$ mkdir media/thumbnails
(video-platform)$ mkdir media/videos
(video-platform)$ cd ..
# Migrate the databases
(video-platform)$ python manage.py makemigrations
(video-platform)$ python manage.py migrate
#  To create the admin login for the app
(video-platform)$ python manage.py createsuperuser
# Run the app
(video-platform)$ python manage.py runserver
```
