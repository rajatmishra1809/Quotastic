from flask import Flask, render_template
import random

app = Flask(__name__)

quotes = [
  {"quote": "Don't watch the clock; do what it does. Keep going.", "author": "Sam Levenson"},
  {"quote": "The best way to predict the future is to create it.", "author": "Peter Drucker"},
  {"quote": "You miss 100% of the shots you don’t take.", "author": "Wayne Gretzky"},
  {"quote": "Whether you think you can or you think you can’t, you’re right.", "author": "Henry Ford"},
  {"quote": "I have not failed. I've just found 10,000 ways that won't work.", "author": "Thomas Edison"},
  {"quote": "Success is not final, failure is not fatal: It is the courage to continue that counts.", "author": "Winston Churchill"},
  {"quote": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt"},
  {"quote": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
  {"quote": "What lies behind us and what lies before us are tiny matters compared to what lies within us.", "author": "Ralph Waldo Emerson"},
  {"quote": "The harder I work, the luckier I get.", "author": "Gary Player"},
  {"quote": "Dream big and dare to fail.", "author": "Norman Vaughan"},
  {"quote": "It always seems impossible until it’s done.", "author": "Nelson Mandela"},
  {"quote": "Start where you are. Use what you have. Do what you can.", "author": "Arthur Ashe"},
  {"quote": "Do what you can, with what you have, where you are.", "author": "Theodore Roosevelt"},
  {"quote": "Act as if what you do makes a difference. It does.", "author": "William James"},
  {"quote": "Success usually comes to those who are too busy to be looking for it.", "author": "Henry David Thoreau"},
  {"quote": "Don't be afraid to give up the good to go for the great.", "author": "John D. Rockefeller"},
  {"quote": "I find that the harder I work, the more luck I seem to have.", "author": "Thomas Jefferson"},
  {"quote": "Success is not how high you have climbed, but how you make a positive difference to the world.", "author": "Roy T. Bennett"},
  {"quote": "Hardships often prepare ordinary people for an extraordinary destiny.", "author": "C.S. Lewis"},
  {"quote": "Don’t wait. The time will never be just right.", "author": "Napoleon Hill"},
  {"quote": "If you are working on something exciting, it will keep you motivated.", "author": "Paulo Coelho"},
  {"quote": "Great things never come from comfort zones.", "author": "Unknown"},
  {"quote": "Push yourself, because no one else is going to do it for you.", "author": "Unknown"},
  {"quote": "Failure will never overtake me if my determination to succeed is strong enough.", "author": "Og Mandino"},
  {"quote": "The only limit to our realization of tomorrow will be our doubts of today.", "author": "Franklin D. Roosevelt"},
  {"quote": "Motivation is what gets you started. Habit is what keeps you going.", "author": "Jim Rohn"},
  {"quote": "Don’t watch the clock; do what it does. Keep going.", "author": "Sam Levenson"},
  {"quote": "The future belongs to those who believe in the beauty of their dreams.", "author": "Eleanor Roosevelt"},
  {"quote": "Don’t let yesterday take up too much of today.", "author": "Will Rogers"},
  {"quote": "It does not matter how slowly you go as long as you do not stop.", "author": "Confucius"},
  {"quote": "You don’t have to be great to start, but you have to start to be great.", "author": "Zig Ziglar"},
  {"quote": "The way to get started is to quit talking and begin doing.", "author": "Walt Disney"},
  {"quote": "If you want to achieve greatness stop asking for permission.", "author": "Unknown"},
  {"quote": "I attribute my success to this: I never gave or took any excuse.", "author": "Florence Nightingale"},
  {"quote": "The difference between ordinary and extraordinary is that little extra.", "author": "Jimmy Johnson"},
  {"quote": "The secret of getting ahead is getting started.", "author": "Mark Twain"},
  {"quote": "Quality is not an act, it is a habit.", "author": "Aristotle"},
  {"quote": "Success is walking from failure to failure with no loss of enthusiasm.", "author": "Winston Churchill"},
  {"quote": "Opportunities don't happen, you create them.", "author": "Chris Grosser"},
  {"quote": "Don’t be pushed around by the fears in your mind. Be led by the dreams in your heart.", "author": "Roy T. Bennett"},
  {"quote": "Challenges are what make life interesting and overcoming them is what makes life meaningful.", "author": "Joshua J. Marine"},
  {"quote": "Keep your eyes on the stars, and your feet on the ground.", "author": "Theodore Roosevelt"},
  {"quote": "You are never too old to set another goal or to dream a new dream.", "author": "C.S. Lewis"},
  {"quote": "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.", "author": "Christian D. Larson"},
  {"quote": "The harder the conflict, the greater the triumph.", "author": "George Washington"},
  {"quote": "Small daily improvements over time lead to stunning results.", "author": "Robin Sharma"},
  {"quote": "Don’t limit your challenges. Challenge your limits.", "author": "Unknown"},
  {"quote": "Sometimes we’re tested not to show our weaknesses, but to discover our strengths.", "author": "Unknown"},
  {"quote": "Start each day with a positive thought and a grateful heart.", "author": "Roy T. Bennett"}

]

@app.route("/")
def home():
    q = random.choice(quotes)
    return render_template("index.html", quote=q["quote"], author=q["author"])

if __name__ == "__main__":
    app.run(debug=True)
