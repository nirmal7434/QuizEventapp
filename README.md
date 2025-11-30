# Quiz Event App - LearnHub

A comprehensive Django-based web application for interactive quizzes and event management. This application allows users to take quizzes, view results, and browse upcoming events in a modern, user-friendly interface.

## 📋 Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Database Models](#database-models)
- [URL Routing](#url-routing)
- [Admin Panel](#admin-panel)
- [Templates](#templates)
- [Authentication](#authentication)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

### Quiz Management
- **Multiple Quiz Types**: Support for Multiple Choice Questions (MCQ) and Text Answer questions
- **Interactive Quiz Taking**: User-friendly interface for taking quizzes
- **Automatic Scoring**: Real-time score calculation and percentage display
- **Result Tracking**: Detailed results with performance feedback
- **Quiz Listing**: Browse all available quizzes with statistics

### Event Management
- **Event Listings**: View all upcoming and past events
- **Event Details**: Display event title, description, date, and location
- **Event Statistics**: Track total events, upcoming events, and cities
- **Event Status**: Visual indicators for upcoming vs. past events

### User Features
- **User Registration**: Create new accounts with username, email, and password
- **User Authentication**: Secure login and logout functionality
- **User Submissions**: Track quiz attempts and scores
- **Personalized Results**: View individual quiz performance

### UI/UX
- **Modern Design**: Beautiful, responsive interface built with Tailwind CSS
- **Mobile-Friendly**: Fully responsive design for all devices
- **Interactive Elements**: Smooth animations and hover effects
- **Font Awesome Icons**: Rich iconography throughout the application

## 🛠 Technology Stack

### Backend
- **Django 5.0.7**: High-level Python web framework
- **Python 3.x**: Programming language
- **SQLite**: Lightweight database for development

### Frontend
- **Tailwind CSS 4.1.17**: Utility-first CSS framework
- **Font Awesome 6.4.0**: Icon library
- **JavaScript**: Client-side interactivity
- **HTML5**: Markup language

### Development Tools
- **django-tailwind**: Django integration for Tailwind CSS
- **PostCSS**: CSS processing
- **Autoprefixer**: CSS vendor prefixing

## 📁 Project Structure

```
quiezproject/
├── QuizEventApp/
│   ├── manage.py                 # Django management script
│   ├── db.sqlite3                # SQLite database
│   ├── quizapp/                  # Main application
│   │   ├── __init__.py
│   │   ├── admin.py              # Admin configuration
│   │   ├── apps.py               # App configuration
│   │   ├── models.py             # Database models
│   │   ├── views.py              # View functions
│   │   ├── tests.py              # Unit tests
│   │   ├── migrations/           # Database migrations
│   │   │   └── 0001_initial.py
│   │   ├── static/               # Static files
│   │   └── template/             # HTML templates
│   │       ├── home.html         # Home page
│   │       ├── quiz_list.html    # Quiz listing page
│   │       ├── take_quiz.html    # Quiz taking page
│   │       ├── result.html       # Results page
│   │       └── events.html       # Events listing page
│   ├── QuizEventApp/             # Project settings
│   │   ├── __init__.py
│   │   ├── settings.py           # Django settings
│   │   ├── urls.py               # URL routing
│   │   ├── wsgi.py               # WSGI configuration
│   │   └── asgi.py               # ASGI configuration
│   └── theme/                    # Tailwind theme
│       ├── __init__.py
│       ├── apps.py
│       ├── package.json          # Node dependencies
│       ├── static/               # Compiled CSS
│       │   └── css/
│       │       └── dist/
│       │           └── styles.css
│       ├── static_src/           # Source CSS
│       │   └── src/
│       │       └── styles.css
│       └── templates/
│           └── base.html         # Base template
└── README.md                     # This file
```

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Node.js and npm (for Tailwind CSS)

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd quiezproject
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Python Dependencies

```bash
cd QuizEventApp
pip install django==5.0.7 django-tailwind
```

### Step 4: Install Node Dependencies

```bash
cd theme
npm install
```

### Step 5: Run Database Migrations

```bash
cd ..
python manage.py migrate
```

### Step 6: Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

This allows you to access the Django admin panel to manage quizzes, questions, and events.

### Step 7: Run Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## ⚙️ Configuration

### Django Settings

The main configuration file is located at `QuizEventApp/QuizEventApp/settings.py`. Key settings include:

- **SECRET_KEY**: Django secret key (change in production!)
- **DEBUG**: Set to `False` in production
- **ALLOWED_HOSTS**: Add your domain in production
- **INSTALLED_APPS**: Includes `quizapp`, `tailwind`, and `theme`
- **DATABASES**: SQLite by default (change for production)

### Tailwind Configuration

Tailwind CSS is configured through the `theme` app. The compiled CSS is located at `theme/static/css/dist/styles.css`.

## 📖 Usage

### For End Users

1. **Home Page**: Visit the homepage to see an overview of available features
2. **Browse Quizzes**: Click "Quizzes" to see all available quizzes
3. **Take a Quiz**: Select a quiz and answer all questions
4. **View Results**: After submission, see your score and performance
5. **Browse Events**: Click "Events" to see upcoming and past events
6. **Register/Login**: Create an account or sign in to track your progress

### For Administrators

1. **Access Admin Panel**: Navigate to `/admin/` and login with superuser credentials
2. **Manage Quizzes**: Create, edit, and delete quizzes
3. **Manage Questions**: Add questions to quizzes with multiple choice or text answers
4. **Manage Answers**: Set correct answers for MCQ questions
5. **View Submissions**: Monitor user quiz submissions and scores
6. **Manage Events**: Create and manage learning events

## 🗄️ Database Models

### Quiz Model
- `title`: CharField (max_length=100) - Quiz title
- `description`: TextField - Optional quiz description
- `created_at`: DateTimeField - Creation timestamp
- `updated_at`: DateTimeField - Last update timestamp

### Question Model
- `quiz`: ForeignKey to Quiz - Parent quiz
- `text`: CharField (max_length=200) - Question text
- `question_type`: CharField - Either 'mcq' or 'text'
- `created_at`: DateTimeField - Creation timestamp

### Answer Model
- `question`: ForeignKey to Question - Parent question
- `text`: CharField (max_length=200) - Answer text
- `is_correct`: BooleanField - Whether this is the correct answer

### UserSubmission Model
- `quiz`: ForeignKey to Quiz - Quiz taken
- `user_name`: CharField (max_length=50) - User identifier
- `score`: IntegerField - Number of correct answers
- `submitted_at`: DateTimeField - Submission timestamp

### UserAnswer Model
- `submission`: ForeignKey to UserSubmission - Parent submission
- `question`: ForeignKey to Question - Question answered
- `answer`: ForeignKey to Answer (nullable) - Selected answer
- `is_correct`: BooleanField - Whether answer was correct

### Event Model
- `title`: CharField (max_length=50) - Event title
- `description`: TextField - Event description
- `date`: DateField - Event date
- `location`: CharField (max_length=50) - Event location

## 🔗 URL Routing

The application uses the following URL patterns:

| URL Pattern | View Function | Description |
|------------|---------------|-------------|
| `/` | `home` | Home page with features overview |
| `/quizzes/` | `quiz_list` | List all available quizzes |
| `/quiz/<quiz_id>/` | `take_quiz` | Display quiz questions |
| `/quiz/<quiz_id>/submit/` | `submit_quiz` | Process quiz submission |
| `/events/` | `events_list` | List all events |
| `/register/` | `register_view` | User registration |
| `/login/` | `login_view` | User authentication |
| `/logout/` | `logout_view` | User logout |
| `/admin/` | Django admin | Admin panel |

## 👨‍💼 Admin Panel

All models are registered in the Django admin panel:

- **Quiz**: Manage quiz titles and descriptions
- **Question**: Add/edit questions for quizzes
- **Answer**: Set correct answers for MCQ questions
- **UserSubmission**: View user quiz attempts
- **UserAnswer**: Review individual answers
- **Event**: Manage learning events

Access the admin panel at `/admin/` after creating a superuser.

## 🎨 Templates

### Home Page (`home.html`)
- Hero section with call-to-action buttons
- Feature cards highlighting quiz and event functionality
- Login/Register modals
- Responsive navigation
- Footer with links and social media

### Quiz List (`quiz_list.html`)
- Grid layout of available quizzes
- Statistics dashboard (total quizzes, categories, questions)
- Quiz cards with start button
- Empty state for no quizzes

### Take Quiz (`take_quiz.html`)
- Question-by-question display
- Radio buttons for MCQ questions
- Text areas for text answer questions
- Form validation before submission
- Question counter and progress indicator

### Results (`result.html`)
- Score display with visual progress circle
- Percentage calculation
- Performance feedback based on score
- Action buttons (retry, back to list)
- Submission details

### Events (`events.html`)
- Event cards with date, location, and description
- Statistics (total events, upcoming, cities)
- Upcoming vs. past event indicators
- RSVP buttons (UI only)

## 🔐 Authentication

The application includes user authentication features:

### Registration
- Username validation (unique check)
- Email field
- Password confirmation
- Error messages for validation failures

### Login
- Username and password authentication
- Django's built-in authentication system
- Success/error message display

### Logout
- Secure session termination
- Redirect to home page

### User Management
- Uses Django's built-in `User` model
- Password hashing handled automatically
- Session management via Django middleware

## 🧪 Development

### Running Tests

```bash
python manage.py test
```

### Creating Migrations

After modifying models:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Collecting Static Files

For production:

```bash
python manage.py collectstatic
```

### Tailwind CSS Development

To rebuild Tailwind CSS:

```bash
cd theme
npm run build
```

## 🚧 Future Enhancements

Potential improvements for the application:

- [ ] User profiles and dashboard
- [ ] Quiz categories and tags
- [ ] Time limits for quizzes
- [ ] Leaderboards and rankings
- [ ] Email notifications for events
- [ ] Quiz analytics and reports
- [ ] Export quiz results to PDF
- [ ] Social sharing features
- [ ] Comments and ratings
- [ ] API endpoints for mobile apps

## 🐛 Troubleshooting

### Common Issues

1. **ModuleNotFoundError**: Ensure virtual environment is activated and dependencies are installed
2. **Database errors**: Run migrations with `python manage.py migrate`
3. **Static files not loading**: Run `python manage.py collectstatic`
4. **Tailwind styles not applying**: Rebuild CSS with `npm run build` in theme directory

### Debug Mode

The application runs in DEBUG mode by default. For production:
- Set `DEBUG = False` in settings.py
- Configure `ALLOWED_HOSTS`
- Use a production database (PostgreSQL recommended)
- Set up proper static file serving

## 📝 Notes

- The application uses SQLite by default, suitable for development
- For production, consider using PostgreSQL or MySQL
- The SECRET_KEY in settings.py should be changed for production
- User authentication is basic; consider adding email verification
- Event RSVP functionality is UI-only; backend implementation needed

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

Developed as a Django learning project for interactive quiz and event management.

## 🙏 Acknowledgments

- Django community for excellent documentation
- Tailwind CSS for the utility-first CSS framework
- Font Awesome for comprehensive icon library

---

**Note**: This is a development project. For production deployment, ensure proper security measures, database configuration, and environment variable management.

