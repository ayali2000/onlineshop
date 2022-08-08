from dataclasses import fields
from django import forms
from django import forms

from store.models import Items
from store.models import OrderItem



class SellForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['Name','Category','Price','Description','Location','Image']
    
    Name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'name'
    }))

    
    Description = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Product description'
    }))
    
    Price = forms.DecimalField(widget=forms.NumberInput(attrs={
        'class':'form-control',
        'placeholder':'Price'
    }))
    
    Location = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Location'
    }))
    


class OrederForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields="__all__"
        
    Name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Your name'
    }))  
    
    Phone_num = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Phone number'
    }))  
    
    Quantity = forms.IntegerField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Quantity'
    }))  
    
    Address = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'Address',
        'rows':4,
    }))       
    
    