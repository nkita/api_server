--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.11
-- Dumped by pg_dump version 9.6.11

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


--
-- Name: uuid-ossp; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS "uuid-ossp" WITH SCHEMA public;


--
-- Name: EXTENSION "uuid-ossp"; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION "uuid-ossp" IS 'generate universally unique identifiers (UUIDs)';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: tb_json; Type: TABLE; Schema: public; Owner: app_user
--

CREATE TABLE public.tb_json (
    id uuid NOT NULL,
    parent_id uuid,
    data jsonb,
    add_date timestamp without time zone,
    modify_date timestamp without time zone,
    type text
);


ALTER TABLE public.tb_json OWNER TO app_user;

--
-- Data for Name: tb_json; Type: TABLE DATA; Schema: public; Owner: app_user
--

INSERT INTO public.tb_json VALUES ('6e213103-e12b-492b-a0a5-026581213b73', '1ad5f86c-9913-4368-a8ce-48775a4188cb', '{"ext": "pdf", "memo": "このファイルは・・・・・", "title": "サンプルファイル", "filepath": "/***/***/***.pdf"}', '2019-01-05 02:49:00.512492', '2019-01-05 02:49:00.512492', 'f');
INSERT INTO public.tb_json VALUES ('8d2e60f8-1018-11e9-b0e0-0242ac110002', '425eb020-e79f-48f8-969b-e17a09705840', '{"ext": "pdf", "memo": "このファイルは・・・・・", "title": "サンプルファイル2", "filepath": "/***/***/***.pdf"}', '2019-01-04 21:02:04.440527', '2019-01-04 21:02:04.440527', 'f');
INSERT INTO public.tb_json VALUES ('0d8ca7cb-f6a6-4216-9bca-8e7dcd0d29ed', NULL, '{"memo": "このメモは・・・・・", "title": "サンプルディレクトリ"}', '2019-01-05 02:44:36.657518', '2019-01-05 02:44:36.657518', 'd');
INSERT INTO public.tb_json VALUES ('0e7240c7-fc65-4a05-97d4-f3a4c2362436', NULL, '{"memo": "このメモは・・・・・", "title": "01_マイピクチャ"}', '2019-01-05 02:43:21.227199', '2019-01-05 02:43:21.227199', 'd');
INSERT INTO public.tb_json VALUES ('1ad5f86c-9913-4368-a8ce-48775a4188cb', NULL, '{"memo": "このメモは・・・・・", "title": "02_マイドキュメント"}', '2019-01-05 02:46:25.098286', '2019-01-05 02:46:25.098286', 'd');
INSERT INTO public.tb_json VALUES ('425eb020-e79f-48f8-969b-e17a09705840', '1ad5f86c-9913-4368-a8ce-48775a4188cb', '{"memo": "このメモは・・・・・", "title": "02_02_サブドキュメント"}', '2019-01-05 02:41:16.495167', '2019-01-05 02:41:16.495167', 'd');


--
-- Name: tb_json tb_json_pkey; Type: CONSTRAINT; Schema: public; Owner: app_user
--

ALTER TABLE ONLY public.tb_json
    ADD CONSTRAINT tb_json_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

