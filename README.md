[![Github All Releases](https://img.shields.io/github/downloads/LastDude/np_api/total.svg)]()

### Warning
This is just a prototype, well prototypes are meant to be thrown away.
But I'm to lazy right now.
Also it is not well tested and there is actually no exception handling in the whole code, and obviously a lot of things going to change over time.

In conclusion it is quick and dirty, but don't use it in "production".

Also I would like to thank spice a wrapper for the MAL API, which i got a lot of inspiration from.

#### Contact:
LetsPlayHansLP@gmail.com

### How to install:
Download the wheel-file:
[releases](https://github.com/LastDude/np_api/releases)

Install using pip:
`pip install np_api*.whl`
### Example:
```python
from np_api import npApi

# Create an instance
np = npApi()

# yieldTags _sort= True -> Popular | _sort = False -> Alphabetical
# Please use this only if you want to fetch all available tags and then save it.
# First 25
i = 0
for tag in np.yieldGroup(sort=False):
  print(tag)  # {"name": **, "count": **, "id": ** }
  if i == 24:
    break
  i+=1

# Same for groups:
np.yieldGroup()
# Artists
np.yieldArtist()
# Characters
np.yieldCharacter()
# Parodies
np.yieldParodie()


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
print(medium.tag)            # List with all tags of this medium. Example: [{'name': '***', 'count': **, 'id': **}, {'name': '***', 'count': **, 'id': **}, ...]
print(medium.character)       # List with all characters of this medium. Example: same as above
print(medium.artist)          # List with all artists of this medium. Example: same as above
print(medium.group)          # List with all groups of this medium. Example: same as above
print(medium.parodie)        # List with all parodies of this medium. Example: same as above
print(medium.language)        # List with all languages of this medium. Example:
print(medium.categorie)      # List with all categories of this medium. Example:
print(medium)                 # String representation of this medium. Prints english title or first item in dic

# Or you can perform a search explicit with id:
medium = np.searchExplicitWithID(123)
print(medium)

# Performing a normal search, we got you:
# Note: all parameters are optional.
query = np.search(title=None, characters=[], parodies=["sword art online"], artist=[], groups=[],
                    tags=["monster", "demon"], sort=True)

# First 25
i = 0
for medium in query:
  print(medium)
  if i == 24:
    break
  i+=1

# Well nothing to say you can explicity search for tags etc. only
query = np.search(tags=["monster", "demon"])

i = 0
for medium in query:
  print(medium)
  if i == 24:
    break
  i+=1

# You can even exclude with "-"
query = np.search(tags=["monster", "-demon"])

# First 25
i = 0
for medium in query:
  print(medium)
  if i == 24:
    break
  i+=1

```

### Things TODO:
* documentation
* testing
* page_start and page_end in searching
* a query class
