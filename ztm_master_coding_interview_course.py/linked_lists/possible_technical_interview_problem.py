"""
En este desafío, vamos a implementar una lista enlazada simple para almacenar información sobre pacientes de un hospital. 
Cada nodo de la lista representará a un paciente y tendrá los siguientes campos:
Nombre del paciente (cadena de texto)
Edad del paciente (número)
Número de cama asignada al paciente (número)

La lista enlazada deberá tener los siguientes métodos:

addPatient(name, age): 
agrega un nuevo paciente a la lista, asignándole la próxima cama disponible. 
Si no hay camas disponibles, debe lanzar un error con el mensaje "No hay camas disponibles".

removePatient(name): 
remueve al paciente con el nombre especificado de la lista y libera su cama. 
Si el paciente no se encuentra en la lista, debe lanzar un error con el mensaje "Paciente no encontrado".

getPatient(name): 
retorna la información del paciente con el nombre especificado en el siguiente formato {name, age, bedNumber}. 
Si el paciente no se encuentra en la lista, debe lanzar un error con el mensaje "Paciente no encontrado".

getPatientList(): 
retorna una lista con la información de todos los pacientes en la lista, cada paciente deberá tener el siguiente formato {name, age, bedNumber}.

getAvailableBeds(): 
retorna un número con el total de camas disponibles.

Recuerda usar la sintaxis raise Exception("mensaje") para lanzar errores.

Aquí tienes un ejemplo de cómo se utilizaría esta singly linked list:


list = PatientList(3)
list.addPatient("Paciente 1", 20)
list.addPatient("Paciente 2", 30)

list.getPatientList()

Output:

[
  { 'name': 'Paciente 1', 'age': 20, 'bedNumber': 1 },
  { 'name': 'Paciente 2', 'age': 30, 'bedNumber': 2 }
]

list.getPatient("Paciente 1")

Output:

{ 'name': 'Paciente 1', 'age': 20, 'bedNumber': 1 }

list.removePatient("Paciente 1")

list.getPatientList()

Output:

[
  { 'name': 'Paciente 2', 'age': 30, 'bedNumber': 2 },
]
"""

class PatientNode:
  def __init__(self, name, age, bed_number):
    self.name = name
    self.age = age
    self.bed_number = bed_number
    self.next = None
    


class PatientList:
  def __init__(self, max_beds):
    self.max_beds = max_beds
    self.beds_available = [number + 1 for number in range(max_beds)]
    self.head = None
    self.tail = self.head


  def addPatient(self, name, age) -> None | Exception:
    
    try:
        NEW_PATIENT = PatientNode(name, age, self.beds_available[0])

        if self.head is None:
            self.head = NEW_PATIENT
            self.tail = NEW_PATIENT
            del self.beds_available[0]
        else:
            self.tail.next = NEW_PATIENT
            self.tail = NEW_PATIENT
            del self.beds_available[0]
    except:
      raise Exception("No hay camas disponibles")
    

  def removePatient(self, name):
    current_patient = self.head

    while current_patient is not None:
      if current_patient.name == name:
        self.beds_available.append(current_patient.bed_number)
        previous_patient.next = current_patient.next
        return
    
      previous_patient = current_patient
      current_patient = current_patient.next

    raise Exception("Paciente no encontrado")


  def getPatient(self, name):
    current_patient = self.head

    while current_patient is not None:
      if current_patient.name == name:
        return {"name": current_patient.name, "age": current_patient.age, "bedNumber": current_patient.bed_number}
    
      current_patient = current_patient.next

    raise Exception("Paciente no encontrado")
    

  def getPatientList(self) -> list:
    iterator = self.head
    patients_array = list()

    while iterator is not None:
      patients_array.append({"name": iterator.name, "age": iterator.age, "bedNumber": iterator.bed_number})

      iterator = iterator.next

    return patients_array
    

  def getAvailableBeds(self): return len(self.beds_available)
  

if __name__ == '__main__':
  medical_care = PatientList(3)

  medical_care.addPatient("Samuel", 187)
  medical_care.addPatient("Lewandoski", 36)
  medical_care.addPatient("Brenda", 90)

  medical_care.removePatient("Lewandoski")
  print(medical_care.getPatient("Brenda"))
  medical_care.getAvailableBeds()

  # print(medical_care.getPatientList())
