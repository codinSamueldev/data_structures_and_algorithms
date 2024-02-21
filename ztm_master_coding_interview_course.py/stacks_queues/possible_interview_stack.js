/* 
  LIFO - Last In First Out.
  This comment describes the nature of the data structure being implemented, indicating that it follows the Last In First Out principle.

  En este ejercicio, se solicita implementar una playlist utilizando un stack en JavaScript.

  Se debe crear la clase Playlist con las siguientes propiedades: 
  top, bottom y length, para representar el tope, la base y la longitud de la pila, respectivamente.

  La clase Playlist debe tener los siguientes métodos:
  addSong(song): 
  Este método permite agregar una canción a la pila. La canción se agrega en el tope de la pila.

  playSong(): 
  Este método permite reproducir la canción que se encuentra en el tope de la pila y luego eliminarla. 
  Si la pila está vacía, se debe lanzar un error con el mensaje "No hay canciones en la lista".

  getPlaylist(): 
  Este método transforma la pila en una lista (array) que contiene todas las canciones en orden de reproducción, 
  desde la última agregada hasta la primera.


  Ejemplo 1:

  playlist = Playlist()

  playlist.addSong("Bohemian Rhapsody")
  playlist.addSong("Stairway to Heaven")
  playlist.addSong("Hotel California")

  print(playlist.playSong()) # Expected output: "Hotel California"

  print(playlist.getPlaylist()) 

  Output: ["Hotel California", "Stairway to Heaven", "Bohemian Rhapsody"]
*/

class Node {
  constructor(value) {
    this.value = value; 
    this.next = null;
  }
}


class Playlist {
  constructor() {
    this.top = null;
    this.bottom = null;
    this.length = 0;
  }


  addSong(song) {
    /* Add songs to the playlist. Time complexity O(1). */

    const newSong = new Node(song); // Creates a new Node instance with the provided song value.

    if (!this.top) {
      // If the stack is empty, sets both top and bottom to the new node.
      this.top = newSong;
      this.bottom = newSong;
    } else {
      // If the stack is not empty, assigns the current top node as the next node of the new node.
      newSong.next = this.top;
      this.bottom = this.top.next; // Updates the bottom node to the next node of the current top node.
      this.top = newSong;
    }

    this.length++;
  }


  playSong() {
    /* Reproduce and remove song from the playlist. Time complexity O(1). */

    if (!this.top && this.bottom) {
      this.bottom = null;
      throw new Error("No hay canciones en la lista");
    } else {
      console.log(this.top.value);
      this.top = this.top.next; // Moves the top pointer to the next song in the playlist.
    }

    this.length--;
  }

  getPlaylist() {
    let iterator = this.top;
    const playlistArray = [];

    while (iterator) {
      playlistArray.push(iterator.value);
      iterator = iterator.next;
    }

    return playlistArray; // Returns the array containing all songs in the playlist.
  }
}


/* Example usage. */
const spotify = new Playlist(); // Instantiates a new Playlist object named spotify.

// Adds a song to the playlist.
spotify.addSong("Bohemian Rhapsody");
spotify.addSong("Stairway to Heaven");
spotify.addSong("Hotel California");

// Plays the top song in the playlist.
spotify.playSong();

// Outputs the current playlist.
console.log(spotify.getPlaylist());
