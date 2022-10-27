import html_layout
import forms

requestObject = {}



def join_code(requestObject):
    # switch request objecgt

    if 'default' in requestObject:
        
        html_layout.include_header("Become a member")
        forms.signupForm()
        html_layout.footer_html()

    elif 'process' :
        errorList = []
        # Check if all the required fields are posted
        errors += "Missing email address"
        fieldsError = True

        # If both emails are posted, validate that they match
        errors  += "Email addresses do not match"
        emailError = True

        # If both passwords are posted, validate that they match
        errors += ""
        passwordError = True

        # Check if email has been used already
        usedEmail = False

        # Verify if user name already exisits

        if len(errorList) > 0 :
            html = forms.signupForm()
            html = html_layout.footer_html()
            return html
        
        # All checks have passed , inser user in database
        # Email user
        # Email admin




