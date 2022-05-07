from django.db import models

TYPE = (
    (1, 'Большой'),
    (2, 'Средний'),
    (3, 'Маленький')
)


class Conference(models.Model):
    name = models.CharField(max_length=150)
    conference_type = models.IntegerField(choices=TYPE, null=True)
    quantity = models.IntegerField()
    projector = models.BooleanField(default=True)
    conditioner = models.BooleanField(default=True)
    board = models.BooleanField(default=True)
    description = models.TextField(null=True)

    def __str__(self):
        return f'{self.id}. {self.conference_type}'


class Image(models.Model):
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE,
                                   blank=True, null=True)
    image = models.ImageField(upload_to='conference')

    def __str__(self):
        return f'{self.id} - {self.conference}'
