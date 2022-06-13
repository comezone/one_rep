-- Table: public.users

-- DROP TABLE IF EXISTS public.users;

CREATE TABLE IF NOT EXISTS public.users
(
    id integer NOT NULL DEFAULT nextval('users_id_seq'::regclass),
    "Имя" character varying COLLATE pg_catalog."default",
    "Фамилия" character varying COLLATE pg_catalog."default",
    "логин" character varying COLLATE pg_catalog."default",
    "пароль" character varying COLLATE pg_catalog."default",
    "Дата Рождения" timestamp without time zone,
    CONSTRAINT users_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.users
    OWNER to postgres;

REVOKE ALL ON TABLE public.users FROM Только чтение;

GRANT DELETE, INSERT, SELECT, UPDATE ON TABLE public.users TO "Администратор";

GRANT SELECT ON TABLE public.users TO "Только чтение";