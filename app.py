from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'krishna_janmashtami_2025_secret_key'

# Sample events data (in a real app, this would come from a database)
events = [
    {
        'id': 3,
        'title': '<span style="color: #FFD700; text-shadow: 2px 2px 4px rgba(0,0,0,0.5); font-weight: bold;">ಕಥಾ ವಾಚನ</span> <br> Krishna Balalile or Mythological Storytelling Competition',
        'description': 'Narrating Krishna\'s childhood plays or mythological stories with expression, voice modulation, and clarity. Share the divine tales of Lord Krishna through engaging storytelling.',
        'date': '06-09-2025',
        'time': '11:00 AM',
        'location': 'Room Number: 110, Dr. B. B. Hegde First Grade College, Kundapura',
        'image': 'krishna2.jfif',
        'category': 'Cultural',
        'rules': [
            'Time limit: 5 minutes',
            'Story must be scripture-based',
            'Expression, voice, and clarity will be considered in scoring',
            'The decision of the judges is final'
        ],
        'venue': 'Room Number: 110',
        'college': 'Dr. B. B. Hegde First Grade College, Kundapura',
        'coordinator': 'Mr. Harish Kanchan<br>Assistant Professor<br>Department of Computer Applications',
        'registration_deadline': '05/08/2025',
        'notice_date': '02/09/2025',
        'college_phone': '20000-576201',
        'duration': '5 minutes',
        'story_type': 'Scripture-based Krishna stories',
        'scoring_criteria': 'Expression, voice modulation, clarity',
        'participation_type': 'Individual',
        'motivational_sentence': 'Share enchanting tales of Shri Krishna and let His divine leelas inspire everyone.',
        'cta_title': 'Ready to narrate the divine tales of Shri Krishna?',
        'Google_form': 'https://docs.google.com/forms/d/e/1FAIpQLSfRv3I5d9HASnAlUhqWwbKG_OLOjIJKRYta3djFyHM_dEW7eg/viewform?usp=header',
    },
    {
        'id': 1,
        'title': 'Bhajane / Keertane Competition',
        'description': 'Singing devotional songs or hymns of Krishna. The competition is open to all students in group format only. A team must have a minimum of 3 members and maximum of 5 members (3 singers + 2 instrumentalists included).',
        'date': '08-09-2025',
        'time': '3:00 PM',
        'location': 'A. V. Hall, Dr. B. B. Hegde First Grade College, Kundapura',
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
        'college': 'Dr. B. B. Hegde First Grade College, Kundapura',
        'coordinator': 'Rashmi Gawadi<br>Assistant Professor<br>Department of Computer Applications',
        'registration_deadline': '06/09/2025',
        'notice_date': '02/09/2025',
        'college_phone': '20000-576201',
        'participation_type': 'Team',
        'motivational_sentence': 'Join us in melodious devotion and let your voice echo the divine bhajans and keertans of Shri Krishna.',
        'cta_title': 'Ready to sing the glories of Lord Krishna?',
        'Google_form': 'https://docs.google.com/forms/d/e/1FAIpQLSfRv3I5d9HASnAlUhqWwbKG_OLOjIJKRYta3djFyHM_dEW7eg/viewform?usp=header'
    },
    {
        'id': 5,
        'title': 'Quiz Competition',
        'description': 'Test your knowledge about Lord Krishna\'s life and teachings from the Mahabharata, Bhagavad Gita, and Shrimad Bhagavata. Participate in this exciting two-round quiz competition with your teammate.',
        'date': '08-09-2025',
        'time': '11:00 AM - 12:00 PM',
        'location': 'Library & Research Lab, Dr. B. B. Hegde First Grade College, Kundapura',
        'image': 'krishna2.jfif',
        'category': 'Academic',
        'rules': [
            'The competition consists of two rounds: Preliminary and Final',
            'Only team entries are permitted (2 members per team)',
            'Any number of teams can participate from each class',
            'Preliminary Round: 30 questions in 60 minutes',
            'Only 5 teams will be selected for the Final Round',
            'Final Round follows "Fastest Finger First" format',
            'Questions based on Krishna\'s life and teachings from Mahabharata, Bhagavad Gita, and Shrimad Bhagavata',
            'No mobile phones or electronic gadgets allowed',
            'No replacement of team members after registration',
            'Tie-breaker: 3 additional questions for final selection',
            'Judges\' decision will be final and binding'
        ],
        'venue': 'Library (Preliminary) & Research Lab (Final)',
        'college': 'Dr. B. B. Hegde First Grade College, Kundapura',
        'coordinator': 'Mr. Pranam B<br>Assistant Professor<br>Department of Computer Applications',
        'registration_deadline': '07/09/2025',
        'notice_date': '03/09/2025',
        'college_phone': '20000-576201',
        'team_size': '2 members per team',
        'rounds': 'Preliminary and Final',
        'preliminary_duration': '60 minutes for 30 questions',
        'final_format': 'Fastest Finger First',
        'topics': 'Krishna\'s life, Mahabharata, Bhagavad Gita, Shrimad Bhagavata',
        'participation_type': 'Team',
        'motivational_sentence': 'Challenge yourself with divine wisdom from the Bhagavad Gita and discover the depths of Lord Krishna\'s teachings.',
        'cta_title': 'Ready to test your Krishna knowledge?',
        'Google_form': 'https://docs.google.com/forms/d/e/1FAIpQLSf1Jv-Wt4u3cxpGldrBML_2hZv6ebPmDB-23a8P63x2c98D-A/viewform?usp=header'
    },
    {
        'id': 6,
        'title': 'Shloka/Bhagavad Gita Recitation Competition',
        'description': 'Recite verses from the Bhagavad Gita or Puranas with correct pronunciation and rhythm. Demonstrate your understanding of Sanskrit verses and their meanings.',
        'date': '10-09-2025',
        'time': '3:15 PM',
        'location': 'A. V. Hall, Dr. B. B. Hegde First Grade College, Kundapura',
        'image': 'krishna2.jfif',
        'category': 'Devotional',
        'rules': [
            'Pronunciation and rhythm must be correct',
            'Time limit: 2 minutes',
            'Extra marks for a verse with meaning',
            'The decision of the judges is final'
        ],
        'venue': 'A. V. Hall',
        'college': 'Dr. B. B. Hegde First Grade College, Kundapura',
        'coordinator': 'Mrs. Jayalakshmi K.<br>Assistant Professor<br>Department of Computer Applications',
        'registration_deadline': '08/09/2025',
        'notice_date': '01/09/2025',
        'college_phone': '20000-576201',
        'duration': '2 minutes',
        'contest_theme': 'Recitation of Gita or Purana verses',
        'scoring_criteria': 'Pronunciation, rhythm, and meaning explanation',
        'participation_type': 'Individual',
        'motivational_sentence': 'Let the divine shlokas of Bhagavad Gita flow through your voice and connect with the eternal wisdom of Lord Krishna.',
        'cta_title': 'Ready to chant the sacred verses of Krishna?',
        'Google_form': 'https://docs.google.com/forms/d/e/1FAIpQLSfRv3I5d9HASnAlUhqWwbKG_OLOjIJKRYta3djFyHM_dEW7eg/viewform?usp=header'
    },
    {
        'id': 2,
        'title': 'Janmashtami Greeting Card Making Competition',
        'description': 'Create beautiful handmade greeting cards celebrating Lord Krishna\'s birth. Express your creativity through art and design while spreading the message of Krishna Janmashtami.',
        'date': '12-09-2025',
        'time': '3:00 PM - 4:15 PM',
        'location': 'College Library, Dr. B. B. Hegde First Grade College, Kundapura',
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
        'college': 'Dr. B. B. Hegde First Grade College, Kundapura',
        'coordinator': 'Megha and Shivani Adiga<br>Assistant Professors<br>Department of Computer Applications',
        'registration_deadline': '10/09/2025',
        'notice_date': '02/09/2025',
        'college_phone': '20000-576201',
        'duration': '1 hour 15 minutes',
        'paper_size': 'A4/A5 size',
        'materials_allowed': 'Colored pens, crayons, watercolors, decorative materials',
        'participation_type': 'Team',
        'motivational_sentence': 'Express your devotion through beautiful handmade cards celebrating the birth of our beloved Lord Krishna.',
        'cta_title': 'Ready to create divine artistry for Krishna?',
        'Google_form': 'https://docs.google.com/forms/d/e/1FAIpQLSf0UEtQ0-DSPx2CfcQ8dtLz2u2K321OKV73Yc4tpgg2Lt57xw/viewform?usp=header',
        
    },
    {
        'id': 4,
        'title': 'Rangoli Competition',
        'description': 'Create beautiful Krishna-themed rangoli designs using colors, flowers, and decorative materials. Express your artistic talent while celebrating the divine presence of Lord Krishna.',
        'date': '13-09-2025',
        'time': '11:30 AM - 12:30 PM',
        'location': 'College Auditorium, Dr. B. B. Hegde First Grade College, Kundapura',
        'image': 'krishna2.jfif',
        'category': 'Creative',
        'rules': [
            'Only Krishna-related themes are allowed',
            'Time: 1 hour',
            'Rangoli can include colors, flowers, and other decorative materials',
            'Judges\' decision will be final'
        ],
        'venue': 'College Auditorium',
        'college': 'Dr. B. B. Hegde First Grade College, Kundapura',
        'coordinator': 'Mrs.Vijayashree A<br>Assistant Professor<br>Department of Computer Applications',
        'registration_deadline': '11/09/2025',
        'notice_date': '02/09/2025',
        'college_phone': '20000-576201',
        'duration': '1 hour',
        'theme_requirement': 'Only Krishna-related themes',
        'materials_allowed': 'Colors, flowers, and decorative materials',
        'participation_type': 'Team',
        'motivational_sentence': 'Create mesmerizing rangoli patterns that celebrate the artistic splendor of Lord Krishna\'s divine presence.',
        'cta_title': 'Ready to paint the divine beauty of Krishna?',
        'Google_form': 'https://docs.google.com/forms/d/e/1FAIpQLSf1Jv-Wt4u3cxpGldrBML_2hZv6ebPmDB-23a8P63x2c98D-A/viewform?usp=header',
    },
    {
        'id': 7,
        'title': 'Photography Competition',
        'description': 'Capture the essence of Krishna Janmashtami celebration through your lens. Take stunning photographs during the fest and showcase your creativity and composition skills.',
        'date': '23-09-2025',
        'time': '12:00 PM (Submission Deadline)',
        'location': 'Lab I, Dr. B. B. Hegde First Grade College, Kundapura',
        'image': 'krishna2.jfif',
        'category': 'Creative',
        'rules': [
            'This is an Individual Contest',
            'The Theme will be revealed on the day of the fest',
            'Color grading is allowed, you can use any software for it',
            'The use of generative fill or any AI Tools will result in disqualification',
            'Photos must be taken on the day of fest itself',
            'Photos must be taken through mobile phones',
            'Contestants are not allowed to venture outside the campus',
            'Photo will be judged based on theme, relevance, creativity, composition, grading and overall vibe'
        ],
        'venue': 'Lab I',
        'college': 'Dr. B. B. Hegde First Grade College, Kundapura',
        'coordinator': 'Mrs. Wilma Sharal Cornelio<br>Assistant Professor<br>Dept. Of Computer Applicationss',
        'registration_deadline': '18/09/2025',
        'notice_date': '04/09/2025',
        'college_phone': '20000-576201',
        'contest_type': 'Individual Contest',
        'theme_reveal': 'Theme will be revealed on the day of the fest',
        'submission_deadline': '12:00 PM on celebration day',
        'equipment_requirement': 'Mobile phones only',
        'campus_restriction': 'Photos must be taken within campus only',
        'judging_criteria': 'Theme, relevance, creativity, composition, grading, overall vibe',
        'participation_type': 'Individual',
        'motivational_sentence': 'Freeze the magic of Krishna Janmashtami through your lens and showcase the divine celebrations in stunning photographs.',
        'cta_title': 'Ready to capture Krishna\'s divine moments?',
        'Google_form': 'https://docs.google.com/forms/d/e/1FAIpQLSfRv3I5d9HASnAlUhqWwbKG_OLOjIJKRYta3djFyHM_dEW7eg/viewform?usp=header'
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
    response.headers['Content-Type'] = 'Applications/javascript'
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
