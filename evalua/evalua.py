import pandas as pd
from dbs.dbs import save_response


def creaToTest(ficha, aprendiz, instructores):
    instructores_to_test = []
    for instructor in instructores:
        data = {
            "FICHA": ficha,
            "PROGFORMACION": instructor['PROGRAMA_DE_FORMACION'],
            "DOCAPRENDIZ": aprendiz['NUMERO_DOCUMENTO'],
            "APRENDIZ_NAME": aprendiz['NOMBRES'],
            "APRENDIZ_LAST": aprendiz['APELLIDOS'],
            "DOCINSTRUCTOR": instructor['NUMERO_DOCUMENTO'],
            "INSTRUCTOR_NAME": instructor['NOMBRES'],
            "INSTRUCTOR_LAST": instructor['APELLIDOS'], 
        }
        instructores_to_test.append(data)
    instructores_to_test = pd.DataFrame(instructores_to_test)
    save_response(instructores_to_test, 'ToTest')
