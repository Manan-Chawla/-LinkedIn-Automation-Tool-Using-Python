import requests
import time


class LinkedinPDFUploader:
    def __init__(self, access_token, pdf_path, title, description):
        self.access_token = access_token
        self.pdf_path = pdf_path
        self.title = title
        self.description = description

        self.api_version = "202602"

        self.base_headers = {
            "Authorization": f"Bearer {self.access_token}",
            "LinkedIn-Version": self.api_version,
            "X-Restli-Protocol-Version": "2.0.0",
            "Content-Type": "application/json"
        }




    def get_user_id(self):
        url = "https://api.linkedin.com/v2/userinfo"

        response = requests.get(
            url,
            headers={"Authorization": f"Bearer {self.access_token}"}
        )

        if response.status_code != 200:
            raise Exception(
                f"Failed to fetch user ID: {response.status_code} - {response.text}"
            )

        return response.json()["sub"]




    def register_upload(self):
        url = "https://api.linkedin.com/rest/documents?action=initializeUpload"

        data = {
            "initializeUploadRequest": {
                "owner": f"urn:li:person:{self.user_id}"
            }
        }

        response = requests.post(
            url,
            headers=self.base_headers,
            json=data
        )

        if response.status_code != 200:
            raise Exception(
                f"Failed to register upload: {response.status_code} - {response.text}"
            )

        response_json = response.json()

        upload_url = response_json["value"]["uploadUrl"]
        document = response_json["value"]["document"]

        return upload_url, document



    def upload_pdf(self, upload_url):
        with open(self.pdf_path, "rb") as f:
            pdf_data = f.read()

        response = requests.put(
            upload_url,
            headers={"Content-Type": "application/pdf"},
            data=pdf_data
        )

        if response.status_code not in [200, 201, 204]:
            raise Exception(
                f"Upload failed: {response.status_code} - {response.text}"
            )

   


    def create_post(self, document):
        url = "https://api.linkedin.com/rest/posts"

        clean_desc = self.description.strip()

        # Normalize line breaks
        clean_desc = clean_desc.replace("\r\n", "\n").replace("\r", "\n")

        if len(clean_desc) > 3000:
            clean_desc = clean_desc[:2990] + "..."

        data = {
            "author": f"urn:li:person:{self.user_id}",
            "commentary": clean_desc,
            "visibility": "PUBLIC",
            "distribution": {
                "feedDistribution": "MAIN_FEED",
                "targetEntities": [],
                "thirdPartyDistributionChannels": []
            },
            "content": {
                "media": {
                    "title": self.title[:100],
                    "id": document
                }
            },
            "lifecycleState": "PUBLISHED",
            "isReshareDisabledByAuthor": False
        }

        response = requests.post(
            url,
            headers=self.base_headers,
            json=data
        )

        if response.status_code not in [200, 201]:
            raise Exception(
                f"Post creation failed: {response.status_code} - {response.text}"
            )

        post_id = response.headers.get("x-restli-id")

        print("\nSUCCESS! PDF posted.")
        print(f"https://www.linkedin.com/feed/update/{post_id}/")

    



    def main(self):
        print("Starting LinkedIn PDF upload process...")

        self.user_id = self.get_user_id()
        print(f"User ID: {self.user_id}")

        upload_url, document = self.register_upload()
        print(f"Document registered: {document}")

        self.upload_pdf(upload_url)
        print("PDF uploaded.")

        print("Waiting 10 seconds for processing...")
        time.sleep(1)

        self.create_post(document)


if __name__ == "__main__":
    access_token="paste_your_access_token"

    pdf_path = "GCP-CheatSheet.pdf"

    title = "Google Cloud Platform (GCP) Cheat Sheet – Developer & Interview Ready Notes"

    description = """I've created a Google Cloud Platform (GCP) Cheat Sheet to simplify core cloud concepts for developers and learners.

This PDF covers:
• Core GCP services (Compute, Storage, Networking)
• IAM & Security fundamentals
• Cloud Run, App Engine, GKE basics
• Architecture-level understanding
• Quick revision points for interviews

Whether you're:
• Preparing for cloud interviews
• Starting your cloud journey
• Revising GCP fundamentals

Detailed notes:
https://github.com/Manan-Chawla/Google-Cloud-Platform-Tutorial/blob/master/GCP-Notes.md

#GoogleCloud #GCP #CloudComputing #DevOps #CloudEngineering #TechLearning #OpenSource
"""

    uploader = LinkedinPDFUploader(access_token, pdf_path, title, description)
    uploader.main()
