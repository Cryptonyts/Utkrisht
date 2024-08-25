# **Utkrisht: Empowering the Education of Mentally Challenged Individuals**

## **Table of Contents**
- [Project Overview](#project-overview)
- [Justification](#justification)
- [Architecture](#architecture)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Comparison with Existing Solutions](#comparison-with-existing-solutions)

## **Project Overview**
Utkrisht is a comprehensive educational platform designed to support the learning needs of mentally challenged individuals. By leveraging cutting-edge technologies such as AI, machine learning, and interactive games, Utkrisht offers a personalized and accessible educational experience. Our platform includes tools for language learning, hand sign recognition, and interactive games aimed at improving cognitive skills.

## **Justification**
We chose to develop Utkrisht because we have three classmates who are neuro-diverse, and we have witnessed firsthand the challenges they face in accessing appropriate educational resources. The existing educational tools for mentally challenged individuals are often fragmented, difficult to use, or lack the personalized touch that is essential for effective learning. Utkrisht aims to bridge this gap by offering a centralized, user-friendly platform that combines multiple learning tools into a cohesive and accessible solution. Our goal is to make education more inclusive and tailored to the needs of every learner.


## **Comparison with Existing Solutions**
While there are various tools available for supporting the education of mentally challenged individuals, they are often scattered across different platforms and lack integration. Utkrisht offers a unique advantage by providing a one-stop solution that combines all necessary educational tools in a single, cohesive platform. This centralized approach not only enhances user experience but also ensures that learning is streamlined and accessible. Moreover, the integration of AI, multilingual support, and interactive games makes Utkrisht more versatile and effective than existing solutions.
- Special thanks to the open-source community and everyone who contributed to the development of the tools and libraries used in this project.
- This project was inspired by the need to create accessible educational resources for individuals with special needs.


## **Architecture**
![WhatsApp Image 2024-08-25 at 13 46 29_685206c2](https://github.com/user-attachments/assets/c381d69b-6135-4418-a8c0-e98b2279b6d3)
![WhatsApp Image 2024-08-25 at 13 46 29_7b245175](https://github.com/user-attachments/assets/95e0f126-1467-44b9-bc35-dd8a699d2a41)

## **Features**
### 1. **ASL Hand Sign Detection Game**
- **Description**: An engaging game that helps users learn and practice American Sign Language (ASL) by detecting hand signs through their webcam.
- **Technology**: The game uses a custom-trained model in TensorFlow for real-time ASL hand sign recognition.

### 2. **AI-Assisted MP3 Audio Summarizer**
- **Description**: A tool that converts lengthy audio files into concise summaries. It supports multiple languages, making it accessible to a diverse user base.
- **Technology**: Utilizes AI and natural language processing to generate summaries and supports text-to-speech in various languages.

### 3. **Flashcard Assistance**
- **Description**: Flashcards designed to reinforce learning through repetition. The flashcards are customizable and can include text, images, or sounds to cater to different learning styles.

### 4. **Interactive Educational Games**
- **Alphabet Tracing Game**: Users can trace letters on a canvas using a mouse or touchscreen, helping them learn to write the alphabet.
- **Memory Game**: A game that challenges users to match pairs of cards, enhancing memory skills. It tracks the longest streak to encourage improvement.
- **Shape Tracing Game**: Users can trace various shapes, helping them recognize and remember different geometric figures.

## **Technologies Used**
- **Backend**: Flask
- **Frontend**: JavaScript, HTML5, CSS3
- **Machine Learning**: TensorFlow
- **Audio Processing**: Python, NLTK (Natural Language Toolkit)
- **Multilingual Support**: Google Translate API, Text-to-Speech API

## **Installation**
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/utkrisht.git
   cd utkrisht
   ```

2. **Set up a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask server**:
   ```bash
   flask run
   ```

5. **Access the application**:
   - Open your web browser and go to `http://localhost:5000`.

## **Usage**
1. **ASL Hand Sign Detection**: Navigate to the ASL game section and follow the instructions to start the hand sign detection game.
2. **Audio Summarizer**: Upload an MP3 file, select the desired language, and receive a summarized text along with an option to convert it into an audio format.
3. **Flashcards**: Choose a flashcard set or create your own to start practicing.
4. **Games**: Engage with the alphabet tracing, memory, and shape tracing games by navigating to their respective sections on the platform.
