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
		* 3.2.2 [Buscar Cronograma Academico](#322-buscar-cronograma-academico)
		* 3.2.3 [Buscar Cronograma de Evaluacion](#323-buscar-cronograma-de-evaluacion)
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
=================

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
=================
Agrega un nuevo registro a la tabla `Docente`, se envian todos los datos de la tabla excepto el `doc_ide`

~~~
POST  "\HOME"
~~~


#### Requisito
~~~
{
	doc_dni="77777777"
	doc_nom="Ernesto"
	doc_ape_pat="Cuadros"
	doc_ape_mat="Vargas"
	doc_grad_aca="Doctor"
	dep_aca_ide="6"
}

~~~

#### Respuesta
~~~

~~~

### 1.3. Buscar de Docente
=================
Busca un docente de la tabla `Docentes` a partir de su `doc_DNI` y retorna todos los datos.

~~~
POST  "\HOME"
~~~

### Requisito
~~~
{
	dni=77777777
}
~~~

### Respuesta
~~~
{
	doc_ide=1
	doc_dni=77777777
	doc_nom="Ernesto"
	doc_ape_pat="Cuadros"
	doc_ape_mat="Vargas"
	doc_grad_aca="Doctor"
	dep_aca_ide="6"
}
~~~

### 1.4 Modificar Docente
=================
Recibe todos los datos del registro y los modifica en la Base de Datos.

~~~
POST  "\HOME"
~~~

#### Requisito

~~~
{
	doc_ide=1
	doc_dni=77777777
	doc_nombre="Ernesto"
	doc_ape_pat="Cuadros"
	doc_ape_mat="Vargas"
	doc_grad_aca="Doctor"
	dep_aca_ide="6"
}
~~~

#### Respuesta
~~~

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
=================
### 2.1 Buscar Curso
=================
Busca un curso por su `cur_cod` y retorna sus valores.

~~~
POST  "\HOME"
~~~

#### Requisito

~~~
{
	
}
~~~

#### Respuesta

~~~
{
	
}
~~~


## 3. Silabo
=================
### 3.1 Crear Silabo
=================
Crea un campo en silabo en blanco para reservar su `sil_ide` y para que sea relacionada con las otras tablas.

~~~
POST  "\HOME"
~~~

#### Requisito

~~~
{
	
}
~~~

#### Respuesta

~~~
{
	
}
~~~
#### 3.1.1 Agregar Silabo
Agrega los datos a la tabla silabo

~~~
POST  "\HOME"
~~~

##### Requisito

~~~
{
	
}
~~~

##### Respuesta

~~~
{
	
}
~~~
#### 3.1.2 Agregar Contenido
Agrega a la tabla unidad, capitulo y tabla(3 serv rest)

~~~
POST  "\HOME"
~~~

##### Requisito

~~~
{
	
}
~~~

##### Respuesta

~~~
{
	
}
~~~
#### 3.1.3 Agregar Cronograma
Agrega el contenido a la tabla cronograma del Silabo

~~~
POST  "\HOME"
~~~

##### Requisito

~~~
{
	
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
POST  "\HOME"
~~~

#### Requisito

~~~
{
	
}
~~~

#### Respuesta

~~~
{
	
}
~~~
### 3.2 Buscar Silabo
=================
Busca el silabo por `sil_ide` y retorna todos los campos de la tabla silabo y subtablas

~~~
POST  "\HOME"
~~~

#### Requisito

~~~
{
	
}
~~~

#### Respuesta

~~~
{
	
}
~~~
### 3.3 Modificar Silabo
=================
Modifica la tabla silabo

~~~
POST  "\HOME"
~~~

#### Requisito

~~~
{
	
}
~~~

#### Respuesta

~~~
{
	
}
~~~

#### 3.3.1 Modificar Contenido
Modifica la tabla de Unidad, Capitulo y tema



#### 3.3.2 Modificar Cronograma
Modifica la tabla cronograma

~~~
POST  "\HOME"
~~~

##### Requisito

~~~
{
	
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
POST  "\HOME"
~~~

#### Requisito

~~~
{
	
}
~~~

#### Respuesta

~~~
{
	
}
~~~
#### 3.4.1 Quitar Contenido
QUita contenido(unidad,capitulo,silabo) del silabo

~~~
POST  "\HOME"
~~~

##### Requisito

~~~
{
	
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
POST  "\HOME"
~~~

##### Requisito

~~~
{
	
}
~~~

##### Respuesta

~~~
{
	
}
~~~


