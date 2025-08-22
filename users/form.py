from django import forms

from .models import Acount

class Profill(forms.ModelForm) :
    class Meta :
        model = Acount
        fields = ["name" , "number_phone1" , "number_phone2" ,
                 "post_code" ,  "addres"]
        labels = {"name" : "name" , "number_phone1" : "number phone" ,
                  "number_phone2" : "another number phone" ,
                  "post_code" : "post code" , "addres" : "addres"}