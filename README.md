# infolabs


## Diagram
See `docs/strucrure.png`

## Models

DomainCheck:
 * _id
 * domain = CharField()
 * state = [CharField](https://docs.djangoproject.com/en/1.11/ref/models/fields/#django.db.models.Field.choices)(choices=...)
 * create_date = [DateTimeFied](https://docs.djangoproject.com/en/1.11/ref/models/fields/#django.db.models.DateTimeField)
 * feature = [ForeignKey](https://docs.djangoproject.com/en/1.11/ref/models/fields/#django.db.models.ForeignKey)()
 
 
 Feature:
  * _id
  * nume = CharField()
  * value = [JsonField](https://docs.djangoproject.com/en/1.11/ref/contrib/postgres/fields/#django.contrib.postgres.fields.JSONField)()
  * compare_value = JsonField()
