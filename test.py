import firebase_admin
from firebase_admin import credentials, firestore

config={
    "type": "service_account",
  "project_id": "academiceval-db982",
  "private_key_id": "9a4fbf30d6c53387153b61fcac03a6000d354b41",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEuwIBADANBgkqhkiG9w0BAQEFAASCBKUwggShAgEAAoIBAQCxIki87XfhQTIZ\n9jjvhI+OOlzFnscM9upNQI4G1qHiTqY/nrRBK4ar9u2MwDRkq64FinPba2d589hs\nnghSe1TCEdptT+H/raOaS3o/6vbQWYNpfcTpXZjHowwABOk+12Is5Dl/CHb6POVW\ne0dMZUU43sq7a5IqSyHC8PuMtyEipu9V/vWVQYBxbU/+kVDvN2OlsUBkdmWT4L9Y\nVrfdimP5QrSL2OEhINFjhiVocX3xTGQvzrIXdOzAi6eDBgHvhBeL9fJANAtTTbLk\n7/vYuZV2U+sRT8sL26ZwIBBrPcI6NyBmIzId1VpnF1zpy58lAboX+pOiLk+HUB5z\nkGwyC69fAgMBAAECgf9I7aFrWsAzynCjDImXrS9tkpnSw1kwlt6tVhnwUG3vvthN\nWT1D/g4N8jXbihOhxXOtOroSNllkD5rYUJ62I6qOossYNmUJEqeveJcPueCxGpAA\nRS4zs1Vm3FPhR73zh+0W9N/qbV6O27bDsTEQD9UJyEoWEzPnaQd9bobvm6lvM89D\nJYMRviSeyzsY8jzuI+7RPpNQJDWRkeJQyUtrvtlieW3TowVw6qOpW6yeitdffqwA\nwnOvrIVnyOAxb1QwC1rRvWSss62sMIpGDTPGxcYjnE7i/rt1nCkAwjkoh+J6RCpx\njEna5OXzM1pDPDtAtuAk5H+VQkdp3ho6NcuFvqECgYEA4lYuBfRJzHW2M10mdaQu\nvZ0XuCPAte5j76zoRZS9NxSeBtTNcLsJjHdat4CXGLldUVLuvArhO3PdMBacdy52\nbn+SGWqpNNQmnXEM2FWPBmXMgKeLKsWz/oXmrDgX+qEkKP13r9O7tU2CXGR3bYRi\n4ovZXGKPxFJE1BQI5RpNAW8CgYEAyFlN101IT4Ta7zt2L6GNmIjl0LxL+i/7eAYZ\naYXpLgjGpi7eocINW86LSBITFUWwyUY1zxOO0SroE2i+QVkp+YgIAZqIhevMsyx/\n24zxW8mk7sqrzkouaLvJmdX915ufP4WKJ+3YqlYQI1eyNFQAK3F9aJz9mpNpu8/0\nSRQBWRECgYAWL4xjWQbC2+b4MfFLJsTOIU/p5NdG/g8dtz0tVN8XPxYeZU2d9zeA\nZVKnGhu1eLYE+rQcCpT5VuofhJfhttQ1EJwpkaL0YrdGR4aSzhAu+FuLYODrWGXE\nVSu/ReBT2OfKfM32ljKYGvjkRZTPT2LCAiNUQvUEsWu9vhkBHArgUQKBgAYuay5n\nXgHGEZMr/Ht/uoSoRJ7qEFYJwPJ1DbepwAYBk09xRsEq4Yqhlr6EgD45xjiPh/15\nlwBxGHPw2V3eyGLAha62+9tV6RzmFJPLh27Ti9kqO57DvybQFGpApfJPBNzK2/Zb\nakHnIdxVSlQ++zpb6AigP1rTjYGT6u+ORHRhAoGBAJbLh9++98xk5TG9hDnzUtfw\nQVLFKbkOGDkl23dRUY5kqnitexCtpjLqGn/pfIeAs5tH6WHoeKvfcsyWRbUuQKDy\nzzEaebG6JcmkVE6r+NpYLdO+2u2ZyuZZCDpQYTBn14DbI9FnzosnhgcPO9vJmuJm\nQWwDbDaw99l+TxUvf3yW\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-l0ja0@academiceval-db982.iam.gserviceaccount.com",
  "client_id": "118098537295695315448",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-l0ja0%40academiceval-db982.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"

}
cred = credentials.Certificate(config)
firebase_admin.initialize_app(cred)


db = firestore.client()

def get_total_documents_in_collection(collection_name):
    try:
        # Retrieve all documents in the collection
        collection_ref = db.collection(collection_name)
        docs = collection_ref.stream()
        
        # Count the number of documents
        total_documents = len(list(docs))
        
        return total_documents
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return 0

# Example usage
collection_name = 'Students'  # Replace with the actual collection name, e.g., 'users'
total_documents = get_total_documents_in_collection(collection_name)
print(f"Total number of documents in the collection '{collection_name}': {total_documents}")
