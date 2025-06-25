# Task 1: KeshBot - Intelligent Rule-based Chatbot (Enhanced Version)

import time
import random

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

slow_print("🤖 Hello! I am KeshBot - your personal AI buddy!")
slow_print("💬 I'm here to have a fun little chat with you. Let's go!\n")

# Name input
name = input("👤 First, may I know your name? \nYou: ").strip().title()
slow_print(f"👋 Nice to meet you, {name}!\n")

# Mood detection
mood = input("🧠 How are you feeling today? (good/bad/okay)\nYou: ").lower()
if "good" in mood or "great" in mood:
    slow_print("😄 That's awesome! Keep the positivity flowing!")
elif "bad" in mood or "sad" in mood:
    slow_print("😢 I'm sorry to hear that. Remember, after rain comes sunshine!")
else:
    slow_print("🙂 Thanks for sharing. I'm always here to chat!")

# Dream job
dream = input("\n💼 What is your dream job or goal?\nYou: ")
slow_print(f"🚀 {dream} sounds like a wonderful aspiration, {name}. Go for it!\n")

# Hobby or interest
hobby = input("🎨 What's a hobby or something you enjoy doing?\nYou: ")
slow_print(f"✨ Wow, {hobby.capitalize()} is a great way to spend time!")

# Tea or Coffee?
drink = input("\n☕ Quick question – Tea or Coffee?\nYou: ").lower()
if "tea" in drink:
    slow_print("🍵 Tea it is! A calm and classic choice.")
elif "coffee" in drink:
    slow_print("☕ Coffee lovers unite! Fuel for productivity.")
else:
    slow_print("🥤 Nice! Whatever keeps you going.")

# Favorite language
lang = input("\n💻 Which programming language do you like the most?\nYou: ")
slow_print(f"🔥 {lang} is powerful. Keep building amazing things with it!")

# Small NLP-style questions
while True:
    ask = input("\n🤔 You can ask me something like 'your name', 'who made you', 'help', or say 'bye' to exit.\nYou: ").lower()
    
    if "your name" in ask:
        slow_print("🤖 I’m KeshBot, your friendly internship chatbot!")
    elif "who made you" in ask or "developer" in ask:
        slow_print("👨‍💻 I was developed by Keshav Pareek during the CodSoft AI Internship.")
    elif "help" in ask:
        slow_print("💡 I'm here to chat, answer simple questions, and make your day better!")
    elif "bye" in ask or "exit" in ask:
        slow_print(f"👋 Goodbye {name}! It was great talking to you.")
        break
    else:
        fallback = [
            "🤔 Hmm... I'm not sure how to respond to that.",
            "😅 I didn’t quite understand. Can you try saying something else?",
            "🤖 I'm still learning. Ask me something simpler?"
        ]
        slow_print(random.choice(fallback))
