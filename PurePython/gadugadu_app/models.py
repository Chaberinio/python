from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=128)
    surName = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.name} {self.surName}'

class Message(models.Model):
    description = models.CharField(max_length=140)
    sender = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='sender_set')
    reciver = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='reciver_set')

    def __str__(self):
        return f'Wiadomość od: {self.sender} Do: {self.reciver} O treści: {self.description}'

