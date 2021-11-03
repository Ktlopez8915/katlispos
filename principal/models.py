# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Articulo(models.Model):
    idarticulo = models.IntegerField(primary_key=True)
    idcategoria = models.ForeignKey('Categoria', models.DO_NOTHING, db_column='idcategoria')
    nombre = models.CharField(max_length=70, db_collation='utf8_spanish_ci')
    presentacion = models.CharField(max_length=100, db_collation='utf8_spanish_ci')
    stockminimo = models.IntegerField()
    stockmaximo = models.IntegerField()
    estado = models.CharField(max_length=45)
    proveedor = models.CharField(max_length=70, db_collation='utf8_spanish_ci')
    fechaingreso = models.DateField()

    class Meta:
        managed = False
        db_table = 'articulo'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cabezamovimiento(models.Model):
    numerodocumento = models.IntegerField(primary_key=True)
    idtipodocumentos = models.ForeignKey('Tipodocumento', models.DO_NOTHING, db_column='idtipodocumentos')
    idusuarios = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='idusuarios')
    idterceros = models.ForeignKey('Tercero', models.DO_NOTHING, db_column='idterceros')
    numerofactura = models.IntegerField(blank=True, null=True)
    fechadocumento = models.DateField()
    valordocumento = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cabezamovimiento'


class Categoria(models.Model):
    idcategorias = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=70, db_collation='utf8_spanish_ci')
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categoria'


class Cuerpomovimiento(models.Model):
    idcuerpomovimiento = models.IntegerField(primary_key=True)
    idcabezamovimiento = models.ForeignKey(Cabezamovimiento, models.DO_NOTHING, db_column='idcabezamovimiento')
    idarticulob = models.ForeignKey(Articulo, models.DO_NOTHING, db_column='idarticulob')
    cantidad = models.IntegerField()
    valor = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cuerpomovimiento'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Kardex(models.Model):
    idcardex = models.IntegerField(primary_key=True)
    idarticulos = models.ForeignKey(Articulo, models.DO_NOTHING, db_column='idarticulos')
    stockactual = models.IntegerField(db_column='Stockactual')  # Field name made lowercase.
    precioventa = models.IntegerField()
    preciocompra = models.IntegerField()
    nombre = models.CharField(max_length=70, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kardex'


class Modulo(models.Model):
    idmodulo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=70, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modulo'


class Movimientocaja(models.Model):
    idmovimientocaja = models.IntegerField(primary_key=True)
    idtipomovimiento = models.ForeignKey('Tipomovimiento', models.DO_NOTHING, db_column='idtipomovimiento')
    idusuarios1 = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='idusuarios1')
    fecha = models.DateField()
    billete = models.IntegerField()
    moneda = models.IntegerField()
    saldocaja = models.IntegerField()
    ventas = models.IntegerField()
    pagos = models.IntegerField()
    diferencias = models.IntegerField()
    comentarios = models.TextField()

    class Meta:
        managed = False
        db_table = 'movimientocaja'


class Tercero(models.Model):
    codigotercero = models.IntegerField(primary_key=True)
    idtipotercero = models.ForeignKey('Tipotercero', models.DO_NOTHING, db_column='idtipotercero')
    nombre = models.CharField(max_length=100, db_collation='utf8_spanish_ci', blank=True, null=True)
    direccion = models.CharField(max_length=50, db_collation='utf8_spanish_ci')
    telefono = models.CharField(max_length=45, db_collation='utf8_spanish_ci')
    correo = models.CharField(max_length=70, db_collation='utf8_spanish_ci')

    class Meta:
        managed = False
        db_table = 'tercero'


class Tipodocumento(models.Model):
    idtipodocumento = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=70, db_collation='utf8_spanish_ci')
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipodocumento'


class Tipomovimiento(models.Model):
    idtipomovimientos = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=70, db_collation='utf8_spanish_ci')
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipomovimiento'


class Tipotercero(models.Model):
    idtipoterceros = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=70, db_collation='utf8_spanish_ci')
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipotercero'


class Tipousuario(models.Model):
    idtipousuarios = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=70, db_collation='utf8_spanish_ci')
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipousuario'


class Usuario(models.Model):
    idusuario = models.IntegerField(primary_key=True)
    idtipousuario = models.ForeignKey(Tipousuario, models.DO_NOTHING, db_column='idtipousuario')
    usuario = models.CharField(max_length=70, db_collation='utf8_spanish_ci', blank=True, null=True)
    contrasena = models.CharField(max_length=10, db_collation='utf8_spanish_ci')
    nombre = models.CharField(max_length=45, blank=True, null=True)
    apellido = models.CharField(max_length=45, blank=True, null=True)
    identificacion = models.CharField(max_length=45, blank=True, null=True)
    usuariomodulo_idusuario = models.ForeignKey('Usuariomodulo', models.DO_NOTHING, db_column='usuariomodulo_idusuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'


class Usuariomodulo(models.Model):
    idusuario = models.IntegerField(primary_key=True)
    idmodulo = models.IntegerField(blank=True, null=True)
    modulo_idmodulo = models.ForeignKey(Modulo, models.DO_NOTHING, db_column='modulo_idmodulo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuariomodulo'
