-- Table: public."Students"

-- DROP TABLE public."Students";

CREATE TABLE public."Students"
(
    "Student_Id" integer NOT NULL,
    "First_Name" text COLLATE pg_catalog."default" NOT NULL,
    "Last_Name" text COLLATE pg_catalog."default" NOT NULL,
    "Email" text COLLATE pg_catalog."default" NOT NULL,
    "Graduation_Date" date NOT NULL,
    "Skills" text COLLATE pg_catalog."default" NOT NULL,
    "Bio" text COLLATE pg_catalog."default" NOT NULL,
    "Photo" text COLLATE pg_catalog."default",
    "Github" text COLLATE pg_catalog."default",
    "Website" text COLLATE pg_catalog."default",
    "Resume" text COLLATE pg_catalog."default",
    "Hashed_password" text COLLATE pg_catalog."default",
    CONSTRAINT "Students_pkey" PRIMARY KEY ("Student_Id")
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public."Students"
    OWNER to postgres;