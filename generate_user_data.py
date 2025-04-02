
import numpy as np

from deepface import DeepFace



def generate_embeddings(img_path):
    """
    Generate and return an embedding for a given image.
    """
    try:
        embedding_obj = DeepFace.represent(img_path=img_path, model_name='ArcFace', enforce_detection=False)
        return np.array(embedding_obj[0]["embedding"])
    except Exception as e:
        print(f"Error generating embedding: {e}")    
        return None

user_data = [
    {"username": "hritik", "password": "1234", "embedding": generate_embeddings(r"C:\\Users\\vrund\\OneDrive\\Pictures\\Camera Roll\\hritik3.jpg")},
    {"username": "dharam", "password": "5678", "embedding": generate_embeddings(r"C:\\Users\\vrund\\OneDrive\\Pictures\\Camera Roll\\dharam.jpg")},
    {"username": "yug", "password": "9999", "embedding": generate_embeddings(r"C:\\Users\\vrund\\OneDrive\\Pictures\\Camera Roll\\yug1.jpg")}
]

# Save user data
np.save("user_data.npy", user_data, allow_pickle=True)
print("User data saved as .npy")