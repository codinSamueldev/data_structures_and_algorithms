"""
En este ejercicio, debes implementar la lógica para procesar correos electrónicos en una empresa utilizando una queue, 
donde los correos más antiguos tienen prioridad. 
Para ello, deberás crear una clase llamada Queue para representar la cola de correos electrónicos. 
La clase debe tener los siguientes métodos:

enqueue(from, to, body, subject): Agrega un correo electrónico al final de la cola.

dequeue(): Elimina y devuelve un objeto con las siguientes propiedades: 
{ from, to, body, subject } del correo electrónico más antiguo de la cola.

peek(): Devuelve el correo electrónico más antiguo de la cola sin eliminarlo.
size(): Devuelve la cantidad de correos electrónicos en la cola.
Tendrás una clase Mail ya construida para usarla dentro del desarrollo de tu solución que simulará ser un nodo dentro de la queue.

Ejemplo:

Input:
emailQueue = Queue()

emailQueue.enqueue(
    'jane@ejemplo.com',
    'support@ejemplo.com',
    'No puedo iniciar sesión en mi cuenta',
    'Problema de inicio de sesión'
)

emailQueue.enqueue(
    'joe@ejemplo.com',
    'support@ejemplo.com',
    'Mi pedido no ha llegado todavía',
    'Estado del pedido'
)

email = emailQueue.dequeue()
print(email)

Output:
{
  '
}
"""

class Mail:
  def __init__(self, from_email, to, body, subject):
    self.from_email = from_email
    self.to = to
    self.body = body
    self.subject = subject
    self.next = None


class Queue:
  def __init__(self):
    self.first = None
    self.last = None
    self.length = 0   
    
  
  def enqueue(self, from_email, to, body, subject) -> None:
    """ Add mails to queue. """
    NEW_EMAIL = Mail(from_email=from_email, to=to, body=body, subject=subject)

    if self.first is None:
      self.first = NEW_EMAIL
      self.last = NEW_EMAIL
    else:
      self.last.next = NEW_EMAIL
      self.last = NEW_EMAIL
    
    self.length += 1


  def dequeue(self) -> dict:
    """ Return email object, then remove it from the queue. """
    mail_unwanted = self.first

    self.first = self.first.next
    self.length -= 1

    return {'from': mail_unwanted.from_email, 'to': mail_unwanted.to, 'body': mail_unwanted.body, 'subject': mail_unwanted.subject}  

  
  def peek(self) -> dict:
    """ See which email is the oldest one. """
    return {'from': self.first.from_email, 'to': self.first.to, 'body': self.first.body, 'subject': self.first.subject}


  def is_empty(self) -> bool:
    """ Is the email queue empty? """
    if self.length > 1:
      return False
    else:
      return True
  

  def size(self) -> int:
    """ How many emails do we have queueing. """
    return self.length
  

  def print_out_queue(self) -> str:
    iterator = self.first

    while iterator is not None:
      print(iterator.subject, "-->", end=" ")

      iterator = iterator.next

    return "done."
  

if __name__ == '__main__':
  gmail = Queue()

  gmail.enqueue("messi@worldcup.ar", "cristiano@alnassr.du", "Ché tengo una copa del mundo y vos?", "WORLD CUP")
  gmail.enqueue("cristiano@alnassr.du", "messi@worldcup.ar", "TEngo más champions y voce?", "Salamero")

  gmail.dequeue()

  print(gmail.peek())

  # gmail.print_out_queue()

