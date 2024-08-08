from flask import Flask, render_template, request, jsonify
import random
import time

app = Flask(__name__)

sample_texts = [
    "The quick brown fox jumps over the lazy dog",
    "Python is a high-level programming language",
    "Practice makes perfect",
    "Typing speed matters in today's digital world",
    "Keep calm and type on",
    "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful",
    "The only way to do great work is to love what you do",
    "You miss 100% of the shots you don't take",
    "The future belongs to those who believe in the beauty of their dreams",
    "Happiness is not something ready-made. It comes from your own actions",
    "In three words, I can sum up everything I've learned about life: it goes on",
    "Life is really simple, but we insist on making it complicated",
    "The only thing standing between you and your goal is the story you keep telling yourself as to why you can't achieve it",
    "You are never too old to set another goal or to dream a new dream",
    "The greatest glory in living lies not in never falling, but in rising every time we fall",
    "The best time to plant a tree was 20 years ago. The second best time is now",
    "Don't count the days; make the days count",
    "Life is 10% what happens to us and 90% how we react to it",
    "I find that the harder I work, the more luck I seem to have",
    "The only limit to our realization of tomorrow will be our doubts of today",
    "Believe you can and you're halfway there"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_text', methods=['GET'])
def get_text():
    text = random.choice(sample_texts)
    return jsonify({"text": text})

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    typed_text = data['typed_text']
    original_text = data['original_text']
    start_time = data['start_time']
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    words_per_minute = (len(typed_text.split()) / elapsed_time) * 60
    accuracy = calculate_accuracy(original_text, typed_text)
    
    return jsonify({
        "elapsed_time": elapsed_time,
        "words_per_minute": words_per_minute,
        "accuracy": accuracy
    })

def calculate_accuracy(actual, typed):
    actual_words = actual.split()
    typed_words = typed.split()
    correct_words = 0
    
    for i in range(min(len(actual_words), len(typed_words))):
        if actual_words[i] == typed_words[i]:
            correct_words += 1
    
    accuracy = correct_words / len(actual_words)
    return accuracy

if __name__ == "__main__":
    app.run(debug=True)
