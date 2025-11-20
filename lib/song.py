class Song:
    count= 0
    artists = []
    genres = []
    genre_count ={}
    artist_count ={}
    def  __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.all_songs_method()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_artist_count(artist)
        Song.add_to_genre_count(genre)

    @classmethod
    def all_songs_method(cls):
        cls.count +=1
        
    
    @classmethod
    def add_to_genres(cls,genre):
        if genre not in cls.genres:
          cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls , artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else :
            cls.genre_count[genre] = 1
    
    @classmethod 
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else :
            cls.artist_count[artist] = 1

# Song("hid", "aya", "hiphop")
# Song("hid", "aya", "hiphop")
# Song.show_artist_names() 

    
