from flask import Flask, render_template_string, request
from crypton import generate_key, encrypt_password, decrypt_password

app = Flask(__name__)

HTML = """
<!doctype html>
<title>Crypton Password Encryptor</title>
<h2 style="align: center">Crypton Password Encryptor</h2>
<form method="post">
    <label>Key:</label><br>
    <input name="key" value="{{ key }}" size="60"><br><br>
    <label>Password to Encrypt:</label><br>
    <input name="password" type="password" size="40"><br>
    <button name="action" value="encrypt">Encrypt</button><br><br>
    <label>Encrypted Password:</label><br>
    <input name="encrypted" value="{{ encrypted }}" size="60"><br>
    <button name="action" value="decrypt">Decrypt</button><br><br>
</form>
{% if decrypted %}
<p><b>Decrypted Password:</b> {{ decrypted }}</p>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def index():
    key = ""
    encrypted = ""
    decrypted = ""
    if request.method == "POST":
        key = request.form.get("key") or generate_key().decode()
        action = request.form.get("action")
        if action == "encrypt":
            password = request.form.get("password", "")
            try:
                encrypted = encrypt_password(password, key.encode())
            except Exception as e:
                encrypted = f"Error: {e}"
        elif action == "decrypt":
            encrypted = request.form.get("encrypted", "")
            try:
                decrypted = decrypt_password(encrypted, key.encode())
            except Exception as e:
                decrypted = f"Error: {e}"
    else:
        key = generate_key().decode()
    return render_template_string(HTML, key=key, encrypted=encrypted, decrypted=decrypted)

if __name__ == "__main__":
    app.run(debug=True)