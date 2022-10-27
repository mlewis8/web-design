
# Receiving the post call from the web
POST = {}
submit = {}
hiddenInput = {}

def signupForm() :
    # Create a form which will be able to post the following :
    html = ""
    inputs = ['first_name','last_name','email1','emailAddress2','bio']

    #<td  input_name = 'first_name' type = 'text' ....

    paswordInput = ['password','retype_password']
    submit['id'] = 'req'
    submit['value'] = 'process'
    return html

def lostPasswordForm() :
    html = ""
    print("If you have lossed your password you may enter your email and a new password will be sent to you")
    inputs = ['email_address']

    #input name, value
    hiddenInput['id'] = 'req'
    hiddenInput['value'] = 'recovery'
    return html

def loginForm() :
    html = ""
    return html


def registrationForm() :
    html = ""
    return html


def dontationForm() :
    # This task is assigned to ....
    html = ""
    return html











