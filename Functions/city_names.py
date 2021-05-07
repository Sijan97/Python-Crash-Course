"""Python Crash Course
By Eric Matthes

Exercises: 8-6 to 8-8"""

# Exercise 8-6
# City Names (Asking user input)
def city_country(name, country):
    """Displays city-country pair."""
    city_details = f"{name}, {country}\n"
    return city_details.title()

while True:
    print("Which city would you visit?")
    print("(Enter 'q' anytime to quit.)")

    city = input("\nName of city: ")
    if city == 'q':
        break

    country = input("Conutry where city is located: ")
    if country == 'q':
        break

    city = city_country(city, country)
    print(city)

# City Names (Without user input)
def city_country2(city, country):
    """Returns a string like 'Santiago, Chille'."""
    return(f"\n{city.title()}, {country.title()}")

# Calling the function
city = city_country2('santiago', 'chille')
print(city)

city = city_country2('kathmandu', 'nepal')
print(city)

# End of exercise 8-6

# Exercise 8-7
# Album
def make_album(artist_name, album_title, tracks=None):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist_name.title(),
        'album': album_title.title(),
        }

    if tracks:
        album_dict['tracks'] = tracks

    return album_dict

album = make_album('linkin park', 'hybrid theory', 12)
print(f"\n{album}")

album = make_album('passenger', 'whispers')
print(album)

album = make_album('michael jackson', 'thriller', 15)
print(album)

# End of exercise 8-7

# Exercise 8-8
# User albums
def user_album(artist_name, album_title, tracks=None):
    """Defining a dictionary that contains information about an album."""
    album_dict = {
        'artist': artist_name.title(),
        'album': album_title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks

    return album_dict

while True:
    print("\n(Enter 'q' anytime to quit.)")

    artist_name = input("Enter artist name: ")
    if artist_name == 'q':
        break

    album_title = input("Enter album title: ") 
    if album_title == 'q':
        break

    album_tracks = input("Number of tracks: ")
    if album_tracks == 'q':
        break
        
    albums = user_album(artist_name, album_title, album_tracks)
    print(albums)

# End of exercise 8-8