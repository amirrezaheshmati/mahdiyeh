from django import forms
from PIL import Image
from .models import Product , Category , Subset ,\
Special , Discount , Colors, Size , Order , TrackingCode , Comments , Replay

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
    
    def clean_picture(self):
        photo = self.cleaned_data.get('picture')

        if photo:
            img = Image.open(photo)
            width, height = img.size
            ratio = width / height

            expected_ratio = 5 / 4  # نسبت مورد نظر

            # کمی خطای کوچک مجاز (برای جلوگیری از مشکل اعشار)
            if not (abs(ratio - expected_ratio) < 0.01):
                raise forms.ValidationError("نسبت تصویر باید 5 به 4 باشد.")

        return photo
        
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

    def clean_picture(self):
        photo = self.cleaned_data.get('picture')

        if photo:
            img = Image.open(photo)
            width, height = img.size
            ratio = width / height

            expected_ratio = 5 / 4  # نسبت مورد نظر

            # کمی خطای کوچک مجاز (برای جلوگیری از مشکل اعشار)
            if not (abs(ratio - expected_ratio) < 0.01):
                raise forms.ValidationError("نسبت تصویر باید 5 به 4 باشد.")

        return photo
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

    def clean_picture(self):
        photo = self.cleaned_data.get('picture')

        if photo:
            img = Image.open(photo)
            width, height = img.size
            ratio = width / height

            expected_ratio = 5 / 4  # نسبت مورد نظر

            # کمی خطای کوچک مجاز (برای جلوگیری از مشکل اعشار)
            if not (abs(ratio - expected_ratio) < 0.01):
                raise forms.ValidationError("نسبت تصویر باید 5 به 4 باشد.")

        return photo
    
class AddColor(forms.ModelForm) :
    class Meta :
        model = Colors
        fields = ["name_color" , "price_color" , "count"]
        labels = {"name_color" : "اسم رنگ" , "price_color" : "قیمت" , "count" : "تعداد موجودی"}

class AddSize(forms.ModelForm) :
    class Meta :
        model = Size
        fields = ["height" , "width" , "colm" , "price_size"]
        labels = {"height" : "طول" , "width" : "عرض" ,
                  "colm" : "ارتفاع" , "price_size" : "قیمت"}
        
class OrderForm(forms.ModelForm) :
    color = forms.ModelChoiceField(
        queryset=Colors.objects.none(),  # اول خالی
        empty_label="انتخاب رنگ"
    )
    size = forms.ModelChoiceField(
        queryset=Size.objects.none(),
        empty_label="انتخاب سایز"
    )
    class Meta :
        model = Order
        fields = ["count" , "color" , "size", "describe"]
        labels = {"count" : "تعداد" ,"color" : "رنگ" , "size" : "اندازه", "describe" : "ملاحظات"}
    
    def __init__(self, *args, **kwargs):
        product = kwargs.pop("product", None)
        super().__init__(*args, **kwargs)
        if product:
            self.fields["color"].queryset = product.colors_set.all()
            self.fields["size"].queryset = product.size_set.all()

class TrackingForm(forms.ModelForm) :
    class Meta :
        model = TrackingCode
        fields = ["link" , "tracking_code"]
        labels = {"link" : "لینک رهگیری" , "tracking_code" : "کد رهگیری"}
        
class CommentAdded(forms.ModelForm) :
    class Meta :
        model =  Comments
        fields = ["text"]
        labels = {"text" : "comment"}

class ReplayAdded(forms.ModelForm) : 
    class Meta :
        model = Replay
        fields = ["text"]
        labels = {"text" : "Replay"}