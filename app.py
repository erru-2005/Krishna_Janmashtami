from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'krishna_janmashtami_2025_secret_key'

# Sample events data (in a real app, this would come from a database)
events = [
    {
        'id': 1,
        'title': 'Bhajane / Keertane Competition',
        'description': 'Singing devotional songs or hymns of Krishna. The competition is open to all students in group format only. A team must have a minimum of 3 members and maximum of 5 members (3 singers + 2 instrumentalists included).',
        'date': '08-09-2025',
        'time': '3:00 PM',
        'location': 'A. V. Hall, Dr. B. B. Hegde First Grade College, Kundapur',
        'image': 'krishna2.jfif',
        'category': 'Devotional',
        'rules': [
            'Time limit: 3+1 minutes',
            'Instruments can be used, but participants must bring their own',
            'The song must be about Krishna',
            'Competition will be held in group format only',
            'A team must have a minimum of 3 members and maximum of 5 members (3 singers + 2 instrumentalists included)',
            'Teams can use instruments (tabla, tala, harmonium, keyboard etc.)',
            'The decision of the judges is final'
        ],
        'venue': 'A. V. Hall',
        'college': 'Dr. B. B. Hegde First Grade College, Kundapur',
        'coordinator': 'Rashmi Gawadi, Assistant Professor, Department of Computer Application',
        'registration_deadline': '06/09/2025',
        'notice_date': '02/09/2025',
        'college_phone': '20000-576201'
    },
    {
        'id': 2,
        'title': 'Janmashtami Greeting Card Making Competition',
        'description': 'Create beautiful handmade greeting cards celebrating Lord Krishna\'s birth. Express your creativity through art and design while spreading the message of Krishna Janmashtami.',
        'date': '12-09-2025',
        'time': '3:00 PM - 4:15 PM',
        'location': 'College Library, Dr. B. B. Hegde First Grade College, Kundapur',
        'image': 'krishna2.jfif',
        'category': 'Creative',
        'rules': [
            'Time: 1 hour 15 minutes',
            'The greeting card should be handmade (do not use ready-made cards available in the market)',
            'The paper size should be A4/A5 size',
            'Colored pens, crayons, watercolors, or any decorative materials can be used',
            'The card should have a message/quote/image related to "Shri Krishna Janmashtami"',
            'Everyone should submit only one card',
            'The judging will be based on creativity, decoration, and relevance of the topic',
            'The decision of the judges is final'
        ],
        'venue': 'College Library',
        'college': 'Dr. B. B. Hegde First Grade College, Kundapur',
        'coordinator': 'Megha and Shivani Adiga, Assistant Professors, Department of Computer Application',
        'registration_deadline': '10/09/2025',
        'notice_date': '02/09/2025',
        'college_phone': '20000-576201',
        'duration': '1 hour 15 minutes',
        'paper_size': 'A4/A5 size',
        'materials_allowed': 'Colored pens, crayons, watercolors, decorative materials'
    },
    {
        'id': 3,
        'title': 'Krishna Balalile or Mythological Storytelling Competition',
        'description': 'Narrating Krishna\'s childhood plays or mythological stories with expression, voice modulation, and clarity. Share the divine tales of Lord Krishna through engaging storytelling.',
        'date': '08-09-2025',
        'time': '11:00 AM',
        'location': 'Room Number: 110, Dr. B. B. Hegde First Grade College, Kundapur',
        'image': 'krishna2.jfif',
        'category': 'Cultural',
        'rules': [
            'Time limit: 5 minutes',
            'Story must be scripture-based',
            'Expression, voice, and clarity will be considered in scoring',
            'The decision of the judges is final'
        ],
        'venue': 'Room Number: 110',
        'college': 'Dr. B. B. Hegde First Grade College, Kundapur',
        'coordinator': 'Shri Harish Kanchan, Assistant Professor, Department of Computer Application',
        'registration_deadline': '05/08/2025',
        'notice_date': '02/09/2025',
        'college_phone': '20000-576201',
        'duration': '5 minutes',
        'story_type': 'Scripture-based Krishna stories',
        'scoring_criteria': 'Expression, voice modulation, clarity'
    }
]

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/home')
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

@app.route('/sw.js')
def service_worker():
    response = app.send_static_file('sw.js')
    response.headers['Content-Type'] = 'application/javascript'
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
