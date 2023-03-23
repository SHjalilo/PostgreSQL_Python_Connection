-- Table: public.employees

-- DROP TABLE IF EXISTS public.employees;

CREATE TABLE IF NOT EXISTS public.employees
(
    id integer NOT NULL DEFAULT nextval('employees_id_seq'::regclass),
    name text COLLATE pg_catalog."default",
    age integer,
    departement text COLLATE pg_catalog."default",
    CONSTRAINT employees_pkey PRIMARY KEY (id)
);