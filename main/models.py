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
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, verbose_name = "Регион")
    location = models.CharField(max_length=255, verbose_name = "Место  расположение")
    count_pesticide = models.IntegerField(verbose_name = "Кол-во пестицидов, кг")
    name_pesticide = models.CharField(max_length=250, blank=True, null=True, verbose_name = "Наименование пестицидов")
    name_banned_pesticide = models.CharField(max_length=250, blank=True, null=True, verbose_name = "Наименование запрещенных пестицидов")

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
                               null=True,
                               verbose_name = "Регион")
    location = models.CharField(max_length=255, verbose_name = "Месторасположение хранилище")
    name = models.CharField(max_length=255, verbose_name = "Название хранилища")
    status = models.ForeignKey(StorageStatus,
                               on_delete=models.SET_NULL,
                               null=True,
                               verbose_name = "Состояние хранилища")
    add_info = models.CharField(max_length=255, null=True, verbose_name = "Дополнительная информация")
    obsolete_pesticides = models.CharField(max_length=255, null=True, verbose_name = "Устаревшие пестициды, кг")
    year = models.ForeignKey(Analysis, on_delete=models.SET_NULL, null=True, verbose_name = "Год")

    class Meta:
        verbose_name = "Хранилища"
        verbose_name_plural = "Хранилищи"

    def __str__(self):
        return self.name


# Table 17
class Room(models.Model):
    region = models.ForeignKey(Region,
                               on_delete=models.SET_NULL,
                               null=True,
                               verbose_name = "Регион")
    number_rooms = models.IntegerField(verbose_name = "Количество складских помещений")
    number_un_rooms = models.IntegerField(verbose_name = "Количество складских помещений без загрязнения")
    number_limit_pdk = models.IntegerField(verbose_name = "Количество территории, где количество пестицидов в пределах ПДК")
    number_above_pdk = models.IntegerField(verbose_name = "Количество территории, где количество пестицидов выше ПДК")

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
                               null=True,
                               verbose_name = "Регион")
    name = models.CharField(max_length=255, verbose_name = "Название препарата")
    location = models.CharField(max_length=255, verbose_name = "Месторасположение хранилища")
    name_location = models.CharField(max_length=255, verbose_name = "Название хранилища")
    trade_name = models.CharField(max_length=255, null=True, verbose_name = "Торговое название")
    number = models.IntegerField(verbose_name = "Количество")
    form = models.ForeignKey(FormPreparation,
                             on_delete=models.SET_NULL,
                             null=True,
                             verbose_name = "Препаративная форма")
    type_container = models.ForeignKey(TypeContainer,
                                       on_delete=models.SET_NULL,
                                       null=True,
                                       related_name="preparation_types",
                                       verbose_name = "Тип контейнера")
    status_container = models.ForeignKey(TypeContainer,
                                         on_delete=models.SET_NULL,
                                         null=True,
                                         related_name="preparation_statuses",
                                         verbose_name = "Состояние контейнера")
    import_year = models.CharField(max_length=10, null=True, verbose_name = "Год ввоза")
    birth = models.CharField(max_length=255, null=True, verbose_name = "Происхождение")
    add_info = models.CharField(max_length=255, null=True, verbose_name = "Дополнительная информация")
    note = models.CharField(max_length=255, null=True, verbose_name = "Замечания")

    class Meta:
        verbose_name = "Препарат"
        verbose_name_plural = "Препараты"

    def __str__(self):
        return self.name


class ImportRecord(models.Model):
    file = models.FileField(upload_to='files')