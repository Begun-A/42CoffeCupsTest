from django.db import models


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
