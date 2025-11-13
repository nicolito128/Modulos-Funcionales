import db.methods as dbm
import gui2

# Programa principal que junta al resto de los modulos
def main():
    dbm.migraciones()
    gui2.start_gui()

# Llama a la función main sólo si es ejecutado como script principal (`python src/main.py`)
if __name__ == "__main__":
    main()
