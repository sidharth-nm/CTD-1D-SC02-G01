# imports
import data_handler as dh

# Validates & verifies credentials; auxilliary function for login_frontend.py
def verify_credentials(username, password):
  # Basic validation check
  if len(username.strip()) <= 0 or len(password.strip()) <= 0:
    #st.error("Username and password fields cannot be blank, try again.")
    return False

  else:
    user_record = dh.get_user_details(username)

    # Verifies whether credentials are correct or not
    # If exist + username & password matched, yields True
    return ( len(user_record) > 0 and user_record['password'] == password)