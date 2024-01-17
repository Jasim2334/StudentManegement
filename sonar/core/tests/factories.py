import factory
from faker import Faker
from core.models import Student
import random,secrets

fake = Faker()

class StudentFactory(factory.django.DjangoModelFactory):
    class Meta: 
        model = Student
        
    name = fake.name()
    age = str(secrets.randbelow(7)+18)
    roll = str(secrets.randbelow(4000)+1000)
    marks = str(secrets.randbelow(400)+100)
    gender = secrets.choice(["M","F"])
    subject = secrets.choice(['Python','Java','R','Rust','C','C++'])
