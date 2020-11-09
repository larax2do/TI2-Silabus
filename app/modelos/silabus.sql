
CREATE database Silabo;

use Silabo;
DROP TABLE IF EXISTS Silabo;
CREATE TABLE Silabo (
  sil_ide INT NOT NULL  ,
  sil_sem varchar(10),
  sil_inst_eva varchar(50),
  sil_per_aca varchar(20)  ,
  sil_fun varchar(15000)  ,
  sil_sum varchar(50)  ,
  sil_req_apro varchar(50)   ,
  PRIMARY KEY (sil_ide)
);


DROP TABLE IF EXISTS Cronograma;
		
CREATE TABLE Cronograma (
  cro_ide INT NOT NULL   ,
  cro_eva varchar(50)   ,
  cro_fecha DATE   ,
  cro_exa_teo INT   ,
  cro_eva_cont INT   ,
  cro_eva_pond INT   ,
   est_eva_ide INT   ,
  PRIMARY KEY (cro_ide)
);



DROP TABLE IF EXISTS Estrategia_evaluacion;
		
CREATE TABLE Estrategia_evaluacion (
  est_eva_ide INT NOT NULL   ,
  est_eva_eva_cont varchar(100)   ,
  est_eva_eva_per varchar(100)   ,
  est_eva_tip_eva varchar(100)   ,
  est_eva_inst_eva varchar(100)   ,
  sil_ide INT   ,
  PRIMARY KEY (est_eva_ide)
);



DROP TABLE IF EXISTS Unidad_academica;
		
CREATE TABLE Unidad_academica (
  uni_aca_ide INT NOT NULL   ,
  uni_nom varchar(100)   ,
  sil_ide INT   ,
  PRIMARY KEY (uni_aca_ide)
);


DROP TABLE IF EXISTS Curso;
		
CREATE TABLE Curso (
  cur_sem INT NOT NULL   ,
  cur_credi INT   ,
  cur_hor_teo INT   ,
  cur_hor_prac INT   ,
  cur_hor_lab INT   ,
 cur_nom varchar(50)  ,
  cur_sum INT   ,
  cur_hor_tot INT   ,
  cur_fund INT   ,
 cur_cod INT   ,
  cur_sem_anual INT   ,
  cur_dur varchar(50)   ,
  sil_ide INT   ,
  PRIMARY KEY (cur_sem)
);



DROP TABLE IF EXISTS Capitulo;
		
CREATE TABLE Capitulo (
  cap_ide INT NOT NULL   ,
  cap_nom varchar(100)  ,
  uni_aca_ide INT   ,
  PRIMARY KEY (cap_ide)
);


DROP TABLE IF EXISTS Tema;
		
CREATE TABLE Tema (
  tem_ide INT NOT NULL   ,
  tem_nom varchar(100)  ,
  tem_sem varchar(10)  ,
  tem_porcen varchar(100)  ,
  cap_ide INT  ,
  PRIMARY KEY (tem_ide)
);



DROP TABLE IF EXISTS Silabo_estrategia_aprendizaje;
		
CREATE TABLE Silabo_estrategia_aprendizaje (
  sil_est_apre_ide INT NOT NULL   ,
  est_apre_ide INT   ,
  sil_ide INT   ,
  PRIMARY KEY (sil_est_apre_ide)
);


DROP TABLE IF EXISTS Estrategia_aprendizaje;
		
CREATE TABLE Estrategia_aprendizaje (
  est_apre_ide INT NOT NULL   ,
  est_apre_tip varchar(100)  ,
  est_apre_desc varchar(100)  ,
  PRIMARY KEY (est_apre_ide)
);

DROP TABLE IF EXISTS Bibliografia;
		
CREATE TABLE Bibliografia (
  bib_ide INT NOT NULL   ,
  bib_nom  varchar(50)  ,
  bib_edi varchar(50)   ,
  bib_editorial varchar(50)   ,
  bib_año varchar(50)   ,
  PRIMARY KEY (bib_ide)
);


DROP TABLE IF EXISTS Bibliografia_silabo;
		
CREATE TABLE Bibliografia_silabo (
  bib_sil_ide INT NOT NULL   ,
  bib_ide INT   ,
  sil_ide INT   ,
  PRIMARY KEY (bib_sil_ide)
);



DROP TABLE IF EXISTS Resultado;
		
CREATE TABLE Resultado (
  res_ide INT NOT NULL   ,
  res_desc varchar(5000) ,
  PRIMARY KEY (res_ide)
);



DROP TABLE IF EXISTS Resultado_silabo;
		
CREATE TABLE Resultado_silabo (
  res_sil_ide INT NOT NULL    ,
  res_ide INT   ,
  sil_ide INT   ,
  PRIMARY KEY (res_sil_ide)
);



DROP TABLE IF EXISTS Autor;
		
CREATE TABLE Autor (
  aut_ide INT NOT NULL   ,
  aut_nom INT   ,
  aut_ape INT   ,
  PRIMARY KEY (aut_ide)
);





DROP TABLE IF EXISTS Autor_bibliografia;
		
CREATE TABLE Autor_bibliografia (
  aut_bib_ide INT NOT NULL    ,
  bib_ide INT   ,
  aut_ide INT   ,
  PRIMARY KEY (aut_bib_ide)
);

   
DROP TABLE IF EXISTS Prerequisitos;
		
CREATE TABLE Prerequisitos(
  pre_ide INT NOT NULL    ,
  curs_ide INT   ,
  pre_cur_ide INT   ,
  PRIMARY KEY (pre_ide)
);


ALTER TABLE Cronograma ADD FOREIGN KEY (est_eva_ide) REFERENCES Estrategia_evaluacion (est_eva_ide);
ALTER TABLE Estrategia_evaluacion ADD FOREIGN KEY (sil_ide) REFERENCES Silabo (sil_ide);
ALTER TABLE Unidad_academica ADD FOREIGN KEY (sil_ide) REFERENCES Silabo (sil_ide);
ALTER TABLE Curso ADD FOREIGN KEY (sil_ide) REFERENCES Silabo (sil_ide);
ALTER TABLE Capitulo ADD FOREIGN KEY (uni_aca_ide) REFERENCES Unidad_academica (uni_aca_ide);
ALTER TABLE Tema ADD FOREIGN KEY (cap_ide) REFERENCES Capitulo (cap_ide);
ALTER TABLE Silabo_estrategia_aprendizaje ADD FOREIGN KEY (est_apre_ide) REFERENCES Estrategia_aprendizaje (est_apre_ide);
ALTER TABLE Silabo_estrategia_aprendizaje ADD FOREIGN KEY (sil_ide) REFERENCES Silabo (sil_ide);
ALTER TABLE Bibliografia_silabo ADD FOREIGN KEY (bib_ide) REFERENCES Bibliografia (bib_ide);
ALTER TABLE Bibliografia_silabo ADD FOREIGN KEY (sil_ide) REFERENCES Silabo (sil_ide);
ALTER TABLE Resultado_silabo ADD FOREIGN KEY (res_ide) REFERENCES Resultado (res_ide);
ALTER TABLE Resultado_silabo ADD FOREIGN KEY (sil_ide) REFERENCES Silabo (sil_ide);
ALTER TABLE Autor_bibliografia ADD FOREIGN KEY (bib_ide) REFERENCES Bibliografia (bib_ide);
ALTER TABLE Autor_bibliografia ADD FOREIGN KEY (aut_ide) REFERENCES Autor (aut_ide);
ALTER TABLE Prerequisitos ADD FOREIGN KEY (curs_ide) REFERENCES Curso (cur_sem);
-- INSERT INTO Silabo (sil_ide,sil_sem,sil_inst_eva,sil_per_aca,sil_fun,sil_sum,sil_req_apro) VALUES
-- ('','','','','','','');
-- INSERT INTO Cronograma (cro_ide,cro_eva,cro_fecha,cro_exa_teo,cro_eva_cont,est_eva_ide) VALUES
-- ('','','','','','');
-- INSERT INTO Estrategia_evaluacion (est_eva_ide,est_eva_eva_cont,est_eva_eva_per,est_eva_tip_eva,est_eva_inst_eva,sil_ide) VALUES
-- ('','','','','','');
-- INSERT INTO Unidad_academica (uni_aca_ide,uni_nom,sil_ide) VALUES
-- ('','','');
-- INSERT INTO Curso (cur_sem,cur_credi,cur_hor_teo,cur_hor_prac,cur_hor_lab,cur_nom,cur_sum,cur_hor_tot,cur_fund,cur_cod,cur_sem_anual,cur_dur,sil_ide) VALUES
-- ('','','','','','','','','','','','','');
-- INSERT INTO Capitulo (cap_ide,cap_nom,uni_aca_ide) VALUES
-- ('','','');
-- INSERT INTO Tema (tem_ide,tem_nom,tem_sem,tem_porcen,cap_ide) VALUES
-- ('','','','','');
-- INSERT INTO Silabo_estrategia_aprendizaje (sil_est_apre_ide,est_apre_ide,sil_ide) VALUES
-- ('','','');
-- INSERT INTO Estrategia_aprendizaje (est_apre_ide,est_apre_tip,est_apre_desc) VALUES
-- ('','','');
-- INSERT INTO Bibliografia (bib_ide,bib_nom,bib_edi,bib_editorial,bib_año) VALUES
-- ('','','','','');
-- INSERT INTO Bibliografia_silabo (bib_sil_ide,bib_ide,sil_ide) VALUES
-- ('','','');
-- INSERT INTO Resultado (res_ide) VALUES
-- ('');
-- INSERT INTO Resultado_silabo (res_sil_ide,res_ide,sil_ide) VALUES
-- ('','','');
-- INSERT INTO Autor (aut_ide,aut_nom,aut_ape) VALUES
-- ('','','');
-- INSERT INTO Autor_bibliografia (aut_bib_ide,bib_ide,aut_ide) VALUES
-- ('','','');