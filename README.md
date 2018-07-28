### Warning
This is just a prototype, well prototypes are meant to be thrown away.
But I'm to lazy right now.
Also it is not well tested and there is actually no exception handling in the whole code, and obviously a lot of things going to change over time.

In conclusion it is quick and dirty, but don't use it in "production".

Also I would like to thank spice a wrapper for the MAL API, which i got a lot of inspiration from.
### How to install:
Download the wheel-file:

Install using pip:
`pip install np_api*.whl`
### Example:
```python
from np_api import npApi

# Create an instance
np = npApi()

# yieldTags _sort= True -> Popular | _sort = False -> Alphabetical
# Please use this only if you want to fetch all available tags and then save it.
for tag in np.yieldGroups(_sort=False):
  print(tag)  # {"name": **, "count": **, "id": ** }

# Same for groups:
np.yieldGroups()
# Artists
np.yieldArtists()
# Characters
np.yieldCharacters()
# Parodies
np.yieldParodies()


# Next up you can pick a random one
medium = np.pickRandom()

# Thats a good example of introducing the Medium which has several attributes:
print(medium.id)              # Id of the medium
print(medium.mediaID)         # Id of the media, I don't know why there are two, but with this id you can search it
print(medium.title)           # A dict with titles of the media for example: {'japanese': '**', 'pretty': '**', 'english': '***'}
print(medium.uploadDate)      # The uploaddateof the medium. Example: jjjj-mm-dd hh:mm:ss
print(medium.cover)           # dictionary with url of the cover and picture information. Example: {'h': **, 't': '*', 'w': **, 'url': '**'}
print(medium.thumbnail)       # dictionary with url of the thumbnail and picture information. Example: {'h': **, 't': '*', 'w': **, 'urls': '**'}
print(medium.numberPages)     # Number of Pages from the medium
print(medium.numberFavorites) # Number of marked favorites
print(medium.pages)           # List with Page urls (pictures) and picture information. Example: [{'h': **, 't': '*', 'w': **}, {'h': **, 't': '*', 'w': **}, {'urls': ['**', '**', ....]}]
print(medium.tags)            # List with all tags of this medium. Example: [{'name': '***', 'count': **, 'id': **}, {'name': '***', 'count': **, 'id': **}, ...]
print(medium.characters)       # List with all characters of this medium. Example: same as above
print(medium.artists)          # List with all artists of this medium. Example: same as above
print(medium.groups)          # List with all groups of this medium. Example: same as above
print(medium.parodies)        # List with all parodies of this medium. Example: same as above
print(medium.language)        # List with all languages of this medium. Example:
print(medium.categories)      # List with all categories of this medium. Example:
print(medium)                 # String representation of this medium. Prints english title or first item in dic

# Or you can perform a search explicit with id:
medium = np.searchExplicitWithID(123)
print(medium)

# Performing a normal search, we got you:
# Note: all parameters are optional.
query = np.search(title=None, characters=[], parodies=["sword art online"], artist=[], groups=[],
                    tags=["monster", "demon"], sort=True)

for medium in query:
    print(medium)

# Well nothing to say you can explicity search for tags etc. only
query = np.search(tags=["monster", "demon"])

for medium in query:
    print(medium)

# You can even exclude with "-"
query = np.search(tags=["monster", "-demon"])

for medium in query:
    print(medium)

```

### Things TODO:
* correct naming
* documentation
* testing
* page_start and page_end in searching
* a query class
