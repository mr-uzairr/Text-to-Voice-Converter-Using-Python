# **Text to Voice Converter using Python**  

This Python script converts text into speech using the **gTTS (Google Text-to-Speech)** library.  

## **Installation**  

1. **Clone this repository:**  
   git clone https://github.com/your-username/Text-to-Voice-Converter.git
   cd Text-to-Voice-Converter


2. **Create and activate a virtual environment (optional but recommended):**  
   python3 -m venv .venv
   source .venv/bin/activate  # For macOS/Linux
   .venv\Scripts\activate     # For Windows


3. **Install dependencies:**  
   pip install -r requirements.txt


## **Usage**  

1. Open the **`texttospeech.py`** file and modify the `text` variable as needed.  
2. Run the script:  
   python texttospeech.py
   
3. The output audio file (`sample.mp3`) will be generated in the same directory.  

## **Requirements**  

- Python 3.6+  
- `gtts` (Google Text-to-Speech)  

## **Install Dependencies**  

If you haven’t installed `gtts`, run:  
pip install gtts

## **Customization**  

- Change the **`text`** variable to convert any desired text to speech.  
- Modify **`language='en'`** to change the output language.  

