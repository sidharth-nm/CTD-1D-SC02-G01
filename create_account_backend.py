import data_handler as dh

# Verifies credentials (input validation is handled in create_account_frontend). Auxilliary function
# If acceptable, returns True; else, returns False
def verify_credentials(username):
  # Checks if username is already in use
  if len(dh.get_user_details(username)) > 0:
    return False 
  else:
    return True