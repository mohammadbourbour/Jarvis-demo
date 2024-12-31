# Jarvis-Demo

Jarvis-Demo is a simple text and voice-based personal assistant program designed to perform various tasks such as telling jokes, playing music, giving motivational quotes, and more. It uses Python and several libraries for text-to-speech, speech recognition, and other functionalities.

## Note

This project is a demo and does not use machine learning for intent detection. Intent detection is based on simple keyword matching. Future versions will incorporate AI models for more advanced intent recognition and expand functionality with additional abilities.

### Designed with OOP:

This project follows an object-oriented programming (OOP) structure, making it easy to extend functionality. Developers can add new abilities by simply creating functions in the \`functions.py\` file and integrating them into the intent handling system in \`main.py\`.

## Features

- **Greet the User:** Friendly greeting messages.
- **Time Inquiry:** Provides the current time.
- **Tell Jokes:** Fetches random jokes to lighten the mood.
- **Motivational Quotes:** Offers uplifting quotes for inspiration.
- **Pomodoro Timer:** Helps with focus using a 25-minute timer.
- **Play Music:** Plays a random music file from a designated folder.
- **Generate Passwords:** Creates strong, random passwords.
- **Fetch News:** Reads the latest headlines using a news API.
- **Storytelling:** Narrates random short stories.
- **Exercise Suggestions:** Recommends simple fitness activities.
- **Share Random Facts:** Tells fascinating facts.
- **Daily Goals:** Helps users set and store daily objectives.

## Prerequisites

Ensure you have Python 3.8+ installed. You'll also need `pip` to install dependencies.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mohammadbourbour/jarvis-demo.git
   cd jarvis-demo
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## How to Run

1. Start the application:
   ```bash
   python main.py
   ```
2. Follow the on-screen instructions to interact with Jarvis via text or voice.

## Directory Structure

```
jarvis-demo/
├── music/               # Put your musics here
├── main.py              # Entry point of the application
├── functions.py         # Contains core abilities and functionality
├── requirements.txt     # List of Python dependencies
├── user_info.json       # Stores user details (auto-created)
└── README.md            # Project documentation
```

## Dependencies

The project relies on the following Python libraries:

- `pyfiglet`: For ASCII art banners.
- `pyttsx3`: For text-to-speech capabilities.
- `SpeechRecognition`: To convert speech to text.
- `termcolor`: For colored terminal output.
- `pyjokes`: For generating jokes.
- `requests`: For interacting with external APIs.

Install these using the `requirements.txt` file.

## Contributing

Feel free to fork this project and submit pull requests. Contributions are always welcome.

## License

This project is open-source and licensed under the MIT License.

## Acknowledgements

Special thanks to the developers of the libraries used in this project.
