from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Район"
        verbose_name_plural = "Районы"

    def __str__(self):
        return self.name


# Table 1
class Pesticide(models.Model):
    name = models.CharField(max_length=250)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    location = models.CharField(max_length=255)
    count_pesticide = models.IntegerField()
    name_pesticide = models.CharField(max_length=250, blank=True, null=True)
    name_banned_pesticide = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        verbose_name = "Пестицид"
        verbose_name_plural = "Пестициды"

    def __str__(self):
        return self.name


class StorageStatus(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Состояние хранилища"
        verbose_name_plural = "Состояние хранилищ"

    def __str__(self):
        return self.name


class Analysis(models.Model):
    year = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Год иследевоние"
        verbose_name_plural = "Годы иследевония"

    def __str__(self):
        return self.year


# Table 2
class Storage(models.Model):
    region = models.ForeignKey(Region,
                               on_delete=models.SET_NULL,
                               null=True)
    location = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    status = models.ForeignKey(StorageStatus,
                               on_delete=models.SET_NULL,
                               null=True)
    add_info = models.CharField(max_length=255, null=True)
    obsolete_pesticides = models.CharField(max_length=255, null=True)
    year = models.ForeignKey(Analysis, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Хранилища"
        verbose_name_plural = "Хранилищи"

    def __str__(self):
        return self.name


# Table 17
class Room(models.Model):
    region = models.ForeignKey(Region,
                               on_delete=models.SET_NULL,
                               null=True)
    number_rooms = models.IntegerField()
    number_un_rooms = models.IntegerField()
    number_limit_pdk = models.IntegerField()
    number_above_pdk = models.IntegerField()

    class Meta:
        verbose_name = "Помещения"
        verbose_name_plural = "Помещений"


class FormPreparation(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Форма препарата"
        verbose_name_plural = "Формы препаратов"

    def __str__(self):
        return self.name


class TypeContainer(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Тип контейнера"
        verbose_name_plural = "Тип контейнера"

    def __str__(self):
        return self.name


# Table 1.1
class Preparation(models.Model):
    region = models.ForeignKey(Region,
                               on_delete=models.SET_NULL,
                               null=True)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    name_location = models.CharField(max_length=255)
    trade_name = models.CharField(max_length=255, null=True)
    number = models.IntegerField()
    form = models.ForeignKey(FormPreparation,
                             on_delete=models.SET_NULL,
                             null=True)
    type_container = models.ForeignKey(TypeContainer,
                                       on_delete=models.SET_NULL,
                                       null=True,
                                       related_name="preparation_types")
    status_container = models.ForeignKey(TypeContainer,
                                         on_delete=models.SET_NULL,
                                         null=True,
                                         related_name="preparation_statuses")
    import_year = models.CharField(max_length=10, null=True)
    birth = models.CharField(max_length=255, null=True)
    add_info = models.CharField(max_length=255, null=True)
    note = models.CharField(max_length=255, null=True)

    class Meta:
        verbose_name = "Препарат"
        verbose_name_plural = "Препараты"

    def __str__(self):
        return self.name


class ImportRecord(models.Model):
    file = models.FileField(upload_to='files')