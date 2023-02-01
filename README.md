# Trakt.tv 'Watching' to → Discord Rich Presence 📺
Update your Discord status based on movies you are watching on Trakt.tv.

- 🖼 Detects what are you playing; a Movie or a TV Show.
- ⭐ Shows the ratings.
- 📌 Shows buttons to the IMDB page and your Trakt profile.

<p align="left"> <img src="assets/rpc.png" height="25%" width="25%" alt="MrMRVLS" /> </p>

## Requirements 🧰
- [Trakt.tv](https://trakt.tv/) account (ofc ☘😏)
- [Python 3+](https://www.python.org/)
- [Discord](https://discord.com/) client for RPC connectivity. 

## Installation 🐍

```
> download a copy of this repo
> navigate to the extracted folder
```

Install all the necessary Python packages to run this programme using the requirements.txt (`sudo` as neccessary):

```
$ pip install -r requirements.txt
```

---

## Getting Started 🥣
Change the `username` in `config.py` to your trakt username. 

```py
username = "MrMRVLS"
```
---

Create a Trakt [API](https://trakt.tv/oauth/applications) App named `Discord` and set the following Redirect URI for OAuth:

```urn:ietf:wg:oauth:2.0:oob```

Record the **Client ID** and **Client Secret** for initializing the Trakt API module. Using this information and your **Trakt username**, run `trakt_init.py`, receive the PIN from Trakt at the end of the process. _(requires sign-in)_

```
$ python trakt_init.py

- Please enter your client id: <client id>
- Please enter your client secret: <client secret>
- Please go here and authorize, https://api-v2launch.trakt.tv/oauth/authorize?response_type=code&...
- Paste the Code returned here: <trakt code>
```

This will cause Trakt API information to be stored in `~/.pytrakt.json` for future reference.

---
## Usage 🍕
### Then run the code: WoWoWo!!! 🍻
```
 $ python discord.py
```
If you did all the steps correctly, you should see the following message on the console.

````
Successfully connected with the Server!
Trakt: not playing.
````
---
_**Do you have an improvement? Feel free to contribute by a pull request.**_ 🤍