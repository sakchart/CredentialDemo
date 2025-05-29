# Example Python script with various credential-like variables for testing

# Hardcoded API Keys
api_key = "AIzaSyD-EXAMPLEKEY-1234567890abcdefghi"
aws_access_key_id = "AKIAIOSFODNN7EXAMPLE"
aws_secret_access_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# Passwords
db_password = "SuperSecret123!"
adminPassword = "admin@1234"
ftp_pass = "ftp_password_here"

# Tokens
jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
slack_bot_token = "xoxb-123456789012-1234567890123-AbCdEfGhIjKlMnOpQrStUvWx"

# Credentials in dictionary
credentials = {
    "username": "admin",
    "password": "P@ssw0rd!"
}

# Embedded in URL
db_url = "postgresql://user:hardcodedpassword@localhost:5432/mydb"

# Encoded (but still hardcoded) values
import base64
encoded_password = base64.b64encode(b"base64password123").decode("utf-8")

# Placeholder/False Positive variables
hint_password = "NotARealPassword"
fake_token = "thisisnotasecretreally"

# Function returning credentials
def get_credentials():
    return {
        "user": "dev_user",
        "pass": "dev_password123"
    }

# Environment-like setup (still hardcoded)
os.environ['SECRET_KEY'] = "my_very_secret_key_987654321"

print("Test complete.")
