import index
import html_layout
import forms

reuqestKey = ['validate']
requestObject = {}


def include_index_html():
    index.header_html()
    # Include body
    index.footer_html()
    return None


def include_login_form():
    # Where does this state gp ?
    # <tr -  input user name,  type text >
    # <tr -  input password  , type password >
    # <tr -  "validate",  'submit' >

    return None


def loggedIn_code():
    return None


def queryAndValidate(inputList):
    # Queries a table  basedon an inputList
    return None

def lost_password_code() :
    html_layout.header_html("RESET PASSWORD")
    if 'recover' in requestObject :
        updateSuccess = False
        # From email address go to the database and reset password
        if updateSuccess == False :
            print("Password can not be reset")
        else :
            print("Please check your email for your new password")
            forms.
            
            

def login_code():
    # switch request objecgt
    
    if 'validate' in requestObject:
        #  query members table  based on 'username' and 'password'  e.g  md5('($_POST['password'])')
        validate = queryAndValidate('<userName>', '<password')

        if validate == True:
            # Update the _SESSION[member_attributes] via fetching the row attribute from the member attributes
            a = None
        else:
            # Specify in the header - " Login failed"
            print()

        loggedIn_code()
        include_footer_html()
    else:
        # Generate login form
        # Include header
        include_login_form()
        include_footer_html()


def logout_code() :
    html = ""
    return html

def loginPage():
    # This page contains the html
    include_index_html()
    return None
