
SESSION_MAP = {}
validate = False

def querySetLoginTime(row) :
    loginTime = ""
    # loginTime = mysql_query("UPDATE" members SET last_login= now() where id = '{$row['id']}'"")
    return loginTime

def loginValidations() :
    #row = {}
    resultTable = None
    # From the members database 
    # Validate _POST['username] and the _POST['password'] 

    if validate == True :
        for row in resultTable :
            SESSION_MAP['login'] = True
            SESSION_MAP['userid'] = row['id']
            SESSION_MAP['firstname'] = row['firstname']
            if row['admin_access'] == 1 :
                SESSION_MAP['admin_access'] = True
            




