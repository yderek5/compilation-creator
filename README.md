# Youtube Automation Project

## Installation Steps

### Install virtualenv

- For Unix OS
  - `python3 -m pip install --user virtualenv`

- For Windows
  - `py -m pip install --user virtualenv`

### Create a Virtual Environment

- For Unix OS
  - `python3 -m venv dev`

- For Windows
  - `py -m venv dev`

### Activate Your dev Virtual Environment

- For Unix OS
  - `source dev/bin/activate`

- For Windows
  - `.\env\Scripts\activate`

### Install dependencies
- `pip install -r requirements.txt`

## Leaving Your Virtual Environment

`deactivate`

## Setup Reddit API secrets

Make a new file in the root of the project called `config.py` and make it look like the following:

```
client_id = "client id"
client_secret = "your client secret"
user_agent = "whatever you want to describe your reddit app"
```

_NOTE_: YOU SHOULD NOT COMMIT THIS FILE - IT'S IN THE GITIGNORE SO THIS HOPEFULLY DOESN'T HAPPEN!

## Running The Script

`python main.py`

