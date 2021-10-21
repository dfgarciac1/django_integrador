from django.db import models

# Create your models here.

class Carrera(models.Model):
    codigo = models.CharField(max_length = 3,primary_key = True)
    nombre = models.CharField(max_length = 50)
    duracion = models.PositiveSmallIntegerField(default = 5)

    def __str__(self):
        return f'{self.nombre} (Duración: {self.duracion} año(s))'

class Estudiante(models.Model):
    dni = models.CharField(max_length = 8,primary_key = True)
    apellidoPaterno =  models.CharField(max_length = 35)
    apellidoMaterno =  models.CharField(max_length = 35)
    nombres =  models.CharField(max_length = 35)
    fechaNacimiento =  models.DateField()
    sexos = [
        ('F','Femenino'),
        ('M','Masculino')
    ]
    
    sexo = models.CharField(max_length = 1,choices = sexos,default = 'M')
    carrera = models.ForeignKey(Carrera,null = False,blank = False,on_delete = models.CASCADE)
    vigencia = models.BooleanField(default = True)
        
    def nombreCompleto(self):
        return f'{self.apellidoPaterno}, {self.apellidoMaterno}, {self.nombres}'

    def __str__(self):
        estadoEstudiante = 'VIGENTE' if self.vigencia else 'RETIRADO'
        return f'{self.nombreCompleto()} / Carrera: {self.carrera} / {estadoEstudiante}'

class Curso(models.Model):
    codigo = models.CharField(max_length = 6,primary_key = True)
    nombre =  models.CharField(max_length = 30)
    creditos =  models.PositiveSmallIntegerField()
    docente =  models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.nombre} ({self.codigo}) / Docente: {self.docente}'

class Matricula(models.Model):
    id = models.AutoField(primary_key = True)
    estudiante = models.ForeignKey(Estudiante,null = False,blank = False, on_delete = models.CASCADE)
    curso = models.ForeignKey(Curso,null = False,blank = False, on_delete = models.CASCADE)
    fechaMatricula = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        letrasexo = 'o' if self.estudiante.sexo == 'M' else 'a'
        fechaMat = self.fechaMatricula.strftime('%A %d%m%y %H:%M%S')
        return f'{self.estudiante.nombreCompleto()} matriculad{letrasexo} en el curso {self.curso} / Fecha: {fechaMat}'

