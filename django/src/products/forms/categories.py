from django import forms
from products.models import Category, Product


class CategoryForm(forms.Form):
    name = forms.CharField(required=True)

    description = forms.CharField(
        widget=forms.widgets.Textarea()
    )


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'description']
