from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ' ': '/'
}

# Encode text to Morse code
def text_to_morse(text):
    return ' '.join(MORSE_CODE_DICT.get(char.upper(), '') for char in text)

# Decode Morse code to text
def morse_to_text(morse):
    reverse_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
    return ''.join(reverse_dict.get(code, '') for code in morse.split())

@app.route('/encode', methods=['POST'])
def encode():
    data = request.json.get("text", "")
    return jsonify({"morse": text_to_morse(data)})

@app.route('/decode', methods=['POST'])
def decode():
    data = request.json.get("morse", "")
    return jsonify({"text": morse_to_text(data)})


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
