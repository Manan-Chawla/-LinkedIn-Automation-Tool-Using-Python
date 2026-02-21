# -LinkedIn-Automation-Tool-Using-Python
Automatically upload and publish a **PDF document** (cheat sheet, ebook, report, etc.) to LinkedIn using the official LinkedIn REST API.

---

## ✨ Features

- ✅ Upload PDF as a LinkedIn Document Post
- ✅ Uses modern LinkedIn REST API (`/rest/assets`, `/rest/posts`)
- ✅ Compatible with Python 3.14
- ✅ Uses OpenID Connect (`/v2/userinfo`)
- ✅ Clean and structured code
- ✅ Debug logs for troubleshooting

---

# 📌 What This Project Does

This automation:

1. Fetches your LinkedIn User ID
2. Registers document upload
3. Uploads the PDF file
4. Publishes a public LinkedIn post with the document attached

---

# 🛠 Tech Stack

- Python 3.14
- requests
- LinkedIn REST API
- OAuth 2.0 (3-Legged Flow)

---

# 📦 Installation

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
pip install requests
```


# LinkedIn Developer Setup (Step-by-Step)
  **Create LinkedIn Developer App**
  1. Go to: https://www.linkedin.com/developers/
  2. Click Create App
  3. Fill:
     App Name
     LinkedIn Page (can use personal page)
     App Logo
  4. Click Create App

  **Add Required Products**
  Inside your App Dashboard → Products
  Enable:
  * Sign In with LinkedIn using OpenID Connect
  * Share on LinkedIn
  Wait 2–5 minutes after enabling.

  **Configure OAuth Settings**
  Go to Auth Tab --> Add Redirect URL : http://localhost:8000/callback

  **Generate Access Token**
  Inside Auth → OAuth 2.0 Tools
  Generate a token with these scopes ---> openid, profile, w_member_social

  **Why these scops are important?**
  | Scope           | Purpose                       |
  | --------------- | ----------------------------- |
  | openid          | Fetch user ID via `/userinfo` |
  | profile         | Access profile data           |
  | w_member_social | Publish posts                 |


# Configure the script 
Create a file app.py and open terminal and install --> pip install requests

# Now run the code which i've uploaded in file app.py.
