# Face_Recognition

Steps to be followed to run the project : 

1 - You need to have Jupyter notebook installed, and then create a virtual environment using the command : conda create --name myenv. 
      Here, I have created the environment called FaceRecognition.
    
2 - Once the virtual environment is created, we then activate the environment with the command : conda activate myenv and then travel to the directory where the         project has been stored.

3 - We first need to run the 1-face_dataset.py file using the command python3 1-face_dataset.py. Once the file is being run, type the user name when prompted so         that the face get's captured.

4 - After the first file, we then train using the command : python3 2-face_training.py.

5 - After the first two steps, we then run the face recognition file using the command : python3 3-face_recog.py.

The files included in the project are : 3 files for capturing the face image, training of the image and then for recognition. The 'dataset' folder will contain the images captured while 'trainer' folder will have the train.yml file. The 'user_names.txt' will have the names of the users. 

** This a real time face recognition project using OpenCV **
