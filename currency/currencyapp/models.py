from django.db import models

class Currency(models.Model):
    title = models.CharField(max_length=50)
    purchase = models.IntegerField()
    sale = models.IntegerField()
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)


    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.name