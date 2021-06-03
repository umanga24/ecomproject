from django import forms
from .models import Order, Customer, Product
from django.contrib.auth.models import User

class CheckOutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["order_by", "shipping_address", "mobile", "Email"]


class CustomerRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(widget=forms.EmailInput())

    class Meta:
         model = Customer
         fields = ("username", "password", "email", "full_name", "address")

    def clean_username(self):
        uname = self.cleaned_data.get("username")
        if User.objects.filter(username = uname).exists():
            raise forms.ValidationError(
                "Customer with username already exits.")
        return uname

class CustomerLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ProductForm(forms.ModelForm):
    more_images = forms.FileField(required=False, widget=forms.FileInput(attrs={
        "class": "form-control",
        "multiple" : True
    }))

    class Meta:
        model = Product
        fields = ["title", "slug", "category", "image", "more_images", "market_price", "selling_price","description","warrenty","return_policy"]

        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder" : "Enter the product title...eg: Mens Blazer"}),
            "slug": forms.TextInput(attrs={
                "placeholder": "eg: mens-blazer"}),

            "description": forms.Textarea(attrs={
                "placeholder": "Description........"}),

            "image": forms.ClearableFileInput(attrs={
                "class": "form-control"}),
        }
class PasswordForgotForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "class":"form-control",
        "placeholder" : "Enter the email use in customer account"
    }))

    def clean_email(self):
        e = self.cleaned_data.get("email")
        if Customer.objects.filter(user__email=e).exists():
            pass
        else:
            raise forms.ValidationError(
                "Customer with this account doesnot exists...")
        return e

class PasswordResetForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-class',
        'autocomplete': 'new-password',
        'placeholder' : 'Enter new Password',
        }), label="New Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-class',
        'autocomplete': 'new-password',
        'placeholder' : 'Confirm Password',
        }), label=" Confirm New Password")

    def clean_confirm_new_password(self):
        new_password = self.cleaned_data.get("new_password")
        confirm_new_password = self.cleaned_data.get("confirm_password")
        if new_password != confirm_new_password:
            raise forms.ValidationError(
                "New password did not match!")
        return confirm_new_password

