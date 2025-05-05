from django import forms

class ResumeUploadForm(forms.Form):
    resume_image = forms.ImageField(label='Upload Resume Image', required=True)

class AnswerForm(forms.Form):
    answer = forms.CharField(label='Your Answer:', required=True)
    
from django import forms
from django.core.validators import EmailValidator, RegexValidator

class LoginForm(forms.Form):
    user_type = forms.ChoiceField(choices=[('candidate', 'Candidate'), ('recruiter', 'Recruiter')], widget=forms.HiddenInput)
    email = forms.EmailField(max_length=254, validators=[EmailValidator()], widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class CandidateSignupForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    email = forms.EmailField(max_length=254, validators=[EmailValidator()], widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    phone_number = forms.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be valid.")],
        widget=forms.TextInput(attrs={'placeholder': 'Phone Number'})
    )
    password = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class RecruiterSignupForm(forms.Form):
    company_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Company Name'}))
    recruiter_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Recruiter Name'}))
    email = forms.EmailField(max_length=254, validators=[EmailValidator()], widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    phone_number = forms.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be valid.")],
        widget=forms.TextInput(attrs={'placeholder': 'Phone Number'})
    )
    password = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    
class CandidateProfileForm(forms.Form):
    skills = forms.CharField(
        max_length=500,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Skills (e.g., Python, Java, Communication)'})
    )
    experience = forms.CharField(
        max_length=2000,
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Experience (e.g., Software Engineer at XYZ, 2 years)'})
    )
    projects = forms.CharField(
        max_length=2000,
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Projects (e.g., Built a web app using Django)'})
    )
    
    
class JobPostingForm(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Job Title'}))
    description = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(attrs={'placeholder': 'Job Description'})
    )
    location = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Location (e.g., Remote, New York)'}))
    skills_required = forms.CharField(
        max_length=500,
        widget=forms.TextInput(attrs={'placeholder': 'Skills Required (e.g., Python, SQL)'})
    )
    
class ScheduleInterviewForm(forms.Form):
    interview_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'placeholder': 'Select date and time'})
    )
    interview_link = forms.URLField(
        max_length=200,
        widget=forms.URLInput(attrs={'placeholder': 'Interview Link (e.g., Zoom, Google Meet)'})
    )
    notes = forms.CharField(
        max_length=1000,
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Additional Notes (optional)'})
    )