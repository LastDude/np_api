import grequests
from . import Constants
from . import objects
from bs4 import BeautifulSoup
import requests
"""
Provides helper methods for parsing and using the unofficial api.
"""


def createMedium(_id):
    """
    creates a Medium from provided _id
    """
    result = requests.get(Constants.API_CALL_ID + _id)
    return objects.Medium(result.text)


def getLists(affiliations, _sorted=False):
    """
    creates a generator for receiving.
    """
    strategie = None
    if affiliations == Constants.Affiliations.TAGS:
        strategie = TagStrategie(_sorted)
    elif affiliations == Constants.Affiliations.ARTISTS:
        strategie = ArtistStrategie(_sorted)
    elif affiliations == Constants.Affiliations.CHARACTERS:
        strategie = CharacterStrategie(_sorted)
    elif affiliations == Constants.Affiliations.PARODIES:
        strategie = ParodieStrategie(_sorted)
    elif affiliations == Constants.Affiliations.GROUPS:
        strategie = GroupStrategie(_sorted)
    else:
        raise TypeError
    generator = strategie.getLists()
    for entry in generator:
        text = entry.text.rsplit(' ', 1)
        yield {Constants.NAME: text[0], Constants.COUNT: text[1][1:-1],
               Constants.ID: entry[Constants.CLASS][1][4:]}


class AbstractStrategie:
    """
    Uses Strategie Pattern to get list of Constants.Affiliations types
    """
    def __init__(self, _sorted):
        self._sorted = _sorted

    def getLists(self):
        """
        Schablonenmethode for providing the generator
        """
        site = self.getFirstSite()
        results, lastPage = self.parsingSite(site, first=True)
        urls = self.createUrls(lastPage)
        for x in results:
            yield x
        rs = (grequests.get(u) for u in urls)
        generator = grequests.imap(rs, stream=True)
        for entry in generator:
            for x in self.parsingSite(entry):
                yield x

    def parsingSite(self, site, first=False):
        """
        Parsing site informations
        """
        if first:
            soup = BeautifulSoup(site.text, Constants.LXML)
            results = soup.select(Constants.SELECT_TAG)
            lastPage = int(soup.select(Constants.SELECT_LAST_PAGE)[
                           0][Constants.HREF][6:])
            return (results, lastPage)
        else:
            soup = BeautifulSoup(site.text, Constants.LXML)
            results = soup.select(Constants.SELECT_TAG)
            return results


class TagStrategie(AbstractStrategie):
    """
    Strategie for getting tags
    """
    def __init__(self, _sorted):
        super().__init__(_sorted)

    def getFirstSite(self):
        if self._sorted:
            return requests.get(Constants.TAGS_URL_SORTED + str(1))
        else:
            return requests.get(Constants.TAGS_URL + str(1))

    def createUrls(self, lastPage):
        if self._sorted:
            return [(Constants.TAGS_URL_SORTED + str(i)) for i in range(2, lastPage + 1)]
        else:
            return [(Constants.TAGS_URL + str(i)) for i in range(2, lastPage + 1)]


class ArtistStrategie(AbstractStrategie):
    """
    Strategie for getting artists
    """
    def __init__(self, _sorted):
        super().__init__(_sorted)

    def getFirstSite(self):
        if self._sorted:
            return requests.get(Constants.ARTISTS_URL_SORTED + str(1))
        else:
            return requests.get(Constants.ARTISTS_URL + str(1))

    def createUrls(self, lastPage):
        if self._sorted:
            return [(Constants.ARTISTS_URL_SORTED + str(i)) for i in range(2, lastPage + 1)]
        else:
            return [(Constants.ARTISTS_URL + str(i)) for i in range(2, lastPage + 1)]


class CharacterStrategie(AbstractStrategie):
    """
    Strategie for getting characters
    """
    def __init__(self, _sorted):
        super().__init__(_sorted)

    def getFirstSite(self):
        if self._sorted:
            return requests.get(Constants.CHARACTERS_URL_SORTED + str(1))
        else:
            return requests.get(Constants.CHARACTERS_URL + str(1))

    def createUrls(self, lastPage):
        if self._sorted:
            return [(Constants.CHARACTERS_URL_SORTED + str(i)) for i in range(2, lastPage + 1)]
        else:
            return [(Constants.CHARACTERS_URL + str(i)) for i in range(2, lastPage + 1)]


class ParodieStrategie(AbstractStrategie):
    """
    Strategie for getting parodies
    """
    def __init__(self, _sorted):
        super().__init__(sorted)

    def getFirstSite(self):
        if self._sorted:
            return requests.get(Constants.PARODIES_URL_SORTED + str(1))
        else:
            return requests.get(Constants.PARODIES_URL + str(1))

    def createUrls(self, lastPage):
        if self._sorted:
            return [(Constants.PARODIES_URL_SORTED + str(i)) for i in range(2, lastPage + 1)]
        else:
            return [(Constants.PARODIES_URL + str(i)) for i in range(2, lastPage + 1)]


class GroupStrategie(AbstractStrategie):
    """
    Strategie for getting groups
    """
    def __init__(self, _sorted):
        super().__init__(_sorted)

    def getFirstSite(self):
        if self._sorted:
            return requests.get(Constants.GROUPS_URL_SORTED + str(1))
        else:
            return requests.get(Constants.GROUPS_URL + str(1))

    def createUrls(self, lastPage):
        if self._sorted:
            return [(Constants.GROUPS_URL_SORTED + str(i)) for i in range(2, lastPage + 1)]
        else:
            return [(Constants.GROUPS_URL + str(i)) for i in range(2, lastPage + 1)]
