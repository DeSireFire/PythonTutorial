import django.db
import django.db.models

class BookInfo(django.db.models.Model):
    btitle = django.db.models.CharField(max_length=100,unique=True)
    bpubdate = django.db.models.DateField()
    isdelete = django.db.models.BooleanField(default=1)

    def __str__(self):
        return self.btitle

    class Meta():
        db_table = 'bookinfo22222222222222222222222'
        ordering = ['-id']

class HeroInfo(django.db.models.Model):
    hname = django.db.models.CharField(max_length=100)
    hgender = django.db.models.BooleanField()
    hcontent = django.db.models.CharField(max_length=200)
    hbookinfo = django.db.models.ForeignKey(BookInfo)

    def __str__(self):
        return self.hname