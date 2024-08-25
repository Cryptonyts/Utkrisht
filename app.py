from flask import *
import os
import assemblyai as aai
from gemini import *
import requests


app = Flask(__name__)

app_data = {'project_name': 'Merch'}
app.secret_key = 'your_secret_key_here'


@app.route("/")
def index():
    app_data = {'project_name': 'Merch'}
    return render_template("index.html", app_data=app_data)

@app.route('/draft1')
def draft1():
    return render_template('draft1.html', app_data=app_data)
@app.route('/standing')
def standing():
    return render_template('standing.html', app_data=app_data)
@app.route('/slant')
def slant():
    return render_template('slant.html', app_data=app_data)
@app.route('/alphabet')
def alphabet():
    return render_template('alphabet.html', app_data=app_data)



@app.route('/success', methods = ['POST'])  
def success():  
    # Check if a file was uploaded
    if 'file' not in request.files:
        return "No file uploaded"

    file = request.files['file']
    
    # Check if the file is empty
    if file.filename == '':
        return "Empty filename"
    
    # Save the uploaded file
    global file_path

    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)

    if file.filename.endswith('.mp3'):
        transcribe_audio(file_path)
        file_path = os.path.join('uploads', file.filename + "transcribed")

    session['file_path'] = file_path
    
    # Call your Python script to process the uploaded file
    output = run_python_script(file_path)
    
    # Redirect to another HTML page with the output
    return redirect(url_for('show_output', output=output))

def get_session():
    return session.get('file_path')

def run_python_script(file_path):
    # Your code to run the Python script and process the uploaded file
    # This function should return the output of the Python script
    # For demonstration purposes, let's just read the content of the file
    
    with open(file_path, 'r') as f:
        return f.read()

def transcribe_audio(file_path):

    # Replace with your API key
    aai.settings.api_key = "ce7e699b08654c93bd8db3f5fe302921"

    # URL of the file to transcribe
    FILE_URL = file_path

    # You can also transcribe a local file by passing in a file path
    # FILE_URL = './path/to/file.mp3'

    config = aai.TranscriptionConfig(auto_highlights=True)

    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(
    FILE_URL,
    config=config
    )

    transcription_text = transcript.text
    transcribed_file_path = os.path.join(file_path + "transcribed")
    with open(transcribed_file_path, 'w') as file:
        file.write(transcription_text)

    return transcript.text
    
@app.route('/show_output')
def show_output():
    # Retrieve the output from the query parameter
    
    output = request.args.get('output', '')
    return render_template('output.html', output=output, app_data=app_data)


@app.route('/transcript')
def transcript():
    app_data = {'project_name': 'Perch'}
    # Get the original transcript text from the query parameter
    #original_transcript = request.args.get('output', '')

    # Call clean_up_text function with the original transcript
    file_path = get_session()
    with open(file_path, 'r') as f:
        text = f.read()
    cleaned_transcript = clean_up_text(text)

    outt = text_to_flowchart(text)
    print("flowcharttttttttsjafagsjasgf : ",outt)
    

    # Pass the cleaned transcript to the template
    return render_template('/output_pages/transcript.html', output=cleaned_transcript, app_data=app_data)


@app.route('/summary')
def summary():
    file_path = get_session()
    with open(file_path, 'r') as f:
        text = f.read()
    summarized_transcript = text_to_notes(text)
    

    # Pass the cleaned transcript to the template
    return render_template('/output_pages/summary.html', output=summarized_transcript, app_data=app_data)


@app.route('/translate')
def translate2():
    preferred_language = request.args.get('parameter')
    file_path = get_session()
    with open(file_path, 'r') as f:
        text = f.read()
    translated_transcript = translate(text,preferred_language)

    return render_template('/output_pages/translate.html', output=translated_transcript, app_data=app_data)


@app.route('/accent')
def accent():
    preferred_accent = request.args.get('parameter')

    CHUNK_SIZE = 1024
    if preferred_accent == "female-american":
        url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"
    elif preferred_accent == "male-american":
        url = "https://api.elevenlabs.io/v1/text-to-speech/29vD33N1CtxCmqQRPOHJ"
    elif preferred_accent == "female-british":
        url = "https://api.elevenlabs.io/v1/text-to-speech/ThT5KcBeYPX3keUQqHPh"
    elif preferred_accent == "male-british":
        url = "https://api.elevenlabs.io/v1/text-to-speech/Yko7PKHZNXotIFUBG7I9"

    file_path = get_session()
    with open(file_path, 'r') as f:
            text_to_read = f.read()

    headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": "d0ce24f3593edee40147c9cf4180e226"
    }

    data = {
    "text": text_to_read,
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.5
    }
    }

    response = requests.post(url, json=data, headers=headers)
    output_file_path = os.path.join('static', 'output.mp3')

    with open(output_file_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)

    return render_template('/output_pages/accent.html', mp3_file_path = "output.mp3", app_data=app_data)

@app.route('/flashcards')
def flashcards():
    
    file_path = get_session()
    with open(file_path, 'r') as f:
        text = f.read()
    full,keyword,description = find_keywords(text)
    print("smth", keyword, description,"smth else")
    return render_template('/output_pages/flashcards.html', keyword = keyword, description = description, app_data=app_data)


def chat_with_gemini(message):
    multimodal_model = genai.GenerativeModel("gemini-1.0-pro")
    response = multimodal_model.generate_content([message, "Respond professionally in plain text."])
    return response.text

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message')
    response = chat_with_gemini(message)
    return jsonify({'response': response})


if __name__ == '__main__':
    app.run(debug=False, host = '0.0.0.0')
