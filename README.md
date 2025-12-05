# 🧠 Wiki Quiz App

Transform any Wikipedia article into an interactive, AI-powered learning experience with beautiful UI and comprehensive features.

![Version](https://img.shields.io/badge/version-2.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-orange)

## **🌐 Live Demo:**   [https://wiki-quiz-apps.onrender.com/app.html](https://wiki-quiz-apps.onrender.com/app.html)    

**🎨 Frontend:** [https://wiki-quiz-apps.onrender.com/app.html](https://wiki-quiz-apps.onrender.com/app.html)      
**🔧 Backend API:** [https://wiki-quiz-app.onrender.com](https://wiki-quiz-app.onrender.com)  
**📚 API Documentation:** [https://wiki-quiz-app.onrender.com/docs](https://wiki-quiz-app.onrender.com/docs)

> **Note:** The backend may take 30-60 seconds to wake up on first request (free tier limitation).

## 🌟 Features

### 🎯 Core Features
- **AI-Powered Quiz Generation** - Automatically generates 5-10 intelligent questions from any Wikipedia article
- **Cloud Database** - Uses Neon PostgreSQL (no local database setup required)
- **Beautiful Modern UI** - Stunning glassmorphism design with gradient backgrounds and smooth animations
- **Fully Responsive** - Works seamlessly on desktop, tablet, and mobile devices

### 🎮 Interactive Learning
- **Two Quiz Modes:**
  - **View Mode** - See all questions with answers and explanations upfront
  - **Take Quiz Mode** - Interactive quiz with instant feedback and scoring
- **Real-time Score Tracking** - Get your score and percentage after completing the quiz
- **Color-coded Feedback** - Green for correct, red for incorrect answers

### 📊 Enhanced Quiz Display
- **Difficulty Badges** - Visual indicators for Easy (Green), Medium (Yellow), and Hard (Red) questions
- **Key Entities** - Displays important people, organizations, and locations mentioned in the article
- **Article Sections** - Shows the structure and main sections of the Wikipedia article
- **Related Topics** - Suggests 3-5 related Wikipedia topics to explore next
- **Comprehensive Explanations** - Each question includes a detailed explanation of the correct answer

### 📚 Quiz History
- **Complete History** - View all previously generated quizzes with serial numbers
- **Quick Access** - Click "View Details" to revisit any past quiz
- **Persistent Storage** - All quizzes are saved in the cloud database
- **Timestamps** - See when each quiz was generated

### 🎨 Premium Design
- **Modern Glassmorphism** - Translucent cards with backdrop blur effects
- **Gradient Backgrounds** - Beautiful purple gradient (customizable)
- **Smooth Animations** - Fade-in effects and hover transitions
- **Professional Typography** - Uses Inter font for clean, modern look
- **Micro-interactions** - Buttons and cards respond to hover and clicks

## 📸 Screenshots

### Main Interface
<img width="1913" height="964" alt="Screenshot 2025-12-06 012626" src="https://github.com/user-attachments/assets/2f0d0599-d1b8-481a-a113-2c0e94079f52" />

### Quiz View Mode
<img width="1901" height="857" alt="Screenshot 2025-12-06 002712" src="https://github.com/user-attachments/assets/a10223f0-3386-45f4-8c7a-3830182ddeaf" />

### Interactive Quiz Mode
<img width="1900" height="866" alt="Screenshot 2025-12-06 002621" src="https://github.com/user-attachments/assets/65a95a34-63d8-466d-9a22-9ba1602ed37e" />

### After interaction
<img width="1898" height="863" alt="Screenshot 2025-12-06 002836" src="https://github.com/user-attachments/assets/36a09e03-7f10-4995-8270-cec470d38699" />

### Result after completing Quiz
<img width="1897" height="864" alt="Screenshot 2025-12-06 002812" src="https://github.com/user-attachments/assets/df450334-307c-4f02-88ae-0f258842d3a0" />

### Quiz History
<img width="1898" height="967" alt="Screenshot 2025-12-06 002910" src="https://github.com/user-attachments/assets/cd560d1b-e3ca-43c6-8f9e-844f7c65d02b" />

---

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Modern, fast Python web framework
- **SQLAlchemy** - Powerful database ORM
- **Neon PostgreSQL** - Serverless cloud database (free tier available)
- **Google Gemini AI** - Advanced LLM for intelligent quiz generation
- **BeautifulSoup4** - Wikipedia article scraping
- **LangChain** - LLM integration framework
- **Pydantic** - Data validation

### Frontend
- **HTML5/CSS3/JavaScript** - Pure vanilla stack (no framework dependencies)
- **Modern CSS** - Glassmorphism, gradients, and animations
- **Google Fonts (Inter)** - Professional typography
- **Responsive Design** - Mobile-first approach

## 📋 Prerequisites

Before you begin, ensure you have:

- **Python 3.8 or higher** installed
- **A Neon account** (free at [neon.tech](https://neon.tech))
- **A Google Gemini API key** (free at [Google AI Studio](https://aistudio.google.com/app/apikey))

## 🚀 Installation & Setup

### Step 1: Clone the Repository

### Step 2: Install Python Dependencies
**Required packages:**
- fastapi
- uvicorn[standard]
- sqlalchemy
- psycopg2-binary
- pydantic
- beautifulsoup4
- httpx
- langchain
- langchain-community
- langchain-google-genai
- python-dotenv

### Step 3: Set Up Neon Database

### Step 4: Get Google Gemini API Key

### Step 5: Configure Environment Variables

### Step 6: Create Database Tables

## 🎮 Running the Application

You need to run **two servers** simultaneously:

### Terminal 1: Start the Backend API

```bash
uvicorn backend.app.main:app --reload --host 127.0.0.1 --port 8000
```

**Expected output:**
```
INFO: Uvicorn running on http://127.0.0.1:8000
INFO: Application startup complete.
```

### Terminal 2: Start the Frontend Server

```bash
python -m http.server 5500 --directory frontend
```

**Expected output:**
```
Serving HTTP on :: port 5500 (http://[::]:5500/) ...
```

### Step 3: Open in Browser

Navigate to: **http://localhost:5500/app.html**

🎉 **The app is now running!**

## 📖 How to Use

### 1️⃣ Generate a Quiz

1. **Enter a Wikipedia URL** in the input field
   - Example: `https://en.wikipedia.org/wiki/Artificial_intelligence`
   - Example: `https://en.wikipedia.org/wiki/Python_(programming_language)`
   - Example: `https://en.wikipedia.org/wiki/Albert_Einstein`

2. **Click "Generate Quiz"**
   - Wait 10-60 seconds (depending on article length)
   - The AI will analyze the article and create intelligent questions

3. **View the Generated Quiz**
   - See the article title and summary
   - Explore key entities (people, organizations, locations)
   - Review article sections
   - Read all questions with difficulty badges

### 2️⃣ Take the Quiz (Interactive Mode)

1. **Click "Take Quiz" button** to switch to interactive mode
2. **Select your answers** by clicking on the options
3. **Complete all questions** to see your score
4. **Review results:**
   - Green = Correct answer
   - Red = Your incorrect answer
   - See explanations for all questions
   - View your score and percentage

### 3️⃣ Explore Related Topics

- Scroll to the bottom to see **Related Topics**
- Click on any topic tag to explore similar subjects
- Build your knowledge progressively

### 4️⃣ Access Quiz History

1. **Click "Past Quizzes" tab**
2. **Browse all generated quizzes** with serial numbers
3. **Click "View Details"** to revisit any quiz
4. **See timestamps** of when each quiz was created

## 🔧 API Endpoints

The backend provides the following REST API endpoints:

- `GET /` - Health check
- `POST /generate` - Generate quiz from Wikipedia URL
  - Request body: `{"url": "https://en.wikipedia.org/wiki/..."}`
  - Returns: Complete quiz with questions, entities, sections, and related topics
- `GET /history` - Get all quiz history
  - Returns: List of all generated quizzes with metadata
- `GET /quiz/{quiz_id}` - Get specific quiz details
  - Returns: Full quiz data for the specified ID
- `GET /docs` - Interactive API documentation (Swagger UI)
  - Visit: http://127.0.0.1:8000/docs

## 🎨 Customization

### Change Color Scheme

Edit `frontend/app.html` and modify the CSS variables:

```css
/* Change gradient background */
body {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  /* Try: #f093fb 0%, #f5576c 100% for pink */
  /* Try: #4facfe 0%, #00f2fe 100% for blue */
}

/* Change primary color */
.btn, .tab-btn.active {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
```

### Adjust Quiz Length

Edit `backend/app/llm.py` to change the number of questions:

```python
# Change "5-10 questions" to your preferred range
- quiz: an array of 5-10 questions.
```


## 📁 Project Structure

```
Wiki Quiz App/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py          # FastAPI app entry point
│   │   ├── router.py        # API endpoints
│   │   ├── database.py      # Database configuration
│   │   ├── models.py        # SQLAlchemy models
│   │   ├── schemas.py       # Pydantic schemas
│   │   ├── scraper.py       # Wikipedia scraper
│   │   └── llm.py           # Gemini AI integration
│   └── requirements.txt     # Python dependencies
├── frontend/
│   ├── app.html            # Main application (ENHANCED VERSION)
│   ├── index.html          # Legacy version
│   ├── index_new.html      # Alternative version
│   ├── style.css           # Legacy styles
│   └── script.js           # Legacy JavaScript
├── .env                    # Environment variables (create this)
├── create_db.py           # Database initialization script
├── test_api.py            # API testing script
└── README.md              # This file
```

**Note:** Use `app.html` for the full enhanced experience with all features!

## 🌐 Deployment

This app is currently deployed and live!

### Live URLs

- **Frontend:** [https://wiki-quiz-apps.onrender.com/](https://wiki-quiz-apps.onrender.com/app.html)
- **Backend API:** https://wiki-quiz-app.onrender.com
- **API Docs:** https://wiki-quiz-app.onrender.com/docs

### Deployment Stack

**Backend (Render Web Service)**
- Platform: Render
- Runtime: Python 3
- Database: Neon PostgreSQL (Serverless)
- Build Command: `pip install -r backend/requirements.txt`
- Start Command: `uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT`

**Frontend (Render Static Site)**
- Platform: Render
- Root Directory: `frontend`
- Publish Directory: `.`
- Auto-deploy: Enabled (on GitHub push)




## 🎯 Future Enhancements

Potential features for future versions:

- [ ] User authentication and personal quiz history
- [ ] Quiz sharing via unique links
- [ ] Export quiz to PDF
- [ ] Multiple language support
- [ ] Custom quiz difficulty settings
- [ ] Timed quiz mode with countdown
- [ ] Leaderboard and achievements
- [ ] Quiz categories and tags
- [ ] Voice-based quiz mode
- [ ] Mobile app (React Native)

## 📝 License

MIT License - Feel free to use this project for learning and development.







