 # Olootu: Yoruba Translator App
    #### Video Demo:  <URL HERE>
    #### Description:
     Olootu is a Python-based console application designed to provide a suite of educational and fun tools for Yoruba language enthusiasts. The application offers translation services, a word game, and a collection of Yoruba proverbs with their meanings and translations. The goal of Olootu is to make learning Yoruba accessible and enjoyable, leveraging technology to bridge the gap between English and Yoruba speakers.

    ###Features:
     -Translation to Yoruba: 
     Translate English text to Yoruba using Google Translate. This feature supports single words, phrases, and full sentences, making it a versatile tool for learners at any level.

     -Word Game: Test your knowledge of Yoruba words with an interactive word game. This game helps reinforce vocabulary by challenging users to translate Yoruba words into English. The game consists of 10 rounds, with immediate feedback provided for each guess.

     -Yoruba Proverbs and Meanings: 
     Explore a collection of Yoruba proverbs along with their translations and meanings.Proverbs are an integral part of Yoruba culture, and this feature provides insights into the wisdom and philosophy embedded in the language.

    ###Installation:
     To run this project, you will need Python installed on your system along with the required packages. Follow the steps below to set up the environment:

    -Clone this repository:
     git clone https://github.com/yourusername/olootu.git 
     cd olootu
    -Create and activate a virtual environment (optional but recommended):
     python -m venv venv
     source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

    -Install the required dependencies:
      pip install -r requirements.txt

    ###Dependencies
    - googletrans: A Python library that implements Google Translate API for translating text.
    - pyfiglet: A Python module for converting text into ASCII art, used to enhance the visual appeal of the console application.
    - sys: A built-in Python module that provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.
    - random: A built-in Python module that implements pseudo-random number generators for various distributions.
    
    ###Usage
     To start the application, run the following command in your terminal: python project.py

    ###Main Menu
    - Translation to Yoruba: Enter an English word, phrase or sentence to get the Yoruba translation. Type "exit" to return to the main menu.

    - Oro Ere (Word Game):
     Play a game to test your Yoruba vocabulary.You will be prompted to translate Yoruba words to English. The game displays words in Yoruba and asks for the equivalent meaning in English. You have 10 words to guess, and your score will be graded over 10. If you guess a word incorrectly, you will be given a second chance. If you get it wrong again, the correct answer will be displayed, and a point will be deducted. The game continues until all 10 words are attempted, and your final score is shown. Afterward, you will be prompted to choose "Yes" to play again or "No" to return to the main menu.

    - OWe ati Itumo (Proverbs and Meaning): 
     Get a random Yoruba proverb with its translation and meaning. Type "exit" to return to the main menu.
    
    - Exit:  
      Type 4 to Exit the application.
    
    ###Troubleshooting
    - Translation errors: If the translation feature isn't working, ensure you have an active internet connection as the Google Translate API requires online access.
    - Installation issues: If you encounter issues during installation, verify that you have the correct version of Python and that all dependencies are installed correctly.

    Contributing
    Contributions are welcome! Please follow these steps to contribute:

    1. Fork the repository.
    2. Create a new branch (git checkout -b feature-branch).
    3. Make your changes.
    4. Commit your changes (git commit -m 'Add some feature').
    5. Push to the branch (git push origin feature-branch).
    6. Open a pull request.

    ###Author
    Habeeb Junaid - https://github.com/TopNaid



