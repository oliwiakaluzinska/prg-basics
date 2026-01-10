class Music:
    def __init__(self,artist, track_title, album, year):
      self.artist = artist
      self.track_title = track_title
      self.album = album
      self.year = year

    def __str__(self):
       return f'{self.artist},\n{self.track_title},\n{self.album},\n{self.year}'
    
def main():
   song1 = Music('Ed Sheeran',"Hearts Don't Break Around Here","Divide",2017)
   print(song1)

main()
