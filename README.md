# Krishna Janmashtami 2024 - Flask Web Application

A beautiful and modern Flask web application for managing and promoting Krishna Janmashtami celebrations. This application provides event management, registration, and information sharing capabilities for the divine festival.

## 🌟 Features

- **Modern Responsive Design**: Beautiful UI with Bootstrap 5 and custom styling
- **Event Management**: Complete event listing with categories and details
- **Registration System**: User-friendly registration form for events
- **Gallery**: Photo gallery showcasing previous celebrations
- **Contact Form**: Easy communication with organizers
- **Search & Filter**: Advanced search and filtering for events
- **Mobile Friendly**: Fully responsive design for all devices

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Krishna_Janmashtami_Website
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   
   **Windows:**
   ```bash
   venv\Scripts\activate
   ```
   
   **macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser**
   Navigate to `http://localhost:5000`

## 📁 Project Structure

```
Krishna_Janmashtami_Website/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── templates/            # HTML templates
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Home page
│   ├── events.html       # Events listing page
│   ├── event_detail.html # Individual event details
│   ├── register.html     # Registration form
│   ├── about.html        # About page
│   ├── contact.html      # Contact page
│   └── gallery.html      # Photo gallery
└── static/               # Static files
    ├── css/
    │   └── style.css     # Custom styles
    ├── js/
    │   └── main.js       # Custom JavaScript
    └── images/           # Image assets
```

## 🎨 Features Overview

### Home Page
- Hero section with call-to-action
- Featured events showcase
- Festival highlights
- Quick statistics

### Events Management
- Complete event listings
- Search and filter functionality
- Event categories (Devotional, Cultural, Entertainment, Community)
- Detailed event information

### Registration System
- User-friendly registration form
- Event selection
- Personal information collection
- Terms and conditions
- Form validation

### Gallery
- Photo gallery with categories
- Modal image viewer
- Filter by event type
- Responsive grid layout

### Contact & About
- Contact form with validation
- Organizer information
- FAQ section
- Social media links

## 🛠️ Customization

### Adding New Events
Edit the `events` list in `app.py`:

```python
events = [
    {
        'id': 5,
        'title': 'New Event Title',
        'description': 'Event description',
        'date': '2024-08-29',
        'time': '14:00',
        'location': 'Event Location',
        'image': 'event-image.jpg',
        'category': 'Devotional'
    }
]
```

### Styling
- Main styles are in `templates/base.html`
- Additional custom styles in `static/css/style.css`
- Color scheme can be modified in CSS variables

### Adding Images
1. Place images in `static/images/`
2. Update image references in templates
3. For gallery, add new items in `templates/gallery.html`

## 🔧 Configuration

### Environment Variables
Create a `.env` file for production:

```env
FLASK_ENV=production
SECRET_KEY=your-secret-key-here
```

### Database Integration
For production, consider adding a database:

```python
# Example with SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
db = SQLAlchemy(app)
```

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production Deployment
1. Set up a production server (e.g., Ubuntu with Nginx)
2. Install Python and dependencies
3. Use Gunicorn for WSGI server:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:8000 app:app
   ```

### Docker Deployment
Create a `Dockerfile`:

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

## 📱 Mobile Responsiveness

The application is fully responsive and works on:
- Desktop computers
- Tablets
- Mobile phones
- All modern browsers

## 🎯 Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Internet Explorer 11+

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Bootstrap 5 for the responsive framework
- Font Awesome for icons
- Google Fonts for typography
- Flask community for the excellent framework

## 📞 Support

For support and questions:
- Email: info@krishnajanmashtami.com
- Phone: +1 (555) 123-4567
- Website: www.krishnajanmashtami.com

## 🔄 Updates

### Version 1.0.0
- Initial release
- Basic event management
- Registration system
- Gallery functionality
- Contact and about pages

---

**Jai Shri Krishna! 🙏**

*May Lord Krishna's divine blessings be with you always.*
