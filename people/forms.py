"""User forms."""

# Django
from django import forms

# Models
from django.contrib.auth.models import User
from people.models import Advisers


class AdviserRegisterForm(forms.Form):
    """Sign up form."""

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)
    #email = forms.CharField(min_length=2, max_length=50)

    email = forms.EmailField(
        min_length=6,
        max_length=150
    )

    phone_number = forms.IntegerField()

    # 1=DNI 2=CET 3=OTROS
    document_type = forms.IntegerField()
    document_number= forms.CharField(max_length=20)
    
    # asesor=1, supervisor=2, visualizador=3, 4=generncial
    type_user = forms.IntegerField()

    def clean_phone_number(self):
        """phone number only 9 caracteres"""
        phone_number  = self.cleaned_data['phone_number']
        phone_number_str=f'{phone_number}a'
        if len(phone_number_str) != 10:
            raise forms.ValidationError('El Telefono debe tener 9 caracteres')
        return phone_number

    def clean_email(self):
        """Validaciones de email"""
        email = self.cleaned_data['email']
        email_taken = User.objects.filter(email=email).exists()
        if email_taken:
            raise forms.ValidationError("Email esta siendo utilizado")
        return email

    def clean_document_number(self):
        """Validaciones de email"""
        document_number = self.cleaned_data['document_number']
        if len(document_number) != 8:
            raise forms.ValidationError("Numero debe tener 8 caracteres")

        document_number_taken = Advisers.objects.filter(document_number=document_number).exists()

        if document_number_taken:
            raise forms.ValidationError("Numero de documento está siendo utilizado")
        return document_number

    #raise forms.ValidationError({'email':['emailperrora.',]})
    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        #creando usuario
        user = User.objects.create_user(
            username=data['document_number'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            password='Botslab123.'
            
            )
        
        #Creando adviser
        adviser = Advisers(
            user=user,
            phone_number=data['phone_number'],
            document_type=data['document_type'],
            document_number=data['document_number'],
            type_user=data['type_user']
        )

        adviser.save()

class AdviserUpdateForm(forms.Form):

    first_name = forms.CharField(min_length=2, max_length=5)
    last_name = forms.CharField(min_length=2, max_length=5)
    email = forms.CharField(
        min_length=6,
        max_length=10
    )

class AdviserListForm(forms.ModelForm):
    """Post model form."""
    
    class Meta:
        """Form settings."""

        model = Advisers
        fields = ('user', 'document_number', 'phone_number')