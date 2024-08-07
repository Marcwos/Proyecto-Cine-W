PGDMP  	    &                |            cine    16.3    16.3 -               0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16423    cine    DATABASE     w   CREATE DATABASE cine WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Spain.1252';
    DROP DATABASE cine;
                postgres    false            �            1259    16541    horarios    TABLE     �   CREATE TABLE public.horarios (
    id integer NOT NULL,
    pelicula_id integer,
    sala_id integer,
    horario time without time zone
);
    DROP TABLE public.horarios;
       public         heap    postgres    false            �            1259    16540    horarios_id_seq    SEQUENCE     �   CREATE SEQUENCE public.horarios_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.horarios_id_seq;
       public          postgres    false    220                       0    0    horarios_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.horarios_id_seq OWNED BY public.horarios.id;
          public          postgres    false    219            �            1259    16425 	   peliculas    TABLE     �   CREATE TABLE public.peliculas (
    id integer NOT NULL,
    nombre character varying(255) NOT NULL,
    sinopsis text,
    imagen_url character varying(255),
    duracion interval,
    categoria character varying(255)
);
    DROP TABLE public.peliculas;
       public         heap    postgres    false            �            1259    16424    peliculas_id_seq    SEQUENCE     �   CREATE SEQUENCE public.peliculas_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.peliculas_id_seq;
       public          postgres    false    216                       0    0    peliculas_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.peliculas_id_seq OWNED BY public.peliculas.id;
          public          postgres    false    215            �            1259    16583    reservas    TABLE     �   CREATE TABLE public.reservas (
    id integer NOT NULL,
    horario_id integer NOT NULL,
    fila integer NOT NULL,
    columna integer NOT NULL
);
    DROP TABLE public.reservas;
       public         heap    postgres    false            �            1259    16582    reservas_id_seq    SEQUENCE     �   CREATE SEQUENCE public.reservas_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.reservas_id_seq;
       public          postgres    false    222                       0    0    reservas_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.reservas_id_seq OWNED BY public.reservas.id;
          public          postgres    false    221            �            1259    16504    salas    TABLE     �   CREATE TABLE public.salas (
    id integer NOT NULL,
    nombre character varying(255) NOT NULL,
    filas integer NOT NULL,
    columnas integer NOT NULL
);
    DROP TABLE public.salas;
       public         heap    postgres    false            �            1259    16503    salas_id_seq    SEQUENCE     �   CREATE SEQUENCE public.salas_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.salas_id_seq;
       public          postgres    false    218                       0    0    salas_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.salas_id_seq OWNED BY public.salas.id;
          public          postgres    false    217            �            1259    16595    usuarios    TABLE     x  CREATE TABLE public.usuarios (
    id integer NOT NULL,
    username character varying(50) NOT NULL,
    password_hash character varying(255) NOT NULL,
    email character varying(100) NOT NULL,
    role character varying(20) NOT NULL,
    CONSTRAINT usuarios_role_check CHECK (((role)::text = ANY ((ARRAY['user'::character varying, 'admin'::character varying])::text[])))
);
    DROP TABLE public.usuarios;
       public         heap    postgres    false            �            1259    16594    usuarios_id_seq    SEQUENCE     �   CREATE SEQUENCE public.usuarios_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.usuarios_id_seq;
       public          postgres    false    224                        0    0    usuarios_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.usuarios_id_seq OWNED BY public.usuarios.id;
          public          postgres    false    223            f           2604    16544    horarios id    DEFAULT     j   ALTER TABLE ONLY public.horarios ALTER COLUMN id SET DEFAULT nextval('public.horarios_id_seq'::regclass);
 :   ALTER TABLE public.horarios ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    220    219    220            d           2604    16428    peliculas id    DEFAULT     l   ALTER TABLE ONLY public.peliculas ALTER COLUMN id SET DEFAULT nextval('public.peliculas_id_seq'::regclass);
 ;   ALTER TABLE public.peliculas ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    215    216    216            g           2604    16586    reservas id    DEFAULT     j   ALTER TABLE ONLY public.reservas ALTER COLUMN id SET DEFAULT nextval('public.reservas_id_seq'::regclass);
 :   ALTER TABLE public.reservas ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    221    222    222            e           2604    16507    salas id    DEFAULT     d   ALTER TABLE ONLY public.salas ALTER COLUMN id SET DEFAULT nextval('public.salas_id_seq'::regclass);
 7   ALTER TABLE public.salas ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    217    218    218            h           2604    16598    usuarios id    DEFAULT     j   ALTER TABLE ONLY public.usuarios ALTER COLUMN id SET DEFAULT nextval('public.usuarios_id_seq'::regclass);
 :   ALTER TABLE public.usuarios ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    224    223    224                      0    16541    horarios 
   TABLE DATA           E   COPY public.horarios (id, pelicula_id, sala_id, horario) FROM stdin;
    public          postgres    false    220   �1                 0    16425 	   peliculas 
   TABLE DATA           Z   COPY public.peliculas (id, nombre, sinopsis, imagen_url, duracion, categoria) FROM stdin;
    public          postgres    false    216   �2                 0    16583    reservas 
   TABLE DATA           A   COPY public.reservas (id, horario_id, fila, columna) FROM stdin;
    public          postgres    false    222   �8                 0    16504    salas 
   TABLE DATA           <   COPY public.salas (id, nombre, filas, columnas) FROM stdin;
    public          postgres    false    218   �9                 0    16595    usuarios 
   TABLE DATA           L   COPY public.usuarios (id, username, password_hash, email, role) FROM stdin;
    public          postgres    false    224   �9       !           0    0    horarios_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.horarios_id_seq', 34, true);
          public          postgres    false    219            "           0    0    peliculas_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.peliculas_id_seq', 10, true);
          public          postgres    false    215            #           0    0    reservas_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.reservas_id_seq', 33, true);
          public          postgres    false    221            $           0    0    salas_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.salas_id_seq', 10, true);
          public          postgres    false    217            %           0    0    usuarios_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.usuarios_id_seq', 3, true);
          public          postgres    false    223            o           2606    16546    horarios horarios_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.horarios
    ADD CONSTRAINT horarios_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.horarios DROP CONSTRAINT horarios_pkey;
       public            postgres    false    220            q           2606    16548 %   horarios horarios_sala_id_horario_key 
   CONSTRAINT     l   ALTER TABLE ONLY public.horarios
    ADD CONSTRAINT horarios_sala_id_horario_key UNIQUE (sala_id, horario);
 O   ALTER TABLE ONLY public.horarios DROP CONSTRAINT horarios_sala_id_horario_key;
       public            postgres    false    220    220            k           2606    16432    peliculas peliculas_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.peliculas
    ADD CONSTRAINT peliculas_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.peliculas DROP CONSTRAINT peliculas_pkey;
       public            postgres    false    216            s           2606    16588    reservas reservas_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.reservas
    ADD CONSTRAINT reservas_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.reservas DROP CONSTRAINT reservas_pkey;
       public            postgres    false    222            m           2606    16509    salas salas_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.salas
    ADD CONSTRAINT salas_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.salas DROP CONSTRAINT salas_pkey;
       public            postgres    false    218            u           2606    16605    usuarios usuarios_email_key 
   CONSTRAINT     W   ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_email_key UNIQUE (email);
 E   ALTER TABLE ONLY public.usuarios DROP CONSTRAINT usuarios_email_key;
       public            postgres    false    224            w           2606    16601    usuarios usuarios_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.usuarios DROP CONSTRAINT usuarios_pkey;
       public            postgres    false    224            y           2606    16603    usuarios usuarios_username_key 
   CONSTRAINT     ]   ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_username_key UNIQUE (username);
 H   ALTER TABLE ONLY public.usuarios DROP CONSTRAINT usuarios_username_key;
       public            postgres    false    224            z           2606    16549 "   horarios horarios_pelicula_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.horarios
    ADD CONSTRAINT horarios_pelicula_id_fkey FOREIGN KEY (pelicula_id) REFERENCES public.peliculas(id);
 L   ALTER TABLE ONLY public.horarios DROP CONSTRAINT horarios_pelicula_id_fkey;
       public          postgres    false    220    216    4715            {           2606    16554    horarios horarios_sala_id_fkey    FK CONSTRAINT     }   ALTER TABLE ONLY public.horarios
    ADD CONSTRAINT horarios_sala_id_fkey FOREIGN KEY (sala_id) REFERENCES public.salas(id);
 H   ALTER TABLE ONLY public.horarios DROP CONSTRAINT horarios_sala_id_fkey;
       public          postgres    false    4717    218    220            |           2606    16589 !   reservas reservas_horario_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.reservas
    ADD CONSTRAINT reservas_horario_id_fkey FOREIGN KEY (horario_id) REFERENCES public.horarios(id);
 K   ALTER TABLE ONLY public.reservas DROP CONSTRAINT reservas_horario_id_fkey;
       public          postgres    false    220    222    4719               �   x�E�ˑ1C�t0S��7��?����]}�g@�������zT�ķNtb��#?-�bq�GV�_�����Y��!�/�bt�)��_+�]/���Ǌٽ��sZ��ӛ�WR�k�2m�B��8e�a�iג]��A݊/{w�Q���7L��z��w��`��i���0��]��~p�ײ�ʐ��g.�nQϧ���`��[�~���(@P'         1  x�mV�n�F<s�b>@Xh%����~ɉ#JnM��;��=C�o�u�!�-W�X��;�BЂ��LwuuUo����@�l������R-9\V�mH���1T�[>3on[���'���_P)��!~�+2E�x��h:��k2%��Z���6��)��m83Ed�"�Ue��aPI��(�M-W��;���P3G��
�y�����lM��/k�����������k��;����"{��(�%_:<�H/6�[D"A��Zr�ې���_ W�,�aoH%����;<Z������/��q��OE�G���]%(DXb�f:� ��ϱ��$P�v?|/�[�[�Cp�#���^�J��ϝm����s@:&������Ãê�bt���s$'���ؙЄ�v�D�lu��FI�$�R�ʏ� �߯_��_���\=}&�bٚWO2��KM[�ag90���I��� :��q#� ��_%[u�y�Oe��!�dpp�9�	�=��i��u�Ai�\�=�V��mo�P���A�2L �x�J��3.�F�O���)��=P��=�S���w��}��3^z�E�i�4�&"]v,����.
R;<6��`�&HP��qAz0jK�s�ń$�#���v��\���|�h�H:4�	��>�6 "0(��T#�����Aª���n�O���I�cn�'�H�[�]��ol�诞e����-�7Q�g\�s�v��-*��˚�-�a-�O�7i���]H�Nh�� ;���^*�� �44���@�{�
�9<�FV�4%"8iO6�%�Ƒ��4	���3���\���y����ʄ䅲�uV��J��hr ɤg�����r��GU��Z^ԯ��_�$�P"����B��UU�H?*5n�Bg����Bu����ȡ��J;��6I9�,��(H�nLt���ɍ��u�[��>R�#����d{2�B�&�:�w���+���KX`T.Nd�y� ;���k��U{�+����WS��,�-{� �f�o��h�suK��I��;A�Q�DU|A%K)�;��5��6f|�d|�`�j�r���"{G�ŧ���T���$��ۺ	�3j��^ JG�sqP�oŏ����l��.?�t����9��W�d�ս��;�`�Y����V__������yċ��e�lQ�L�cs��T�6]Mz��d��}�U�vxh�ioz��Z���\r�veE��*�N���N�f'ˢ1?Yj����6�1
���gmZ�*\Ze����F�T�����fcq���TÃ��A|N�)��[$��ËQ�Ԛ��?�v4Ս��E������Y��Y���3� !�T�j�I4KMr�Bv;f��̶����qn��Czd���: �៱�~1|����zL<��NJ�R�Q�*��8w�d�#�'n���*�2a��QǢr�:��?�\#L|F��E����( y`T��ڼ�q�C���X
�\J���z�Ħ���t�F�6�<�9Y�q/�5�z���Xr����89f�+�^�K�$�Gn�3.���u��� ���:�U�[$m!����ܭW��j�j]         �   x�=�� C��0N�o��?G��Ӌ� �--��N�N�#�LG7�Q�la�"���6�2�K	�⊂n�J#��%U�
:4����%95�Y���۟X{��/%<jCAЬ?3��Ϭgv�bԯۥ�����jo�".����(         Z   x�-ͱ� �Z�"�0`c�H��>��qP�?�$ŵ�u(!���h�N�L\�0h��)ߥAL��bʤf�M�&�7���
χ�����         �   x�M̹�0  й�f��6���*�q)����&Ƿ<j��c� 'F9�h�e�]��g��{R�4�Vw{o����Љ�d����N�d�ׄV|�������$5mМ�B���od{he>��,�![��<�;K.F�1�U�#[�B%ÿ���y��1<�     