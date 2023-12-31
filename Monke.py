import random
import time
from pynput import keyboard
import pygame
from colorama import Fore, Style, init

init(autoreset=True)

pygame.init()
pygame.mixer.init()

keypress_sound = pygame.mixer.Sound("keyboard.wav")
backspace_sound = pygame.mixer.Sound("backspace.wav")

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


def on_keypress(key):
    global user_input
    
    try:
        char = key.char
        keypress_sound.play() 

        if char is not None:
            user_input += char
            print(char, end='', flush=True)
    except AttributeError:
        if key == keyboard.Key.space:
            user_input += ' ' 
            print(' ', end='', flush=True) 
        elif key == keyboard.Key.backspace:
            backspace_sound.play() 
            user_input = user_input[:-1]
            print("\b \b", end='', flush=True)

def typing_test(text, time_limit):
    global user_input
    user_input = ""
    listener = keyboard.Listener(on_press=on_keypress)
    listener.start()
    
    print("Type the following text:")
    print(Fore.YELLOW + text + Style.RESET_ALL)
    input("Press Enter to start...")
    
    start_time = time.time()
    
    while len(user_input) < len(text):
        pass
    
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    words_per_minute = (len(user_input.split()) / elapsed_time) * 60
    accuracy = calculate_accuracy(text, user_input)
    
    print("\n" +Fore.GREEN + f"Time taken: {elapsed_time:.2f} seconds" + Style.RESET_ALL)
    print(Fore.CYAN + f"Words per minute: {words_per_minute:.2f} WPM" + Style.RESET_ALL)
    print(Fore.GREEN + f"Accuracy: {accuracy:.2%}" + Style.RESET_ALL)
    
    listener.stop()

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
    while True:
        sample_text = random.choice(sample_texts)
        time_limit = len(sample_text) / 15 
        
        typing_test(sample_text, time_limit)
        
        retry = input("Do you want to try another typing test? (yes/no): ").lower()
        if retry != "yes":
            break

pygame.mixer.quit()
