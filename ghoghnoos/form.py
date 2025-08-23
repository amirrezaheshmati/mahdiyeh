from django import forms

from .models import Product , Category , Subset , Special , Discount , Colors, Size , Order

class AddProduct(forms.ModelForm) :
    class Meta :
        model = Product
        fields = ["name" , "price" , "picture" , "describe"]
        labels = {"name" : "اسم کالا" , "price" : "قیمت" ,
                "picture" : "تصویر" , "describe" : "توضیحات"}
    
    def clean_name(self) :
        name = self.cleaned_data.get("name")
        qs = Product.objects.filter(name = name)
        
        if self.instance.pk :
            qs = qs.exclude(pk = self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("این اسم قبلا در بخش کالاها استفاده شده است")
        if Special.objects.filter(name = name).exists() :
            raise forms.ValidationError("این اسم قبلا در بخش فروش ویژه انتخاب شده است")
        if Discount.objects.filter(name = name).exists() :
            raise forms.ValidationError("این اسم قبلا در بخش تخفیف ها استفاده شده است")
        if Category.objects.filter(name = name).exists() :
            raise forms.ValidationError("اسم محصولات باید با اسم دسته بندی متفاوت باشد")
        if Subset.objects.filter(name = name).exists() :
            raise forms.ValidationError("اسم محصولات باید با اسم زیر مجموعه ها متفاوت باشد")
        return name
        
class AddCategory(forms.ModelForm) :
    class Meta :
        model = Category
        fields = ["name"]
        labels = {"name" : "اسم دسته بندی"}
    
    def clean_name(self) :
        name = self.cleaned_data.get("name")
        if Product.objects.filter(name = name).exists():
            raise forms.ValidationError("این اسم قبلا در بخش کالاها استفاده شده است")
        if Special.objects.filter(name = name).exists() :
            raise forms.ValidationError("این اسم قبلا در بخش فروش ویژه انتخاب شده است")
        if Discount.objects.filter(name = name).exists() :
            raise forms.ValidationError("این اسم قبلا در بخش تخفیف ها استفاده شده است")
        if Category.objects.filter(name = name).exists() :
            raise forms.ValidationError("اسم محصولات باید با اسم دسته بندی متفاوت باشد")
        if Subset.objects.filter(name = name).exists() :
            raise forms.ValidationError("اسم محصولات باید با اسم زیر مجموعه ها متفاوت باشد")
        return name

class AddSubset(forms.ModelForm) :
    class Meta :
        model = Subset
        fields = ["name"]
        labels = {"name" : "اسم زیر مجموعه"}
    
    def clean_name(self) :
        name = self.cleaned_data.get("name")
        if Product.objects.filter(name = name).exists():
            raise forms.ValidationError("این اسم قبلا در بخش کالاها استفاده شده است")
        if Special.objects.filter(name = name).exists() :
            raise forms.ValidationError("این اسم قبلا در بخش فروش ویژه انتخاب شده است")
        if Discount.objects.filter(name = name).exists() :
            raise forms.ValidationError("این اسم قبلا در بخش تخفیف ها استفاده شده است")
        if Category.objects.filter(name = name).exists() :
            raise forms.ValidationError("اسم محصولات باید با اسم دسته بندی متفاوت باشد")
        if Subset.objects.filter(name = name).exists() :
            raise forms.ValidationError("اسم محصولات باید با اسم زیر مجموعه ها متفاوت باشد")
        return name

class AddSpecial(forms.ModelForm) :
    class Meta :
        model = Special
        fields = ["name" , "price" , "picture" , "describe"]
        labels = {"name" : "اسم کالا" , "price" : "قیمت" ,
                "picture" : "تصویر" , "describe" : "توضیحات"}
    
    def clean_name(self) :
        name = self.cleaned_data.get("name")
        qs = Special.objects.filter(name = name)
        
        if self.instance.pk :
            qs = qs.exclude(pk = self.instance.pk)
        if Product.objects.filter(name = name).exists() :
            raise forms.ValidationError("این اسم قبلا در بخش کالاها استفاده شده است")
        if qs.exists():
            print("amir")
            raise forms.ValidationError("این اسم قبلا در بخش فروش ویژه انتخاب شده است")
        if Discount.objects.filter(name = name).exists() :
            raise forms.ValidationError("این اسم قبلا در بخش تخفیف ها استفاده شده است")
        if Category.objects.filter(name = name).exists() :
            raise forms.ValidationError("اسم محصولات باید با اسم دسته بندی متفاوت باشد")
        if Subset.objects.filter(name = name).exists() :
            raise forms.ValidationError("اسم محصولات باید با اسم زیر مجموعه ها متفاوت باشد")
        return name

class AddDiscount(forms.ModelForm) :
    class Meta :
        model = Discount
        fields = ["name" , "price1", "price" , "picture" , "describe"]
        labels = {"name" : "اسم کالا" , "price" : "قیمت اصلی" , "price1" : "قیمت بیشتر(تخفیف خورده)",
                "picture" : "تصویر" , "describe" : "توضیحات"}
    
    def clean_name(self) :
        name = self.cleaned_data.get("name")
        qs = Special.objects.filter(name = name)
        
        if self.instance.pk :
            qs = qs.exclude(pk = self.instance.pk)
        if Product.objects.filter(name = name).exists():
            raise forms.ValidationError("این اسم قبلا در بخش کالاها استفاده شده است")
        if Special.objects.filter(name = name).exists() :
            raise forms.ValidationError("این اسم قبلا در بخش فروش ویژه انتخاب شده است")
        if qs.exists() :
            raise forms.ValidationError("این اسم قبلا در بخش تخفیف ها استفاده شده است")
        if Category.objects.filter(name = name).exists() :
            raise forms.ValidationError("اسم محصولات باید با اسم دسته بندی متفاوت باشد")
        if Subset.objects.filter(name = name).exists() :
            raise forms.ValidationError("اسم محصولات باید با اسم زیر مجموعه ها متفاوت باشد")
        return name

class AddColor(forms.ModelForm) :
    class Meta :
        model = Colors
        fields = ["name_color" , "price_color" , "count"]
        labels = {"name_color" : "اسم رنگ" , "price_color" : "قیمت" , "count" : "تعداد موجودی"}

class AddSize(forms.ModelForm) :
    class Meta :
        model = Size
        fields = ["height" , "width" , "colm" , "price_size" ,"count"]
        labels = {"height" : "طول" , "width" : "عرض" ,
                  "colm" : "ارتفاع" , "price_size" : "قیمت" , "count" : "تعداد موجودی"}

class OrderForm(forms.Form) :
    color = forms.ModelChoiceField(queryset=Colors.objects.none() , empty_label="انتخاب رنگ")
    size = forms.ModelChoiceField(queryset=Size.objects.none() , empty_label="انتخاب سایز")
    
    def __init__(self , *args , **kwargs) :
        product = kwargs.pop("product")
        super().__init__(*args , **kwargs)
        self.fields["color"].queryset = product.colors_set.all()
        self.fields["size"].queryset = product.size_set.all()
        
class OrderForm2(forms.ModelForm) :
    class Meta :
        model = Order
        fields = ["count" , "describe"]
        labels = {"count" : "تعداد" , "describe" : "ملاحظات"}