APLICACIÓN

eventos_multideportivos.py

from models import Participante, Disciplina, Evento, Encuentro
from database import connect_db, create_tables
from relations import define_relations
from utils import insert_sample_data, validate_data

def main():
    db = connect_db()
    create_tables(db)
    define_relations(db)
    insert_sample_data(db)
    # Lógica principal de la aplicación
    print("Aplicación iniciada correctamente")

if __name__ == "__main__":
    main()

