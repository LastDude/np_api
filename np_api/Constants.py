from enum import Enum
"""
Some constants used in the programm
"""

# URLS
TAGS_URL = "https://nhentai.net/tags/?page="
TAGS_URL_SORTED = "https://nhentai.net/tags/popular?page="

ARTISTS_URL = "https://nhentai.net/artists/?page="
ARTISTS_URL_SORTED = "https://nhentai.net/artists/popular?page="

CHARACTERS_URL = "https://nhentai.net/characters/?page="
CHARACTERS_URL_SORTED = "https://nhentai.net/character/popular?page="

PARODIES_URL = "https://nhentai.net/parodies/?page="
PARODIES_URL_SORTED = "https://nhentai.net/parodies/popular?page="

GROUPS_URL = "https://nhentai.net/groups/?page="
GROUPS_URL_SORTED = "https://nhentai.net/groups/popular?page="

RANDOM_URL = "https://nhentai.net/random/"

API_CALL_ID = "https://nhentai.net/api/gallery/"
PICTURE_URL = "https://i.nhentai.net/galleries/"
THUMB_COVER_URL = "https://t.nhentai.net/galleries/"

QUERY_URL = "https://nhentai.net/api/galleries/search?query="

# Propertys
ENGLISH = "english"
MEDIA_ID = "media_id"
ID = "id"
TITLE = "title"
UPLOAD_DATE = "upload_date"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
IMAGES = "images"
COVER = "cover"
URL = "url"
URLS = "urls"
PAGES = "pages"
THUMBNAIL = "thumbnail"
NUMBER_FAVORITES = "num_favorites"
NUMBER_PAGES = "num_pages"
TAGS = "tags"
TYPE = "type"
NAME = "name"
COUNT = "count"
TAG = "tag"
CHARACTER = "character"
ARTIST = "artist"
GROUP = "group"
PARODY = "parody"
LANGUAGE = "language"
CATEGORY = "category"

# CSS
CLASS = "class"
SELECT_TAG = "a.tag"
SELECT_LAST_PAGE = "a.last"
HREF = "href"
# DATA
LXML = "lxml"


class Affiliations(Enum):
    TAGS = 1
    ARTISTS = 2
    CHARACTERS = 3
    PARODIES = 4
    GROUPS = 5
