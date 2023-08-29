import yaml
import hashlib

with open('./credentials.yaml', 'r') as f:
    VALID_CREDENTIALS = yaml.safe_load(f)

def is_valid_credentials(username, password):
    user_stored_cred = None

    for cred in VALID_CREDENTIALS:
        if cred['username'] == username:
            user_stored_cred = cred
            break
    
    if user_stored_cred is None:
        return False
    
    #unhash the password
    
    password_hash = hashlib.sha256(password.encorde('utf-8')).hexdigest()

    if cred['password_hash'] == password_hash:
        return True
    return False

if __name__ == "__main__":
    username = input("What is your username?\n")
    password = input("What is your password?\n")

    if is_valid_credentials(username, password):
        print("I smell good")
    else:
        print("Nice try bud")