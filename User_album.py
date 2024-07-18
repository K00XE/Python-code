#applying dictionary with functions
def make_album(artist_name, album_title, number_of_songs = None):
    """return a diction of information about album and artist"""
    details = {'artist': artist_name, 'album': album_title}
    if number_of_songs:
        details['songs'] = number_of_songs
    return details

while True:
    print("\nplease tell me your favorite album including artist.")
    print("(enter 'q' at anytime to quit)")

    a_name = input("Artist name: ")
    if a_name == 'q':
        break

    a_title = input("Album title: ")
    if a_title == 'q':
        break

    new_make_album = make_album( a_name, a_title)
    print(f"Noice {new_make_album} is great.") 