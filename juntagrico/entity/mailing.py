# encoding: utf-8

from django.utils.translation import gettext as _

from django.db import models

class MailTemplate(models.Model):
    '''
    Mail template for rendering
    '''
    name = models.CharField('Name', max_length=100, unique=True)
    template = models.TextField('Template', max_length=1000, default='')
    code = models.TextField('Code', max_length=1000, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('MailTemplate')
        verbose_name_plural = _('MailTemplates')
        permissions = (('can_load_templates', 'Benutzer kann Templates laden'),)