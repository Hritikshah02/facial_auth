# Face Authentication System

This repository contains a simple face authentication system using OpenCV, DeepFace, and SciPy. The system captures an image using the webcam, extracts facial features, and verifies the identity based on stored user data.

## Features
- Captures an image from the webcam for authentication.
- Extracts facial features using DeepFace (ArcFace model).
- Compares stored embeddings with real-time captured images.
- Uses cosine similarity for verification.
- User authentication based on username, password, and face recognition.

## Requirements
Ensure you have the following dependencies installed:
```sh
pip install opencv-python numpy deepface scipy
```

## How It Works
1. **User Authentication**
   - Prompts the user for a username and password.
   - Loads stored user credentials and their corresponding facial embeddings.
2. **Face Verification**
   - Captures an image using the webcam.
   - Extracts facial features from the image.
   - Compares the extracted features with the stored embeddings.
   - Grants or denies access based on cosine similarity.

## Usage
### Generating User Data
To generate `user_data.npy` with user credentials and facial embeddings, run:
```sh
python generate_user_data.py
```

Ensure that the image paths provided in the script are correct and accessible.

### Running Face Authentication
Once user data is generated, run the authentication script:
```sh
python face_auth.py
```

### Steps
1. Enter your username and password.
2. If credentials are valid, capture an image from the webcam.
3. The system will compare the captured image with stored embeddings.
4. If the face matches, access is granted; otherwise, it is denied.

## File Structure
```
|-- face_auth.py          # Main authentication script
|-- generate_user_data.py # Script to generate user_data.npy
|-- user_data.npy         # Stored user data with embeddings
|-- README.md             # Documentation
```

## Notes
- Ensure that `user_data.npy` exists and contains valid user embeddings.
- Modify the `data_path` in the script if you store user data elsewhere.
- Adjust the similarity threshold in `find_user()` if needed.

## License
This project is licensed under the MIT License.

