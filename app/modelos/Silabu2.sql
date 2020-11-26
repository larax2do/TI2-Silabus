create database Silabo2;
use Silabo2;

DROP TABLE IF EXISTS Curso;		
CREATE TABLE Curso (
cur_ide INT NOT NULL auto_increment,
cur_cod INT,
cur_nom varchar(50),
cur_sem INT,
cur_dur INT,
cur_hor_teo INT,
cur_hor_prac INT,
cur_hor_lab INT,
cur_credi INT,
cur_fund varchar(5000),
PRIMARY KEY (cur_ide)
);


DROP TABLE IF EXISTS Silabo;
CREATE TABLE Silabo (
  sil_ide INT NOT NULL auto_increment,
  sil_per varchar(10),
  sil_inf_espe varchar(4000),
  sil_comp_asig varchar(5000),
  sil_eva_apre varchar(3000),
  sil_req_apro varchar(2000),
  cur_ide INT,
  PRIMARY KEY (sil_ide)
);

DROP TABLE IF EXISTS Programacion_actividades;
CREATE TABLE Programacion_actividades(
  prog_ide INT NOT NULL auto_increment,
  prog_act_met varchar(1000),
  prog_act_med varchar(1000),
  prog_act_form varchar(1000),
  prog_act_inv varchar(1000),
  sil_ide INT,
  PRIMARY KEY (prog_ide)
);



DROP TABLE IF EXISTS Cronograma_evaluacion;
CREATE TABLE Cronograma_evaluacion (
  cro_ide INT NOT NULL auto_increment,
  cro_eva INT NOT NULL,
  cro_fecha DATE,
  cro_exa_teo INT,
  cro_eva_con INT,
  sil_ide INT,
  PRIMARY KEY (cro_ide)
);




DROP TABLE IF EXISTS Docente;
CREATE TABLE Docente (
doc_ide INT NOT NULL auto_increment,
doc_dni INT NOT NULL,
doc_nom varchar (100),
doc_ape_mat varchar(100),
doc_ape_pat varchar(100),
doc_grad_aca varchar(100),
dep_aca_ide INT,
PRIMARY KEY (doc_ide)
);

DROP TABLE IF EXISTS Sil_docente;
CREATE TABLE Sil_docente (
sil_docente_ide INT NOT NULL auto_increment,
doc_ide INT,
sil_ide INT,
PRIMARY KEY (sil_docente_ide)
);


DROP TABLE IF EXISTS Departamento_academico;
CREATE TABLE Departamento_academico (
dep_aca_ide INT NOT NULL auto_increment,
dep_aca_nom varchar (100),
PRIMARY KEY (dep_aca_ide)
);


DROP TABLE IF EXISTS Unidad_academica;
CREATE TABLE Unidad_academica (
uni_aca_ide INT NOT NULL auto_increment,
uni_nom varchar(100),
sil_ide INT,
PRIMARY KEY (uni_aca_ide)
);






DROP TABLE IF EXISTS Capitulo;		
CREATE TABLE Capitulo (
  cap_ide INT NOT NULL auto_increment,
  cap_nom varchar(100),
  uni_aca_ide INT,
  PRIMARY KEY (cap_ide)
);


DROP TABLE IF EXISTS Tema;
CREATE TABLE Tema (
  tem_ide INT NOT NULL auto_increment,
  tem_nom varchar(100),
  tem_sem varchar(10),
  tem_porcen varchar(100),
  cap_ide INT,
  PRIMARY KEY (tem_ide)
);



DROP TABLE IF EXISTS Bibliografia;
CREATE TABLE Bibliografia (
  bib_ide INT NOT NULL auto_increment,
  bib_nom  varchar(50),
  bib_edi varchar(50),
  bib_editorial varchar(50),
  bib_año varchar(50),
  PRIMARY KEY (bib_ide)
);


DROP TABLE IF EXISTS Bibliografia_silabo;
CREATE TABLE Bibliografia_silabo (
  bib_sil_ide INT NOT NULL auto_increment,
  bib_sil_prio BOOLEAN,
  bib_ide INT,
  sil_ide INT,
  PRIMARY KEY (bib_sil_ide)
);



DROP TABLE IF EXISTS Autor;
CREATE TABLE Autor (
  aut_ide INT NOT NULL auto_increment,
  aut_nom INT,
  aut_ape INT,
  PRIMARY KEY (aut_ide)
);





DROP TABLE IF EXISTS Autor_bibliografia;
CREATE TABLE Autor_bibliografia (
  aut_bib_ide INT NOT NULL auto_increment,
  bib_ide INT,
  aut_ide INT,
  PRIMARY KEY (aut_bib_ide)
);

   
DROP TABLE IF EXISTS Prerequisitos;
CREATE TABLE Prerequisitos(
  pre_ide INT NOT NULL auto_increment,
  curs_ide INT,
  pre_cur_ide INT,
  PRIMARY KEY (pre_ide)
);


ALTER TABLE Cronograma_evaluacion ADD FOREIGN KEY (sil_ide) REFERENCES Silabo (sil_ide);

ALTER TABLE Unidad_academica ADD FOREIGN KEY (sil_ide) REFERENCES Silabo (sil_ide);
ALTER TABLE Silabo ADD FOREIGN KEY (cur_ide) REFERENCES Curso (cur_ide);
ALTER TABLE Capitulo ADD FOREIGN KEY (uni_aca_ide) REFERENCES Unidad_academica (uni_aca_ide);
ALTER TABLE Tema ADD FOREIGN KEY (cap_ide) REFERENCES Capitulo (cap_ide);
ALTER TABLE Programacion_actividades ADD FOREIGN KEY (sil_ide) REFERENCES Silabo(sil_ide);
ALTER TABLE Bibliografia_silabo ADD FOREIGN KEY (bib_ide) REFERENCES Bibliografia (bib_ide);
ALTER TABLE Bibliografia_silabo ADD FOREIGN KEY (sil_ide) REFERENCES Silabo (sil_ide);
ALTER TABLE Autor_bibliografia ADD FOREIGN KEY (bib_ide) REFERENCES Bibliografia (bib_ide);
ALTER TABLE Autor_bibliografia ADD FOREIGN KEY (aut_ide) REFERENCES Autor (aut_ide);
ALTER TABLE Prerequisitos ADD FOREIGN KEY (curs_ide) REFERENCES Curso (cur_ide);

ALTER TABLE Sil_docente ADD FOREIGN KEY (sil_ide) REFERENCES Silabo (sil_ide);
ALTER TABLE Sil_docente ADD FOREIGN KEY (doc_ide) REFERENCES Docente (doc_ide);

ALTER TABLE Docente ADD FOREIGN KEY (dep_aca_ide) REFERENCES Departamento_academico (dep_aca_ide);