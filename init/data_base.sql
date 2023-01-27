--create schema
CREATE SCHEMA reino
    AUTHORIZATION goyo;

-- create table catalog
CREATE TABLE reino.ct_magic_affinity
(
    id integer NOT NULL,
    name character varying(30) NOT NULL,
    description character varying,
    status smallint,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS reino.ct_magic_affinity
    OWNER to goyo;

-- create table trebol
CREATE TABLE reino.ct_grimonio
(
    id integer NOT NULL,
    name character varying(30) NOT NULL,
    description character varying,
    status smallint,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS reino.ct_grimonio
    OWNER to goyo;

-- create table trebol
CREATE TABLE reino.ct_status
(
    id integer NOT NULL,
    name character varying(30) NOT NULL,
    description character varying,
    status smallint,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS reino.ct_status
    OWNER to goyo;

-- create table request
CREATE TABLE reino.ta_students
(
    id integer NOT NULL,
    name character varying(20) NOT NULL,
    lastname character varying(20),
    identification character varying(10),
    age smallint,
    magic_affinity smallint,
    grimonio smallint,
    status smallint,
    PRIMARY KEY (id),
    CONSTRAINT fx_grimonio FOREIGN KEY (grimonio)
        REFERENCES reino.ct_grimonio (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT fx_magic_affinity FOREIGN KEY (magic_affinity)
        REFERENCES reino.ct_magic_affinity (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT fx_status FOREIGN KEY (status)
        REFERENCES reino.ct_status (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
);

ALTER TABLE IF EXISTS reino.ta_students
    OWNER to goyo;

ALTER TABLE IF EXISTS reino.ta_students
    ALTER COLUMN id SET DEFAULT nextval('reino.ta_students_sequences'::regclass);

-- catalgo grimonios
INSERT INTO reino.ct_grimonio(
	id, name, description, status)
	VALUES (1, 'Sinceridad', 'Trébol de 1 hoja', 1);
	
INSERT INTO reino.ct_grimonio(
	id, name, description, status)
	VALUES (2, 'Esperanza', 'Trébol de 2 hojas', 1);

INSERT INTO reino.ct_grimonio(
	id, name, description, status)
	VALUES (3, 'Amor', 'Trébol de 3 hojas', 1);

INSERT INTO reino.ct_grimonio(
	id, name, description, status)
	VALUES (4, 'Buena Fortuna', 'Trébol de 4 hojas', 1);

INSERT INTO reino.ct_grimonio(
	id, name, description, status)
	VALUES (5, 'Desesperación', 'Trébol de 5 hojas', 1);

-- catalogo status
INSERT INTO reino.ct_status(
	id, name, description, status)
	VALUES (1, 'request_init', 'solicitud iniciada', 1);
INSERT INTO reino.ct_status(
	id, name, description, status)
	VALUES (2, 'update_request', 'Actualización de solicitud', 1);
INSERT INTO reino.ct_status(
	id, name, description, status)
	VALUES (3, 'accepted_student', 'Estudiante aceptado', 1);
INSERT INTO reino.ct_status(
	id, name, description, status)
	VALUES (4, 'rejected_student', 'Estudiante rechazado', 1);
INSERT INTO reino.ct_status(
	id, name, description, status)
	VALUES (5, 'delete_student', 'Estudiante eliminado', 1);