from django.db import models

# Create your models here. - ORM: Object Relational Mapper


# Clases: Concepto
# Objetos: Definicion
# 1. Creas/Modificas o Eliminas algun ORM (Modelo)
# 2. Creas una migracion: makemigrations <app>
# 3. Aplicas los cambios en la base de datos: migrate <app>
# 1. Crear deudores - CREATE
# 2. Actualizar esos deudores - UPDATE
# 3. Eliminar esos deudores - DELETE
# 4. Observar un or los deudor(es) - READ (Individual y lista)
# C.R.U.D
class Deudor(models.Model):
    # Django automaticamente define el nombre de la tabla como: <appname>_<classename_minuscula>
    # 1. Definir el schema o la estructura de una tabla.
    # 2. Son utilizado por el sistema de migraciones para aplicar cambios a la base de datos y mantener un historico
    # 3. Las instancias representan registros en la tabla.
    # 4. Possibilida la consulta en la base de dados atravez de un MANAGER, atributo .objects
    name = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    deuda = models.DecimalField(decimal_places=3, max_digits=50)
    data_de_actualizacion = models.DateTimeField(auto_now=True)
    # 10.50131313
    # parte entera: digitos
    # parte decimal: decimal placesImplementacion de la

    def __str__(self):
        return self.name


"""
CREATE TABLE deudor
name varchar(100) 
apellido varchar(100)
deuda decimal


CREATE TABLE cobrador
name
apellido
moto
modelo"""

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_data = models.DateTimeField('data_published')

    def __str__(self):
        return self.question_text

