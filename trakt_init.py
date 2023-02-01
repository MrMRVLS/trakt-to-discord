#--GitHub.com/░█▀▄▀█ █▀▀█ ░█▀▄▀█ ░█▀▀█ ░█──░█ ░█─── ░█▀▀▀█--
#--------─────░█░█░█ █▄▄▀ ░█░█░█ ░█▄▄▀ ─░█░█─ ░█─── ─▀▀▀▄▄--
#---────---──-░█──░█ ▀─▀▀ ░█──░█ ░█─░█ ──▀▄▀─ ░█▄▄█ ░█▄▄▄█--
#--──-----──---------────-------──---──────-----------------

from sys import argv
import config
import trakt

if len(argv) != 1:

    print("Usage: $ python trakt_init.py")
else:
    username = config.username

    trakt.core.AUTH_METHOD=trakt.core.OAUTH_AUTH

    trakt.init(username, store=True)