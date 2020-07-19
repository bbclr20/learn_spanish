from django.db import models
from django.utils import timezone

# Create your models here.
class Vocab(models.Model):
    
   
    spanish = models.CharField(max_length=20)
    english = models.CharField(max_length=20)
    chinese = models.CharField(max_length=20, null=True)
    
    # annoying
    classes_choices = [
            ("Ani", "Animal"), 
            ("Fd", "Food"),
            ("Oth", "Other")
        ]

    lookup_dict = {}
    for v,k in classes_choices:
        lookup_dict[k] = v
    
    classes = models.CharField(
        max_length=20,
        choices=classes_choices,
        default=classes_choices[-1][0]
    )

    pub_date = models.DateTimeField(default=timezone.now())

    class Meta:
        ordering = ('pub_date',)

    def __str__(self):
        return self.spanish
