/*
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
*/


class PatientNode {
    constructor (name, age, bedNumber) {
        this.name = name
        this.age = age
        this.bedNumber = bedNumber
        this.next = null
    }
}


class PatientList {
    constructor (maxBeds){
        this.maxBeds = maxBeds
        this.bedsAvailable = []
        for (let index = 0; index < maxBeds; index++) {this.bedsAvailable.push(index + 1)}
        this.head = null
        this.tail = null
    }

    addPatient (name, age) {
        
        try {
            if (this.bedsAvailable[0] == undefined) {
                throw new Error()
            }

            const NEW_PATIENT = new PatientNode(name, age, this.bedsAvailable[0]);
            if (this.head === null) {
                this.head = NEW_PATIENT;
                this.tail = NEW_PATIENT;
                this.bedsAvailable.splice(0, 1);
            } else {
                this.tail.next = NEW_PATIENT;
                this.tail = NEW_PATIENT;
                this.bedsAvailable.splice(0, 1);
            }
        } catch (error) {
            console.error("Error:", error);
            throw new Error("No hay camas disponibles");
        }
    }


    removePatient (name) {
        let currentPatient = this.head
        let previousPatient = currentPatient

        while (currentPatient != null) {

            if (currentPatient.name === name){
                this.bedsAvailable.push(currentPatient.bedNumber)
                previousPatient.next = currentPatient.next
                return
            }
            
            previousPatient = currentPatient
            currentPatient = currentPatient.next
        }

        throw new Error("Paciente no encontrado")
    }


    getPatient (name) {
        let currentPatient = this.head

        while (currentPatient != null) {

            if (currentPatient.name === name){
                return {"name": currentPatient.name, "age": currentPatient.age, "bedNumber": currentPatient.bedNumber}
            }
            
            currentPatient = currentPatient.next
        }
        
        throw new Error("Paciente no encontrado")
    }


    getPatientList () {
        let iterator = this.head
        const patients_array = []
        
        while (iterator !== null) {
            patients_array.push({"name": iterator.name, "age": iterator.age, "bedNumber": iterator.bedNumber})

            iterator = iterator.next
        }
        return patients_array
    }


    getAvailableBeds () {return this.bedsAvailable.length}
}


/* Example usage */
medicalCare = new PatientList(3)

medicalCare.addPatient("Samuel", 18)
medicalCare.addPatient("Brenda", 18)
medicalCare.addPatient("Rice", 18)

medicalCare.getPatient("Rice")

medicalCare.removePatient("Rice")

medicalCare.getAvailableBeds()


console.log(medicalCare.getPatientList());

