import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "29161424"))
    API_HASH = os.environ.get("API_HASH", "5f5b24e80c36c2b4f20518d54fdd2c6a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5788020712:AAEloTloJMfW3hKVYFf7GG0sgKIF56kMAUY")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQC0P2tXWBFAxdW6lr0KpvdmYfeMSeCCRy8RquONulEInaLQKyKn_Yo0oy3JUUuUgX_-RibCt0lXB3NxjudQl--BS8qoYAIAQx7qTlYtRz2qZIGW0EyPHk4oD0aZR486YUcYJtl7xe6k1nhICoCasEDJZVyeHu2AFiaOZrsgxAmqS8cco6EjNJUXRLDdfxKooxSM6eeyiPXG4LCdJCQajNjZDDjg2tuR3EEPrNcp75kqRZhJAEzBwGQfWHrYZhhSDQ3UFH0XjXj6XfOqP8BgSy8hx04htdj3a5bYIEqO4fi0BoDYsz9OpbbefxRll0c0yrZjC0Bzc7nEGS2fhc4YpXMkAAAAAU3UO8gA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "hobmusic_bot")
    SUPPORT = os.environ.get("SUPPORT", "https://t.me/hobtalkscommunity") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5981767677")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
