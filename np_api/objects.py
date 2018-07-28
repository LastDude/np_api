from . import Constants
import logging
import json
import datetime


class Medium:
    """
    A Medium consists out of these attributes which can be get infos from:
     - id
     - mediaID
     - title
     - characters
     - parodies
     - artist
     - groups
     - tags
     - language
     - categorie
     - thumbnail
     - cover
     - numberPages
     - pages
     - uploadDate
     - numberFavorites
     Note: Data is dynamically loaded when needed.

    """

    def __init__(self, medium_data):
        if isinstance(medium_data, dict):
            self._rawData = medium_data
            logging.debug("medium_data already in dict-Format")
        else:
            self._rawData = json.loads(medium_data)
            logging.debug("medium_data not in json-Format")
        self._id = None
        self._mediaID = None
        self._title = None
        self._characters = None
        self._parodies = None
        self._artist = None
        self._groups = None
        self._tags = None
        self._language = None
        self._categorie = None
        self._thumbnail = None
        self._cover = None
        self._numberPages = None
        self._pages = None
        self._uploadDate = None
        self._numberFavorites = None

    @property
    def mediaID(self):
        """
        returns the mediaID
        """
        if self._mediaID is None:
            self._mediaID = self._rawData[Constants.MEDIA_ID]
            logging.debug("Set mediaID: %s", self._mediaID)
        return self._mediaID

    @property
    def id(self):
        """
        returns the id
        """
        if self._id is None:
            self._id = self._rawData[Constants.ID]
            logging.debug("Set id: %s", self._id)
        return self._id

    @property
    def title(self):
        """
        returns the title
        """
        if self._title is None:
            self._title = self._rawData[Constants.TITLE]
            logging.debug("Set title: %s", self._title)
        return self._title

    @property
    def uploadDate(self):
        """
        returns the uploadDate
        """
        if self._uploadDate is None:
            self._uploadDate = datetime.datetime.fromtimestamp(
                int(self._rawData[Constants.UPLOAD_DATE])).strftime(Constants.DATE_FORMAT)
            logging.debug("Set uploadDate: %s", self._uploadDate)
        return self._uploadDate

    @property
    def cover(self):
        """
        returns cover informations
        """
        if self._cover is None:
            self._cover = self._rawData[Constants.IMAGES][Constants.COVER]
            if self._cover["t"] == "j":
                self._cover[Constants.URL] = Constants.THUMB_COVER_URL + \
                    self.mediaID + "/cover.jpg"
            else:
                self._cover[Constants.URL] = Constants.THUMB_COVER_URL + \
                    self.mediaID + "/cover.png"
            logging.debug("Set cover: %s", self._cover)
        return self._cover

    @property
    def pages(self):
        """
        returns page informations
        """
        if self._pages is None:
            x = []
            for i in range(0, self.numberPages):
                if self._rawData[Constants.IMAGES][Constants.PAGES][i]["t"] == "j":
                    x.append(Constants.PICTURE_URL + self.mediaID
                                + "/" + str(i + 1) + ".jpg")
                else:
                    x.append(Constants.PICTURE_URL + self.mediaID
                                + "/" + str(i + 1) + ".png")
            self._pages = [{Constants.URLS: x}]
            self._pages.append(
                self._rawData[Constants.IMAGES][Constants.PAGES])
            logging.debug("Set pages")
        return self._pages

    @property
    def thumbnail(self):
        """
        returns thumbnail informations
        """
        if self._thumbnail is None:
            self._thumbnail = self._rawData[Constants.IMAGES][Constants.THUMBNAIL]
            if self._thumbnail["t"] == "j":
                self._thumbnail[Constants.URLS] = Constants.THUMB_COVER_URL + \
                    self.mediaID + "/thumb.jpg"
            else:
                self._thumbnail[Constants.URLS] = Constants.THUMB_COVER_URL + \
                    self.mediaID + "/thumb.png"
            logging.debug("Set thumbnail: %s", self._thumbnail)
        return self._thumbnail

    @property
    def numberFavorites(self):
        """
        returns the number of favorites
        """
        if self._numberFavorites is None:
            self._numberFavorites = int(
                self._rawData[Constants.NUMBER_FAVORITES])
            logging.debug("Set number of Favorites: %s", self._numberFavorites)
        return self._numberFavorites

    @property
    def numberPages(self):
        """
        returns the number of pages
        """
        if self._numberPages is None:
            self._numberPages = int(self._rawData[Constants.NUMBER_PAGES])
            logging.debug("Set number of Pages: %s", self._numberPages)
        return self._numberPages

    def getInfos(self, type):
        """
        helper method to get informations out of the json
        """
        result = []
        x = self._rawData[Constants.TAGS]
        for entry in x:
            if entry[Constants.TYPE] == type:
                result.append(
                    {Constants.NAME: entry[Constants.NAME], Constants.COUNT: entry[Constants.COUNT],
                        Constants.ID: entry[Constants.ID]})
        return result

    @property
    def tags(self):
        """
        returns tag informations
        """
        if self._tags is None:
            self._tags = self.getInfos(type=Constants.TAG)
            logging.debug("Set tags")
        return self._tags

    @property
    def characters(self):
        """
        returns character informations
        """
        if self._characters is None:
            self._characters = self.getInfos(type=Constants.CHARACTER)
            logging.debug("Set characters")
        return self._characters

    @property
    def artists(self):
        """
        returns artists information
        """
        if self._artist is None:
            self._artist = self.getInfos(type=Constants.ARTIST)
            logging.debug("Set artists")
        return self._artist

    @property
    def groups(self):
        """
        returns groups information
        """
        if self._groups is None:
            self._groups = self.getInfos(type=Constants.GROUP)
            logging.debug("Set groups")
        return self._groups

    @property
    def parodies(self):
        """
        returns parodies information
        """
        if self._parodies is None:
            self._parodies = self.getInfos(type=Constants.PARODY)
            logging.debug("Set parodies")
        return self._parodies

    @property
    def language(self):
        """
        returns language information
        """
        if self._language is None:
            self._language = self.getInfos(type=Constants.LANGUAGE)
            logging.debug("Set language")
        return self._language

    @property
    def categories(self):
        """
        returns categories information
        """
        if self._categorie is None:
            self._categorie = self.getInfos(type=Constants.CATEGORY)
            logging.debug("Set categories")
        return self._categorie

    def __str__(self):
        """
        returns the title, if available in english else the first title which is provided
        """
        print(Constants.ENGLISH)
        if self.title[Constants.ENGLISH]:
            return self._title[Constants.ENGLISH]
        else:
            return self._title[0]
