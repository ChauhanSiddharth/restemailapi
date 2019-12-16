from django.db import models

# Create your models here.
class EmailModel(models.Model):
	sender_email = models.EmailField(max_length=100)
	receiver_email = models.EmailField(max_length=100)
	receiver_name = models.CharField(max_length=100)
	subject = models.CharField(max_length=100)
	message = models.TextField()
	message_delete = models.BooleanField(default=False)
	message_archive = models.BooleanField(default=False)
	message_sent = models.BooleanField(default=False)

	def __str__(self):
		return self.subject