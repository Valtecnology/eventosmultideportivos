                                      Integrantes
Nombre: Valeria
Apellido: Ahumada
DNI: 19115140  
Correo: imparable2030@gmail.com
Github: https://github.com/Valtecnology

Nombre: Simón Azul
Apellido: Sánchez Vottero
DNI: 39173576
Correo: simonvottero.95@gmail.com
Github: https:// github.com/simonbleu 

                                       Propuesta 
                                       
 Desarrollar una aplicación que facilite la organización integral de eventos multideportivos.
 Esta herramienta permitirá gestionar a los participantes, agregar diversas disciplinas deportivas y 
 organizar los encuentros,así como los horarios de cada evento de manera eficiente.
 

                                       Nombre

Eventos Multideportivos                                         

                                                                      
                                       Detalle de la Aplicación Modularizada del Proyecto
                                    
Este proyecto está compuesto por varios módulos en Python, cada uno con una responsabilidad específica. 

A continuación, detallamos los archivos .py que forman parte de la aplicación y su funcionalidad:

                                       
                                       Estructura de Archivos .py

1. main.py

2. models.py

3. database.py

4. relations.py
 
5. utils.py


                                        Descripción de los Archivos

main.py

Descripción: Es el punto de entrada principal de la aplicación. Aquí se inicializan los módulos y se gestiona el flujo principal.
Funcionalidad: Configuración inicial, ejecución principal del programa.

models.py

Descripción: Define las clases que representan las entidades del sistema.
Funcionalidad:
Participante: ID Participante, Nombre, Apellido, Edad, Género, Disciplina Deportiva.
Disciplina: ID Disciplina, Nombre Disciplina, Descripción.
Evento: ID Evento, Nombre Evento, Fecha Inicio, Fecha Fin.
Encuentro: ID Encuentro, Fecha Encuentro, Hora Encuentro.

database.py

Descripción: Maneja la conexión y las operaciones con la base de datos.
Funcionalidad: Conexión a la base de datos, ejecución de consultas SQL, gestión de transacciones.

relations.py

Descripción: Define las relaciones y cardinalidades entre las entidades.
Funcionalidad:
Participa (Participante - Evento)
Compite en (Participante - Disciplina Deportiva)
Incluye (Evento - Disciplina Deportiva)
Organiza (Evento - Encuentro)

utils.py

Descripción: Contiene funciones utilitarias y de apoyo que son utilizadas por otros módulos.
Funcionalidad: Funciones comunes como manejo de fechas, validaciones, etc.

                                       
                                       Aplicación
                                       
```
from models import Participante, Disciplina, Evento, Encuentro
from database import connect_db, create_tables
from relations import define_relations
from utils import insert_sample_data, validate_data 

eventos_multideportivos.py

def main():
       db = connect_db()
       create_tables(db)
       define_relations(db)
       insert_sample_data(db)
       # Lógica principal de la aplicación
       print("Aplicación iniciada correctamente")

 if __name__ == "__main__":
    main()


```












