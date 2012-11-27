import jinja2
from tower import ugettext as _, ugettext_lazy as _lazy

from django import forms

from gameon.users.models import Profile


class ProfileForm(forms.ModelForm):
    name = forms.CharField(required=True, error_messages={
        'required': _lazy(u'A Display Name is required.')
    })

    class Meta:
        model = Profile
        fields = ('name',)


class ProfileCreateForm(ProfileForm):
    agreement = forms.BooleanField(required=True, error_messages={
        'required': _lazy(u'You must agree to the privacy policy to register.')
    })

    def __init__(self, *args, **kwargs):
        super(ProfileCreateForm, self).__init__(*args, **kwargs)

        self.fields['agreement'].label = jinja2.Markup(_(
            u"I'm okay with Mozilla handling this info as you explain in your "
            u"<a href='{url}' target='_blank'>privacy policy</a>.")).format(
                url='http://www.mozilla.org/en-US/privacy-policy.html')