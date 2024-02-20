"""
En este ejercicio, se solicita implementar una playlist utilizando un stack en Python.

Se debe crear la clase Playlist con las siguientes propiedades: top, bottom y length, para representar el tope, la base y la longitud de la pila, respectivamente.

La clase Playlist debe tener los siguientes métodos:

addSong(song): Este método permite agregar una canción a la pila. La canción se agrega en el tope de la pila.

playSong(): Este método permite reproducir la canción que se encuentra en el tope de la pila y luego eliminarla. 
Si la pila está vacía, se debe lanzar un error con el mensaje "No hay canciones en la lista".

getPlaylist(): Este método transforma la pila en una lista (array) que contiene todas las canciones en orden de reproducción, desde la última agregada hasta la primera.


Ejemplo 1:

playlist = Playlist()

playlist.addSong("Bohemian Rhapsody") playlist.addSong("Stairway to Heaven") playlist.addSong("Hotel California")

Output: print(playlist.playSong()) # Output: "Hotel California" print(playlist.playSong()) # Output: "Stairway to Heaven" print(playlist.playSong()) # Output: "Bohemian Rhapsody" print(playlist.playSong()) # Output: Error: No hay canciones en la lista ``` Ejemplo 2:

Input:

playlist = Playlist()

playlist.addSong("Bohemian Rhapsody")
playlist.addSong("Stairway to Heaven")
playlist.addSong("Hotel California")

print(playlist.getPlaylist()) 

Output: ["Hotel California", "Stairway to Heaven", "Bohemian Rhapsody"]
"""

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
  

class Playlist:
  def __init__(self):
    self.top = None
    self.bottom = None
    self.length = 0
    

  def addSong(self, song):
    NEW_SONG = Node(value=song)

    if self.top is None:
      self.top = NEW_SONG
      self.bottom = NEW_SONG
    else:
      NEW_SONG.next = self.top
      self.bottom = self.top.next
      self.top = NEW_SONG

    self.length += 1


  def playSong(self):
    if self.top is None and self.bottom:
      self.bottom = None
      raise Exception("No hay canciones en la lista")
    else:
        print(self.top.value)
        self.top = self.top.next


  def getPlaylist(self):

    iterator = self.top
    playlist_array = list()

    while iterator is not None:
      playlist_array.append(iterator.value)
      
      iterator = iterator.next

    return playlist_array

  

if __name__ == '__main__':
  spotify = Playlist()

  spotify.addSong("Bohemian Rhapsody")
  spotify.addSong("Stairway to Heaven")
  spotify.addSong("Hotel California")

  """
  spotify.playSong()
  spotify.playSong()
  """

  print(spotify.getPlaylist())
