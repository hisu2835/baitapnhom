from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal')
)

class CheckoutForm(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Họ và Tên'
    }))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Số điện thoại'
    }))
    country = forms.ChoiceField(
        choices=[('', 'Chọn quốc gia')] + list(CountryField().choices),
        widget=CountrySelectWidget(attrs={'class': 'form-control'})
    )
    city = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Tỉnh/Thành phố'
    }))
    district = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Quận/Huyện'
    }))
    ward = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Phường/Xã'
    }))
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Địa chỉ chi tiết'
    }))
    payment_option = forms.ChoiceField(
        choices=[('S', 'Stripe'), ('P', 'PayPal')],
        widget=forms.RadioSelect
    )

class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Mã giảm giá'
    }))

class RefundForm(forms.Form):
    ref_code = forms.CharField()
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4
    }))
    email = forms.EmailField()
