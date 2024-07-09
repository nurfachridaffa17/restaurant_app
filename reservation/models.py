from django.db import models
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Create your models here.

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    number_of_guests = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.pk:
            original = Reservation.objects.get(pk=self.pk)
            if not original.approved and self.approved:
                self.send_approval_email()
        super().save(*args, **kwargs)

    
    def send_approval_email(self):
        subject = 'Your Request Has Been Approved'
        from_email = 'nurfachridaffa17@gmail.com'
        to_email = self.email
        html_content = render_to_string('Reservation/approved_mail.html', {
            'user': self.name,
            'date': self.date,
            'request': "Reservation Table",
            'support_url': 'https://pesantap.my.id'
        })
        msg = EmailMultiAlternatives(subject, '', from_email, [to_email])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()