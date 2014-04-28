from django.dispatch import receiver
from forms_builder.forms.signals import form_valid


# todo: what if this fails?
@receiver(form_valid)
def set_username(sender=None, form=None, entry=None, **kwargs):
    request = sender
    if request.user.is_authenticated():
        field = entry.form.fields.get(label="Userid")
        field_entry, _ = entry.fields.get_or_create(field_id=field.id)
        field_entry.value = request.user.id
        field_entry.save()
