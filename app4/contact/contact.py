# Contact CRUD

from .models import Contact


# CREATE

def add_contact (name, email):
    return Contact.objects.create(name=name, email=email)


# READ (one)
def get_contact (pk):
    return Contact.objects.get(pk=pk)


# READ (list)
def list_contacts ():
    return Contact.objects.all()


# READ (query)
def query_contacts (name):
    return Contact.objects.filter(name=name)


# UPDATE
def edit_contact (pk, name, email):
    c = get_contact (pk)
    c.name = name
    c.email = email
    c.save()
    return c


# DELETE
def delete_contact (pk):
    get_contact(pk).delete()
