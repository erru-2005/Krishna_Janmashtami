from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'krishna_janmashtami_2024_secret_key'

# Sample events data (in a real app, this would come from a database)
events = [
    {
        'id': 1,
        'title': 'Bhajan Sandhya',
        'description': 'Evening devotional songs and bhajans dedicated to Lord Krishna',
        'date': '2024-08-26',
        'time': '18:00',
        'location': 'Main Temple Hall',
        'image': 'bhajan.jpg',
        'category': 'Devotional'
    },
    {
        'id': 2,
        'title': 'Dahi Handi Celebration',
        'description': 'Traditional Dahi Handi breaking ceremony with cultural performances',
        'date': '2024-08-27',
        'time': '10:00',
        'location': 'Temple Grounds',
        'image': 'dahi-handi.jpg',
        'category': 'Cultural'
    },
    {
        'id': 3,
        'title': 'Krishna Leela Drama',
        'description': 'Dramatic presentation of Lord Krishna\'s divine pastimes',
        'date': '2024-08-27',
        'time': '19:00',
        'location': 'Cultural Center',
        'image': 'drama.jpg',
        'category': 'Entertainment'
    },
    {
        'id': 4,
        'title': 'Prasad Distribution',
        'description': 'Distribution of blessed food and sweets to devotees',
        'date': '2024-08-28',
        'time': '12:00',
        'location': 'Community Hall',
        'image': 'prasad.jpg',
        'category': 'Community'
    }
]

@app.route('/')
def home():
    return render_template('index.html', events=events[:3])

@app.route('/events')
def events_page():
    return render_template('events.html', events=events)

@app.route('/event/<int:event_id>')
def event_detail(event_id):
    event = next((e for e in events if e['id'] == event_id), None)
    if event:
        return render_template('event_detail.html', event=event)
    else:
        flash('Event not found!', 'error')
        return redirect(url_for('events_page'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        # In a real app, you would send an email or save to database
        flash(f'Thank you {name}! Your message has been sent successfully. We will get back to you soon.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        event_id = request.form.get('event_id')
        
        # In a real app, you would save this to a database
        flash(f'Thank you {name}! You have successfully registered for the event.', 'success')
        return redirect(url_for('events_page'))
    
    return render_template('register.html', events=events)

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
