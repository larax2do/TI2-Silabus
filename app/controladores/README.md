# Documentacion de los servicios REST
Modulo: SIlabos

## Tabla de Contenidos
* 1 [Docente](#1-docente)
	* 1.1 [Agregar Docente](#11-agregar-docente)
	* 1.2 [Buscar Docente](#12-buscar-docente)
	* 1.3 [Modificar Docente](#13-modificar-docente)
	* 1.4 [Quitar Docente](#14-quitar-docente)

* 2 [Curso](#2-curso)
	* 2.1 [Buscar Curso](#21-buscar-curso)

* 3 [Silabo](#3-silabo)
	* 3.1 [Crear Silabo](#31-Crear-silabo)
		* 3.1.1 [Agregar Silabo](#311-agregar-Silabo)
		* 3.1.2 [Agregar Contenido](#312-agregar-contenido)
		* 3.1.3 [Agregar Cronograma de Evaluacion](#313-agregar-cronograma-de-evaluacion)
		* 3.1.4 [Asignar Bibliografia](#314-asignar-bibliografia)
	* 3.2 [Buscar Silabo](#32-buscar-silabo)
		* 3.2.1 [Buscar Contenido](#321-buscar-contenido)
		* 3.2.2 [Buscar Cronograma de Evaluacion](#323-buscar-cronograma-de-evaluacion)
	* 3.3 [Modificar Silabo](#33-modificar-silabo)
		* 3.3.1 [Modificar Contenido](#331-modificar-contenido)
		* 3.3.2 [Modificar Cronograma de Evaluacion](#332-modificar-cronograma-de-evaluacion)
	* 3.4 [Quitar Silabo](#34-quitar-silabo)
		* 3.4.1 [Quitar Contenido](#341-quitar-contenido)
		* 3.4.2 [Quitar Bibliografia](#342-quitar-bibliografia)

* 4 [Bibliografia](#4-bibliografia)
	* 4.1 [Agregar Bibliografia](#41-agregar-bibliografia)
	* 4.2 [Buscar Bibliografia](#42-buscar-bibliografia)
	* 4.3 [Modificar Bibliografia](#43-modificar-bibliografia)
	* 4.4 [Quitar Bibliografia](#44-quitar-bibliografia)



## 1. Docente

### Tabla Docente



| Docente       | Descripcion                |
| :-----------: | :------------------------: |
| doc_ide       | Indice(Auto incrementable) |
| doc_dni       | DNI                        |
| doc_nom       | nombre                     |
| doc_ape_pat   | Apellido Paterno           |
| doc_ape_mat   | Apellido Materno           |
| doc_grad_aca  | Grado Academico            |
| dep_aca_ide   | Departamento Academico(FK) |


### 1.2 Agregar Docente

Agrega un nuevo registro a la tabla `Docente`, se envian todos los datos de la tabla excepto el `doc_ide`

~~~
POST  "/addDocente"
~~~


#### Requisito
~~~
{
	"dni": 12345,
	"name": "José",
	"lastname1": "Ccari",
	"lastname2": "Quispe",
	"gradoacademico": "Estudent",
	"depAcademico": 9
}
~~~

#### Respuesta
~~~
Insert Succesful
~~~

### 1.3. Buscar de Docente

Busca un docente de la tabla `Docentes` a partir de su `doc_DNI` y retorna todos los datos.

~~~
GET  "/searchDocente/1234"
~~~

### Requisito


### Respuesta
~~~
[
  {
    "dep_aca_ide": 9,
    "doc_ape_mat": "Cuadros",
    "doc_ape_pat": "Vargas",
    "doc_dni": 1234,
    "doc_grad_aca": "Doctor ",
    "doc_nom": "Ernesto"
  }
]
~~~

### 1.4 Modificar Docente


Recibe todos los datos del registro y los modifica en la Base de Datos.

~~~
POST  "/updateDocente"
~~~

#### Requisito

~~~
{
	"doc_ide" : 2 ,
	"doc_dni" : 999999 ,
	"doc_nom" : "José" ,
	"doc_ape_pat" : "Carlos" ,
	"doc_ape_mat" : "Ccari" ,
	"doc_grad_aca" : "Master" ,
	"dep_aca_ide" : 9
}
~~~

#### Respuesta
~~~
Docente Actualizado
~~~

### 1.5 Quitar Docente
=================
***Elimina*** un docente de la base de datos.

~~~
POST  "\HOME"
~~~

#### Requisito

~~~
{
	doc_dni=77777777
}
~~~

#### Respuesta

~~~

~~~



## 2. Curso

### 2.1 Buscar Curso

Busca un curso por su `cur_cod` y retorna sus valores.

~~~
POST  "/searchCurs/CS1703236"
~~~

#### Requisito

~~~
{
	
}
~~~

#### Respuesta

~~~

  {
    "cur_cod": "CS1703236",
    "cur_credi": 3,
    "cur_dur": 17,
    "cur_fund": null,
    "cur_hor_lab": 6,
    "cur_hor_prac": 0,
    "cur_hor_teo": 6,
    "cur_nom": "Programación Competitiva",
    "cur_sem": null
  }

~~~


## 3. Silabo

### 3.1 Crear Silabo

Crea un campo en silabo en blanco para reservar su `sil_ide` y para que sea relacionada con las otras tablas.


#### 3.1.1 Agregar Silabo
Agrega los datos a la tabla silabo

~~~
POST  "/silabo/silabo/agregar"
~~~

##### Requisito

~~~
{
    "sil_ide": 5,
    "sil_per": VI Semestre,
    "sil_inf_espe": informacion esperada,
    "sil_comp_asig": "asignado",
    "sil_eva_apre": evaluacion de aprendizaje,
    "sil_requ_apro": Estructura de Datos Avanzada,
}
~~~

##### Respuesta

~~~
{
	Insert Succesful
}
~~~
#### 3.1.2 Agregar Contenido

Agrega a la tabla unidad
~~~
POST  "/silabo/unidad_academica/agregar"
~~~
Agrega la tabla de capitulo
~~~
POST  "/silabo/capitulo/agregar"
~~~
Agrega la tabla de tema
~~~
POST  "/silabo/tema/agregar"
~~~

##### Requisito


Tabla de unidad academica
~~~
{
	"sil_ide": 2,
	"sil_per": IV Semestre,
	"sil_inf_espe": Informacion esperada de datos,
	"sil_comp_asig": asignado,
	"sil_eva_apre": evaluacion del aprendizaje de profesores,
	"sil_req_apro": Estructura de Datos Avanzada
}
~~~
Tabla de capitulo 
~~~
{
	"cap_ide": 2,
	"cap_nom": Capitulo 1
}
~~~
Tabla de Tema
~~~
{
	"tem_ide": 2,
	"tem_sem": IV Semestre,
	"tem_porcen": 80 por ciento
}
~~~


##### Respuesta

~~~
{
	Insert Succesful
}
~~~
~~~
{
	Insert Succesful
}
~~~
~~~
{
	Insert Succesful
}
~~~
#### 3.1.3 Agregar Cronograma
Agrega el contenido a la tabla cronograma del Silabo

~~~
POST  "/silabo/cronogramaEva/agregar"
~~~

##### Requisito

~~~
{
	"cro_eva": 2,
	"cro_eva_con": 15,
	"cro_exa_teo": 50,
	"cro_fecha": "Fri, 14 Aug 2020 00:00:00 GMT",
}
~~~

##### Respuesta

~~~
{
	
}
~~~
#### 3.1.4 Asignar Bibliografia
Asigna una bibliografia al silabo

~~~
POST
~~~

#### Requisito

~~~
{
    "bib_nom"
    "bib_edi"
    "bib_editorial"
    "bib_año"
}
~~~

#### Respuesta
Insert Succesful

### 3.2 Buscar Silabo
=================
Busca el silabo por `sil_ide` y retorna todos los campos de la tabla silabo y subtablas

~~~
POST
~~~

#### Requisito
sil_ide

#### Respuesta

~~~
{
    "sil_fun"
    "sil_ide"
    "sil_inst_eva"
    "sil_per_aca"
    "sil_req_apro"
    "sil_sem"
    "sil_sum"
}
~~~

#### 3.2.1 Buscar Contenido

Busca el contenido del silabo por `sil_ide` y retorna todos los campos de la tabla unidad_academica, capitulos y temas

~~~
POST  "/silabo/contenido/buscar"
~~~

##### Requisito

~~~
{
	"sil_ide":2
}
~~~

##### Respuesta

~~~
[
  {
    "cap_ide": 2,
    "cap_nom": "1 cap 2",
    "tem_ide": 2,
    "tem_nom": "tem1",
    "tem_porcen": "5",
    "tem_sem": "1",
    "uni_aca_ide": 2,
    "uni_nom": "uni dos"
  },
  {
    "cap_ide": 2,
    "cap_nom": "1 cap 2",
    "tem_ide": 3,
    "tem_nom": "tem2",
    "tem_porcen": "5",
    "tem_sem": "1",
    "uni_aca_ide": 2,
    "uni_nom": "uni dos"
  },
  {
    "cap_ide": 3,
    "cap_nom": "1 cap 1",
    "tem_ide": 4,
    "tem_nom": "tem1",
    "tem_porcen": "5",
    "tem_sem": "1",
    "uni_aca_ide": 3,
    "uni_nom": "uni tres"
  },
  {
    "cap_ide": 3,
    "cap_nom": "1 cap 1",
    "tem_ide": 5,
    "tem_nom": "tem2",
    "tem_porcen": "5",
    "tem_sem": "1",
    "uni_aca_ide": 3,
    "uni_nom": "uni tres"
  }
]
~~~

#### 3.2.2 Buscar Cronograma de Evaluacion

Busca el cronograma de evaluacion del silabo por `sil_ide` y retorna todos los campos de la tabla Cronograma_evaluacion

~~~
POST  "/silabo/cronogramaEva/buscar"
~~~

##### Requisito

~~~
{
	"sil_ide":2
}
~~~

##### Respuesta

~~~
[
  {
    "cro_eva": 2,
    "cro_eva_con": 15,
    "cro_exa_teo": 50,
    "cro_fecha": "Fri, 14 Aug 2020 00:00:00 GMT",
    "cro_ide": 2
  },
  {
    "cro_eva": 2,
    "cro_eva_con": 15,
    "cro_exa_teo": 15,
    "cro_fecha": "Fri, 14 Aug 2020 00:00:00 GMT",
    "cro_ide": 3
  }
]
~~~

### 3.3 Modificar Silabo

Modifica la tabla silabo

~~~
POST  "/silabo/silabo/modificar"
~~~

#### Requisito

~~~
{
    "sil_ide": 5,
    "sil_per": VI Semestre,
    "sil_inf_espe": informacion esperada,
    "sil_comp_asig": "asignado",
    "sil_eva_apre": evaluacion de aprendizaje,
    "sil_requ_apro": Estructura de Datos Avanzada,
}
~~~

#### Respuesta
~~~
{
    "sil_ide": 5,
    "sil_per": VI Semestre,
    "sil_inf_espe": informacion esperada,
    "sil_comp_asig": "asignado",
    "sil_eva_apre": evaluacion de aprendizaje,
    "sil_requ_apro": Estructura de Datos Avanzada,
}
~~~

#### 3.3.1 Modificar Contenido
Modifica la tabla de Unidad
~~~
POST  "/silabo/unidad_academica/modificar"
~~~
Modifica la tabla de capitulo
~~~
POST  "/silabo/capitulo/modificar"
~~~
Modifica la tabla de tema
~~~
POST  "/silabo/tema/modificar"
~~~

##### Requisito
Tabla de unidad academica
~~~
{
	"sil_ide": 2,
	"sil_per": IV Semestre,
	"sil_inf_espe": Informacion esperada de datos,
	"sil_comp_asig": asignado,
	"sil_eva_apre": evaluacion del aprendizaje de profesores,
	"sil_req_apro": Estructura de Datos Avanzada
}
~~~
Tabla de capitulo 
~~~
{
	"cap_ide": 2,
	"cap_nom": Capitulo 1
}
~~~
Tabla de Tema
~~~
{
	"tem_ide": 2,
	"tem_sem": IV Semestre,
	"tem_porcen": 80 por ciento
}
~~~
##### Respuesta

Contenido Modificado/Actualizado
Tabla de unidad academica
~~~
{
	"sil_ide": 2,
	"sil_per": IV Semestre,
	"sil_inf_espe": Informacion esperada de datos,
	"sil_comp_asig": asignado,
	"sil_eva_apre": evaluacion del aprendizaje de profesores,
	"sil_req_apro": Estructura de Datos Avanzada
}
~~~
Tabla de capitulo 
~~~
{
	"cap_ide": 2,
	"cap_nom": Capitulo 1
}
~~~
Tabla de Tema
~~~
{
	"tem_ide": 2,
	"tem_sem": IV Semestre,
	"tem_porcen": 80 por ciento
}
~~~

#### 3.3.2 Modificar Cronograma
Modifica la tabla cronograma

~~~
POST  "/silabo/cronogramaEva/modificar"
~~~

##### Requisito

~~~
{
	"cro_eva": 2,
	"cro_eva_con": 15,
	"cro_exa_teo": 50,
	"cro_fecha": "Fri, 14 Aug 2020 00:00:00 GMT",
	"cro_ide": 2
}
~~~

##### Respuesta

~~~
{
	
}
~~~
### 3.4 Quitar Silabo
=================
QUita el silabo y todas sus subtablas

~~~
DEL  "\HOME"
~~~

#### Requisito
ID

#### Respuesta

~~~
null
~~~
#### 3.4.1 Quitar Contenido
Quita contenido(unidad,capitulo,silabo) del silabo

~~~
POST  "/silabo/contenido/quitar/unidad"
~~~

##### Requisito

~~~
{
	uni_aca_ide: 1
}
~~~

~~~
{
	cap_ide: 1
}
~~~

~~~
{
	tem_ide: 1
}
~~~

##### Respuesta

~~~
{
	
}
~~~
#### 3.4.2 Quitar Bibliografia
QUita la bibliografia asignada al silabo

~~~
DEL
~~~

##### Requisito
ID

##### Respuesta

~~~
null
~~~



