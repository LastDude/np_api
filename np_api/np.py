import grequests
from . import Constants
from . import helper
import requests
import json
from . import objects


class np_api:
    """
    Main-module for using API
    
    
    """

    def __init__(self):
        pass

    def yieldTag(self, sort=False):
        """
        returns a generator of tag elements.
        """
        generator = helper.getList(Constants.Affiliation.TAG, sort)
        for x in generator:
            yield x

    def yieldGroup(self, sort=False):
        """
        returns a generator of group elements.
        """
        generator = helper.getList(Constants.Affiliation.GROUP, sort)
        for x in generator:
            yield x

    def yieldArtist(self, sort=False):
        """
        returns a generator of artist elements.
        """
        generator = helper.getList(Constants.Affiliation.ARTIST, sort)
        for x in generator:
            yield x

    def yieldCharacter(self, sort=False):
        """
        returns a generator of character elements.
        """
        generator = helper.getList(Constants.Affiliation.CHARACTER, sort)
        for x in generator:
            yield x

    def yieldParodie(self, sort=False):
        """
        returns a generator of parodies elements.
        """
        generator = helper.getList(Constants.Affiliation.PARODIE, sort)
        for x in generator:
            yield x

    def pickRandom(self):
        """
        returns a random picked element
        """
        random = requests.head(Constants.RANDOM_URL, allow_redirects=True)
        return helper.createMedium(random.url.split("/")[-2])

    def search(self, title=None, characters=[], parodies=[], artist=[], groups=[], tags=[],
               sort=False):
        """
        returns a generator of a search query
        """

        sorting = "date"
        query = Constants.QUERY_URL
        if title is not None:
            query += title + " "
        if characters:
            query += "character:" + " ".join(characters) + " "
        if parodies:
            query += "parodies:" + " ".join(parodies) + " "
        if artist:
            query += "artist:" + " ".join(artist) + " "
        if groups:
            query += "group:" + " ".join(groups) + " "
        if tags:
            query += "tags:" + " ".join(tags) + " "
        if sort:
            sorting = "popular"
        query = query[0:-1]

        queryPages = query + "&page=" + "1" + "&sort=" + sorting
        result = requests.get(queryPages).text
        jresult = json.loads(result)
        lastPage = int(jresult["num_pages"])
        urls = [(query + "&page=" + str(i) + "&sort=" + sorting)
                for i in range(2, lastPage + 1)]
        if not jresult["result"]:
            return
        for element in jresult["result"]:
            yield objects.Medium(element)
        rs = (grequests.get(u) for u in urls)
        generator = grequests.imap(rs, stream=True)
        for page in generator:
            result = page.text
            jresult = json.loads(result)
            if not jresult["result"]:
                return
            for element in jresult["result"]:
                yield objects.Medium(element)

    def searchExplicitWithID(self, id):
        """
        gets Medium with explicit ID
        """
        return helper.createMedium(str(id))
