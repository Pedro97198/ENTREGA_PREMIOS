Classification of Sign Language Images

Team Members: Ignacio Donderis, Miguel Santiago, Pedro Torrijos

First Part (Web Scraping)
    Here is where we encountered the first problem. The images we had were of entire words, not individual letters. This was not ideal for creating the model.

Second Part (Web Scraping)
    We downloaded images of the sign language alphabet from a government website using web scraping. We created Python code to download the images, another code to label the words according to the website's tags, and filtered to keep only the photos showing the person with the sign.

Third Part (First Model on Roboflow)
    We attempted to create the model with the images we had, which totaled 32 images. Due to the small number of images, the model was not functional, resulting in unacceptably low accuracy.

Fourth Part (Kaggle)
    We tried to download images from Kaggle with the intention of creating an HTML, dumping the images into the HTML, and performing web scraping. However, this approach also failed due to problems creating the webpage (uploading images to the webpage). Therefore, we used the images directly.

Fifth Part (EDA)
    Upon downloading the images, they were organized into folders by letter, but the PNG filenames were numbers, which were not suitable for labeling in Roboflow. Therefore, we created a code that utilizes the name of the folder to properly name the photos. Due to time limitations with Roboflow processing images, we opted to reduce the number of images by 10 for each letter.

Sixth Part (Second Model on Roboflow)
    We uploaded the images, labeled them within Roboflow (assigning 1/3 for each person), and created the model, which gave us an accuracy of 77.9%. We tested the model using the tool provided by Roboflow to use the mobile phone camera.

Seventh Part (Hugging Face)
    We searched for a pre-trained model on the Hugging Face website, which classifies images into groups according to the sign.