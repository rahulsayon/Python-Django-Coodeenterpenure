from django import forms

from . models import Product

class ProductForm(forms.ModelForm):
     title = forms.CharField(label='',widget=forms.Textarea(attrs={"placeholder":"your title"}))
     description = forms.CharField(required=False,
                                            
                                    widget=forms.Textarea(
                                                            attrs={
                                                            "class":"new-class-name two",
                                                            "rows":20,
                                                            "cols":20,
                                                            "placeholder":"your description",
                                                            "id":"my-id-for-textarea"
                                                            }
                                                         )
                                  )
     price = forms.DecimalField(initial=199.99)
    
     class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
     def clean_title(self,*args,**kwargs):
         title = self.cleaned_data.get("title")
         if  title == "cfe":
             raise forms.ValidationError("This is not valid title")
         return title

     def clean_price(self,*args,**kwargs):
         price = self.cleaned_data.get("price")
         if  price == 1000.0:
             raise forms.ValidationError("This is not valid price")
         return price


class RawProductForm(forms.Form):
    title = forms.CharField(label='',widget=forms.Textarea(attrs={"placeholder":"your title"}))
    description = forms.CharField(required=False,widget=forms.Textarea(
        attrs={
        "class":"new-class-name two",
        "rows":20,
        "cols":20,
        "placeholder":"your description",
        "id":"my-id-for-textarea"
    }
    ))
    price = forms.DecimalField(initial=199.99)