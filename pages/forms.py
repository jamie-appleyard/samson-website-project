from django import forms
from .models import Enquiry
from django.forms.widgets import NumberInput, CheckboxSelectMultiple
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Div, Submit, HTML, Field
from crispy_forms.bootstrap import InlineCheckboxes


# Enquiry form built out using crispy form layout tools for added customisation.
class EnquiryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.helper = FormHelper()
                self.helper.form_id = 'EnquiryForm'
                self.helper.form_class = 'enquiry_form container-fluid'
                self.helper.form_method = 'post'
                self.helper.layout = Layout(
                    Div(
                        Div(
                        'name',
                        'contact_number',
                        'email',
                        Submit('submit', 'Submit', css_class="btn btn-md btn-primary mt-5 text-light enq-btn-sm"),
                        css_class="col-sm-12 col-md-5"
                    ),
                        Div(
                            'message',
                            Submit('submit', 'Submit', css_class="btn btn-md btn-primary mt-5 text-light enq-btn-lg"),
                            css_class='col-sm-12 col-md-5'
                    ),
                    css_class="row justify-content-center"
                ),
            )
    class Meta:
        model = Enquiry
        fields = ['name', 'contact_number', 'email', 'message']
        exclude = []

