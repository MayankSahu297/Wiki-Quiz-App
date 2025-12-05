# 🧠 Wiki Quiz App

Transform any Wikipedia article into an interactive, AI-powered learning experience with beautiful UI and comprehensive features.

![Version](https://img.shields.io/badge/version-2.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-orange)

## 🌐 Live Demo

**🎨 Frontend:** [https://wiki-quiz-apps.onrender.com/](https://wiki-quiz-apps.onrender.com/)  
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

```bash
git clone <your-repo-url>
cd "Wiki Quiz App"
```

### Step 2: Install Python Dependencies

```bash
pip install -r backend/requirements.txt
```

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

1. Go to [neon.tech](https://neon.tech) and sign up (free)
2. Create a new project named `wiki-quiz-app`
3. Copy your connection string (it looks like):
   ```
   postgresql://username:password@ep-xxxxx.region.aws.neon.tech/dbname?sslmode=require
   ```

### Step 4: Get Google Gemini API Key

1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated API key

### Step 5: Configure Environment Variables

Create a `.env` file in the project root directory:

```env
POSTGRES_URL=postgresql://your_neon_connection_string_here
GEMINI_API_KEY=your_gemini_api_key_here
USE_MOCK_LLM=false
```

**Configuration Options:**
- `POSTGRES_URL` - Your Neon PostgreSQL connection string
- `GEMINI_API_KEY` - Your Google Gemini API key
- `USE_MOCK_LLM` - Set to `true` for testing without API calls (uses demo quizzes)

### Step 6: Create Database Tables

```bash
python create_db.py
```

You should see: `✅ DB tables created`

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

## 🐛 Troubleshooting

### Database Connection Error
- ✅ Verify your Neon connection string in `.env`
- ✅ Check that your Neon database is active (not paused)
- ✅ Ensure the connection string includes `?sslmode=require`
- ✅ Run `python create_db.py` to create tables

### Gemini API Quota Exceeded
- ✅ Get a new API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
- ✅ Or set `USE_MOCK_LLM=true` in `.env` to use demo quizzes
- ✅ Check your API usage at [Google AI Studio](https://aistudio.google.com)

### Port Already in Use
- ✅ Change backend port: `uvicorn backend.app.main:app --reload --port 8001`
- ✅ Change frontend port: `python -m http.server 5501 --directory frontend`
- ✅ Update the URL in your browser accordingly

### Frontend Not Loading
- ✅ Ensure the frontend server is running on port 5500
- ✅ Check browser console (F12) for errors
- ✅ Clear browser cache (Ctrl+Shift+Delete)
- ✅ Try accessing http://localhost:5500/app.html directly

### Quiz Generation Takes Too Long
- ✅ Normal generation time: 10-60 seconds
- ✅ Longer articles take more time
- ✅ Check backend terminal for progress logs
- ✅ Ensure stable internet connection for API calls

### Browser Caching Issues
- ✅ Hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)
- ✅ Clear cache: Ctrl+Shift+Delete
- ✅ Use incognito/private browsing mode
- ✅ Access http://localhost:5500/app.html (not index.html)

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

- **Frontend:** https://wiki-quiz-apps.onrender.com/
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

### Deploy Your Own Instance

Want to deploy your own version? Follow these steps:

#### 1. Deploy Backend

1. **Push code to GitHub**
2. **Create a new Web Service** on [Render](https://render.com)
3. **Connect your GitHub repository**
4. **Configure settings:**
   - Build Command: `pip install -r backend/requirements.txt`
   - Start Command: `uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT`
5. **Add environment variables:**
   - `POSTGRES_URL` - Your Neon connection string
   - `GEMINI_API_KEY` - Your Google Gemini API key
   - `USE_MOCK_LLM` - Set to `false` for production
6. **Deploy** and copy your backend URL

#### 2. Deploy Frontend

1. **Update API URL** in `frontend/index.html`:
   ```javascript
   const API_URL = "https://your-backend-url.onrender.com";
   ```
2. **Commit and push** to GitHub
3. **Create a new Static Site** on Render
4. **Configure settings:**
   - Root Directory: `frontend`
   - Publish Directory: `.`
5. **Deploy** and access your live app!

For detailed deployment instructions, see [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md).

## 🔐 Security Notes

- ⚠️ **Never commit `.env` file** to version control
- ⚠️ **Keep your Gemini API key private**
- ⚠️ **Use environment variables** for sensitive data
- ⚠️ **The Neon connection string contains your password** - keep it secure
- ✅ Add `.env` to `.gitignore`

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

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Support

For issues or questions:
- Open an issue on GitHub
- Check the Troubleshooting section above
- Review the API documentation at http://127.0.0.1:8000/docs

## 🙏 Acknowledgments

- **Wikipedia** - For providing free, open knowledge
- **Google Gemini AI** - For powerful language model capabilities
- **Neon** - For serverless PostgreSQL hosting
- **FastAPI** - For the excellent Python web framework
- **LangChain** - For LLM integration tools

---

**Built with ❤️ using FastAPI, Neon PostgreSQL, and Google Gemini AI**

🌟 **Star this repo if you found it helpful!**

---

## 📸 Screenshots

### Main Interface
![Main Interface](screenshots/main-interface.png)

### Quiz View Mode
![Quiz View Mode](screenshots/quiz-view.png)

### Interactive Quiz Mode
![Interactive Mode](screenshots/quiz-interactive.png)

### Quiz History
![Quiz History](screenshots/history.png)

---

**Version 2.0** - Enhanced with Interactive Quiz Mode, Difficulty Badges, Key Entities, and Premium UI Design

