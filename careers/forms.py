from django import forms
from careers.models import JobApplication, Career, TrainingInterest
from django.forms.widgets import NumberInput, CheckboxSelectMultiple
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Div, Submit, HTML, Field
from crispy_forms.bootstrap import InlineCheckboxes

#Model form tied to the JobApplication Model, utilising crispy forms tools to customise this form in detail
class ApplicationForm(forms.ModelForm):
        def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.helper = FormHelper()
                self.helper.form_id = 'applicationForm'
                self.helper.form_class = 'application_form container-fluid'
                self.helper.form_method = 'post'
                self.helper.enctype = 'multipart/form-data'
                self.helper.layout = Layout(
                        Div(
                                Div(
                                        HTML("<h1 class='application-title'>Application Form</h1>"),
                                ),
                                Div(
                                        Div(
                                                HTML("<h2 class='text-center form-title'>About you</h2>"),
                                                'first_name',
                                                'last_name',
                                                'email_address',
                                                'mobile_number',
                                                css_class = "about_you",  
                                        ),
                                        css_class = "col-12 col-sm-12 col-md-6",
                                ), 
                                Div(
                                        Div(
                                                HTML("<h2 class='text-center form-title'>Your Location</h2>"),
                                                'first_line',
                                                'second_line',
                                                'town',
                                                'county',
                                                'postcode',
                                                css_class = "location",
                                        ),
                                        css_class = "col-12 col-sm-12 col-md-6"
                                ),
                                css_class = "row text_row mb-5 justify-content-around",        
                        ),
                        Div(
                                Div(
                                        HTML("<h1 class='form-title'>Please select which of the following apply</h1>"),
                                        css_class = "col-12 mb-3 text-center",
                        ),
                                Div(
                                        "uk_bank_account",
                                        "criminal_offences",
                                        "over_18",
                                        css_class = "col-12 col-sm-12 col-md-6 app_checkboxes"
                        ),
                                Div(
                                        "right_to_work",
                                        "sia_badge",
                                        "address_history",
                                        "working_history",
                                        css_class = "col-12 col-sm-12 col-md-6 app_checkboxes"
                        ),css_class = "row app_checkboxes_row mt-5 mb-5", 
                        ),
                        Div(
                                Div(
                                        HTML("<h1 class='form-title'>SIA Badges currently held</h1>"),
                                        css_class="col-12 text-center"
                                ),
                                Div(
                                        Field('sia_badges'),
                                        css_class="col-12 sia_badges",
                                ),
                                css_class = "row sia_row mt-5 mb-5",
                        ),
                        Div(
                                Div(
                                        HTML("<h1 class='mt-3 mb-2 form-title'>Identification</h1>"),
                                        HTML("<h5 class='mb-4 mt-4 lead id-note'>ID will be required upon interview to vet you and prove a right to work.  Labels with * must be less than 3 months old, those with ** must be issued in the last 12 months. When both counters are green the ID provided will be suitable."),
                                        css_class="col-12 col-md-11 text-center",
                                ),
                                Div(
                                        Div(
                                                HTML("<h1 id='groupATotal'>00/00</h1>"),
                                                css_class = "col-12 id-a-counter text-center",
                                        ),
                                        InlineCheckboxes('group_a'),
                                        css_class = "col-12 col-sm-12 col-md-4 group_a"
                                ),
                                Div(
                                        Div(
                                                HTML("<h1 id='groupBTotal'>00/05</h1>"),
                                                css_class = "col-12 id-b-counter text-center",
                                        ),
                                        InlineCheckboxes('group_b'),
                                        css_class = "col-12 col-sm-12 col-md-8 group_b"
                                ),
                                Div(
                                        HTML("<h3>Please select more forms of ID</h3>"),
                                        css_class='identity-error col-12',
                                ),
                                css_class = "row identification_row justify-content-center mt-5 mb-5"
                        ),
                        Div(
                                Div(
                                        HTML("<h2 class='form-title'>Uploading a CV is optional but it will help your application for this position</h2>"),
                                        css_class="col-11 col-sm-11 col-md-8 text-center"
                                ),
                                Div(
                                        Field('cv', css_class="form-control form-control-lg"),
                                        css_class = "col-12 col-sm-10 col-md-6 cv-upload mt-5"
                                ),
                                css_class = "row cv_row mt-5 mb-5 pb-5 justify-content-center"  
                        ),
                        Div(
                                Div(
                                        Submit('submit', 'Submit', css_class = "btn btn-lg btn-success app-submit"),
                                        css_class="col-12"
                                        
                                ),
                                css_class = "submit-row row mt-5"
                        )   
                )

        class Meta:
                model = JobApplication
                exclude = ['user', 'job_reference', 'result']
                widgets = { 'sia_badges' : CheckboxSelectMultiple()}
                labels = {
                        'uk_bank_account' : "I have a UK bank account",
                        'criminal_offences' : "I have been convicted of a criminal offence",
                        'over_18': 'I am over 18',
                        'right_to_work' : 'I have the right to work in the UK',
                        'sia_badge' : 'I have an SIA badge',
                        'address_history' : 'I can provide an 5 year address history',
                        'working_history' : 'I can provide a 5 year working history'
                }     
        
#Model Form for listing a new vacancy through the dashboard
class NewVacancyForm(forms.ModelForm):
        class Meta:
                model = Career
                exclude = ['job_apply_by_date', 'job_date_posted',
                'job_posted_by', 'number_of_applications']

#Model Form to allow visitors to the site to register their interest in training with Samson, leaving their details so that they can
#be contacted at a later date.
class TrainingInterestForm(forms.ModelForm):
        def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.helper = FormHelper()
                self.helper.form_id = 'TrainingInterestForm'
                self.helper.form_class = 'ti_form row'
                self.helper.form_method = 'post'
                self.helper.enctype = 'multipart/form-data'
                self.helper.layout = Layout(
                        Div(
                                Field('name', css_class="inline-field"),
                                Field('email', css_class="inline-field"),
                                css_class = "col-12 inline-fields"
                        ),
                        Div(
                                Field("course", css_class="inline"),
                                Submit("submit", "Submit", css_id="ti-submit"),
                                HTML("<p class='ti-submit-success'>Submitted, thank you.</p>"),
                                css_class = "col-12" 
                        )
                )

        class Meta:
                model = TrainingInterest
                exclude = []
    
    
    
    
    
    
    


