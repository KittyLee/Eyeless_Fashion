# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from django.db import models

class EyelessUser(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    class Meta:
        managed = False
        db_table = 'eyeless_user'

class EyelessStylist(models.Model):
    id = models.IntegerField(primary_key=True)
    style_id = models.IntegerField()
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    class Meta:
        managed = False
        db_table = 'eyeless_stylist'

class EyelessPost(models.Model):
    id = models.IntegerField(primary_key=True)
    post_id = models.IntegerField()
    user_id = models.ForeignKey('EyelessUser')
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    text = models.TextField()
    class Meta:
        managed = False
        db_table = 'eyeless_post'

class EyelessMessage(models.Model):
    id = models.IntegerField(primary_key=True)
    message_id = models.IntegerField()
    post_id = models.ForeignKey('EyelessPost')
    user_id = models.ForeignKey('EyelessUser')
    style_id = models.ForeignKey('EyelessStylist')
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    text = models.TextField()
    class Meta:
        managed = False
        db_table = 'eyeless_message'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        managed = False
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        managed = False
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    class Meta:
        managed = False
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'django_session'
