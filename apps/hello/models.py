from django.db import models
from PIL import Image


# Create your models here.
class Contact(models.Model):
    class Meta:
        db_table = 'Contact'
        verbose_name = u'Contact'
        verbose_name_plural = u'Contacts'

    def __unicode__(self):
        return u'{0} {1}'.format(self.name, self.surname)

    name = models.CharField(max_length=20, blank=False, )
    surname = models.CharField(max_length=20, blank=True, default='', )
    birth_date = models.DateField(blank=False, verbose_name=u'Data of birth',
                                  null=True, )
    email = models.EmailField(blank=False, verbose_name=u'Email', null=False)
    skype = models.CharField(max_length=20, blank=True, null=True, )
    jabber = models.EmailField()
    other = models.TextField(max_length=50, blank=True, null=True, )
    bio = models.TextField(max_length=256, blank=True, null=True)
    photo = models.ImageField(upload_to='images', blank=True, null=True,
                              default='/')

    def save(self, *args, **kwargs):
        """Save Photo after ensuring it is not blank.  Resize as needed.
        """
        size = (200, 200)
        if not self.id and not self.photo:
            return
        super(Contact, self).save(*args, **kwargs)
        try:
            filename = self.photo.path
            image = Image.open(filename)

            image.thumbnail(size, Image.ANTIALIAS)
            image.save(filename)
        except:
            pass


class RequestLog(models.Model):
    class Meta:
        db_table = 'RequestLog'

    def __unicode__(self):
        return u'{0} {1} {2}'.format(self.pk, self.method, self.path)

    method = models.CharField(max_length=20)
    path = models.CharField(max_length=1024)
    remote_addr = models.IPAddressField()
    time = models.DateTimeField(auto_now=True)


class ObjectsDBLog(models.Model):
    action = models.CharField(max_length=15)
    model = models.CharField(max_length=30)
    date_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'{0} {1}'.format(self.model, self.action)
