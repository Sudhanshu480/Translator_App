# Translator App:

Welcome to the Translator App project. This Streamlit-based application leverages Google's translation service to provide instant translations between different languages. It's designed to be user-friendly and efficient, making it easy to translate text with just a few clicks.

## This is how it looks intially: 
![image](https://github.com/Sudhanshu480/Translator_App/assets/96736479/694f9cb9-1f00-467c-b88b-07069983e213)

## Features:
- **Instant Translation**: Translate text between various languages instantly.
- **Streamlit Interface**: Simple and intuitive UI built with Streamlit.
- **Language Selection**: Easy selection of source and target languages from the sidebar.

# This is how it translates a text from one Language into another
## Translation from English to Spanish:
![image](https://github.com/Sudhanshu480/Translator_App/assets/96736479/4fd1e1a0-7e58-40fc-98d9-131c653f9a10)

## Translation from English to Hindi:
![image](https://github.com/Sudhanshu480/Translator_App/assets/96736479/03be83f5-91cc-4a87-9c66-4121f165460c)



## How it Works
The core functionality of the Translator App revolves around the `translate` function. Here’s a detailed explanation:

1. **User Input**: The function takes three inputs from the user: 
    - `text`, which is the text to be translated.
    - `source`, which is the source language of the text.
    - `target`, which is the target language for translation.
2. **Translation**: The `translate` function utilizes Google's translation service to translate the text from the source language to the target language.
3. **Display**: The translated text is displayed in the Streamlit interface.

## Prerequisites
- Python 3.9 or higher
- Streamlit
- googletrans==4.0.0-rc1

## Usage
### Run the Streamlit App:
```
streamlit run app.py
```

### Interact with the App:
1. **Enter Text**: Type or paste the text you want to translate in the provided text area.
2. **Select Languages**: Choose the source language and target language from the dropdown menus in the sidebar.
3. **Translate**: Click the "Translate" button to get the translated text.

### Example:
1. **Source Language**: English
2. **Target Language**: Spanish
3. **Text**: "Hello, how are you?"
4. **Translation**: "Hola, ¿cómo estás?"

## File Structure
```
translator-app/
│
├── app.py                 # Main application script
├── requirements.txt       # Required Python packages
├── README.md              # Project documentation
└── LICENSE                # Project license
```


## About
This app uses Google's translation service to translate text between different languages. Simply enter your text, select the source and target languages, and click on the translate button to see the translation.

## Contributing
Contributions are welcome! Please feel free to fork this repository and submit pull requests to propose changes or improvements.
