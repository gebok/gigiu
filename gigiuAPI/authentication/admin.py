from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from authentication.models import User

# Register your models here.


class UserCreationForm(forms.ModelForm):
    """ A form for creating new users. Includes all the required fields, plus a repeated password. """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', )

    def clean_password2(self):
        """ Check that the two password entries match """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        """ Save the password in hashed format """
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """ A form for updating users. Includes all the fields on the user, but replaces the password 
    field with admin's disabled hashed display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'is_active', 'admin', 'staff')


class UserAdmin(BaseUserAdmin):
    """ The forms to change and add user instances """
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used for displaying the User model
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User
    list_display = ('email', 'first_name', 'last_name',
                    'admin', 'staff', 'created_at', 'updated_at')
    list_filter = ('email',)
    fieldsets = (
        (None, {"fields": ('email', 'password',)}),
        ('Personal info', {'fields': ('first_name', 'last_name',)}),
        ('Permissions', {"fields": ('admin', 'staff')}),
    )

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin overrides
    # get_fieldsets to use this attribute when creating a user
    add_fieldsets = (
        (None, {'classes': ('wide',),
                'fields': ('email', 'password1', 'password2', 'first_name', 'last_name')
                }),
    )

    search_fields = ('email', )
    ordering = ('email', )
    filter_horizontal = ()


# Now register the new UserAdmin ...
admin.site.register(User, UserAdmin)

# .... and since we're not using Django's built-in permissions,
# unregister the Group model admin
# admin.site.unregister(Group)
