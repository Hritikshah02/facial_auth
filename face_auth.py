import cv2
import numpy as np
import os
from deepface import DeepFace
from scipy.spatial.distance import cosine

def capture_image_from_camera(save_path="captured_image.jpg"):
    """
    Captures an image from the webcam and saves it to the specified path.
    """
    cap = cv2.VideoCapture(0)  # Open the default camera (0)
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return None

    print("Press 'Space' to capture the image. Press 'Esc' to exit.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image")
            break

        cv2.imshow("Capture Image - Press 'Space' to Save", frame)
        
        key = cv2.waitKey(1) & 0xFF
        if key == 32:  # Space key to capture image
            cv2.imwrite(save_path, frame)
            print(f"✅ Image saved as {save_path}")
            break
        elif key == 27:  # ESC key to exit
            print("❌ Capture canceled.")
            cap.release()
            cv2.destroyAllWindows()
            return None

    cap.release()
    cv2.destroyAllWindows()
    return save_path

def extract_features_from_image(image_path):
    """
    Extract features (embedding) from a given image path.
    """
    try:
        embedding_obj = DeepFace.represent(img_path=image_path, model_name="ArcFace", enforce_detection=False, align=True)
        embedding = np.array(embedding_obj[0]['embedding'])
        return embedding
    except Exception as e:
        print(f"Error generating embedding: {e}")
        return None

def verify_user_credentials(username, password, data_path="user_data.npy"):
    """
    Check if username and password exist in stored data.
    Returns the user's saved embedding if credentials are valid.
    """
    try:
        user_data = np.load(data_path, allow_pickle=True)   
    except FileNotFoundError:
        print("User data file not found.")
        return None

    for user in user_data:
        if user["username"] == username and user["password"] == password:
            print("✅ Username & Password Matched!")
            return user["embedding"]
    
    print("❌ Invalid Username or Password.")
    return None

def find_user(saved_embedding, current_embedding, threshold=0.45):
    """
    Verify user by comparing stored embedding with real-time captured face.
    """
    similarity = 1 - cosine(saved_embedding, current_embedding)
    print(f"✅ Cosine Similarity: {similarity:.4f}")
    
    if similarity > (1 - threshold):
        print("🎉 Face verified successfully!")
        return True
    else:
        print("⚠️ Face does not match!")
        return False

# --- User Authentication Process ---
username = input("Enter username: ")
password = input("Enter password: ")

saved_embedding = verify_user_credentials(username, password)

if saved_embedding is not None:
    print("Proceeding with face verification...")

    # --- Capture Image in Real-Time ---
    captured_image_path = capture_image_from_camera()

    if captured_image_path:
        current_embedding = extract_features_from_image(captured_image_path)

        if current_embedding is not None:
            if find_user(saved_embedding, current_embedding):
                print("✅ Access Granted!")
            else:
                print("❌ Access Denied!")
