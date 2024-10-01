from flask import Flask, render_template, request, redirect, url_for, session
import firebase_admin
from firebase_admin import credentials, firestore
import matplotlib.pyplot as plt
import pandas as pd

# Initialize Firebase Admin with service account
cred = credentials.Certificate(r'./privatekey.json')  # Replace with the path to your service account JSON file
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

def plot_exam_attendance(collection_name):
    """
    Plots the number of students present in each exam based on the exam date.
    
    :param collection_name: The name of the collection where exam data is stored
    """
    try:
        # Fetch all documents from the collection
        collection_ref = db.collection(collection_name)
        docs = collection_ref.stream()

        # Lists to store dates and student counts
        dates = []
        student_counts = []

        for doc in docs:
            data = doc.to_dict()
            exam_date = data.get('date')  # Ensure your Firestore documents have a 'date' field
            student_count = data.get('students_present', 0)  # Assume a 'students_present' field holds the count
            
            if exam_date and student_count is not None:
                dates.append(exam_date)
                student_counts.append(student_count)

        # Convert dates to a format suitable for plotting
        dates = [pd.to_datetime(date) for date in dates]  # Optional: Use if dates need to be converted to datetime objects
        
        # Plot the data
        plt.figure(figsize=(10, 6))
        plt.plot(dates, student_counts, marker='o', linestyle='-', color='b')
        plt.title('Number of Students Present in Each Exam')
        plt.xlabel('Exam Date')
        plt.ylabel('Number of Students Present')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()

        plt.show()

    except Exception as e:
        print(f"An error occurred: {str(e)}")

collection_name = 'Students'  
plot_exam_attendance(collection_name)
