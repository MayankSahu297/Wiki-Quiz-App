# 🚀 Complete Deployment Guide - Wiki Quiz App

Step-by-step guide to upload your project to GitHub and deploy it on Render.

---

## 📦 PART 1: Upload to GitHub

### Step 1: Create `.gitignore` File

Create a file named `.gitignore` in your project root directory:

**File: `.gitignore`**
```gitignore
# Environment variables - NEVER commit this!
.env

# Python cache
__pycache__/
*.py[cod]
*$py.class
*.pyc
.Python

# Virtual environments
env/
venv/
.venv/
ENV/
env.bak/
venv.bak/

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# OS files
.DS_Store
Thumbs.db
.DS_Store?
._*
.Spotlight-V100
.Trashes

# Database
*.db
*.sqlite
*.sqlite3

# Logs
*.log
logs/

# Build files
build/
dist/
*.egg-info/

# Testing
.pytest_cache/
.coverage
htmlcov/
.tox/

# Temporary files
*.tmp
temp/
tmp/
```

### Step 2: Initialize Git Repository

Open terminal in your project folder (`Wiki Quiz App`) and run:

```bash
git init
```

**Expected output:**
```
Initialized empty Git repository in C:/Users/VICTUS/Documents/Wiki Quiz App/.git/
```

### Step 3: Add All Files to Git

```bash
git add .
```

This stages all files except those in `.gitignore`.

### Step 4: Create Your First Commit

```bash
git commit -m "Initial commit: Wiki Quiz App v2.0 with interactive features"
```

**Expected output:**
```
[main (root-commit) abc1234] Initial commit: Wiki Quiz App v2.0 with interactive features
 XX files changed, XXXX insertions(+)
 create mode 100644 README.md
 create mode 100644 backend/app/main.py
 ...
```

### Step 5: Create GitHub Repository

1. **Go to GitHub:**
   - Visit [github.com](https://github.com)
   - Log in to your account

2. **Create New Repository:**
   - Click the **"+"** icon (top-right corner)
   - Select **"New repository"**

3. **Fill Repository Details:**
   - **Repository name:** `wiki-quiz-app`
   - **Description:** `AI-powered Wikipedia quiz generator with interactive learning features`
   - **Visibility:** Choose **Public** (recommended) or **Private**
   - **DO NOT** check "Initialize this repository with:"
     - ❌ Don't add README
     - ❌ Don't add .gitignore
     - ❌ Don't choose a license
   - Click **"Create repository"**

### Step 6: Connect Local Repository to GitHub

GitHub will show you commands. Copy and run them:

```bash
git remote add origin https://github.com/YOUR_USERNAME/wiki-quiz-app.git
git branch -M main
git push -u origin main
```

**⚠️ IMPORTANT:** Replace `YOUR_USERNAME` with your actual GitHub username!

**Example:**
```bash
git remote add origin https://github.com/johndoe/wiki-quiz-app.git
git branch -M main
git push -u origin main
```

**If prompted for credentials:**
- Username: Your GitHub username
- Password: Use a **Personal Access Token** (not your password)
  - Get token at: [github.com/settings/tokens](https://github.com/settings/tokens)

### Step 7: Verify Upload

1. Refresh your GitHub repository page
2. You should see all your files
3. **CRITICAL CHECK:** Verify `.env` is **NOT** visible (should be ignored)
4. Check that `README.md` displays correctly

✅ **Success!** Your code is now on GitHub!

---

## 🌐 PART 2: Deploy Backend on Render

### Step 1: Prepare for Deployment

First, ensure your backend can run on Render by checking `backend/requirements.txt`:

```bash
# View requirements
cat backend/requirements.txt
```

Should contain:
```
fastapi
uvicorn[standard]
sqlalchemy
psycopg2-binary
pydantic
beautifulsoup4
httpx
langchain
langchain-community
langchain-google-genai
python-dotenv
```

### Step 2: Create Render Account

1. Go to [render.com](https://render.com)
2. Click **"Get Started"** or **"Sign Up"**
3. **Sign up with GitHub** (recommended - easier integration)
4. Click **"Authorize Render"** to connect your GitHub account

### Step 3: Create New Web Service

1. In Render Dashboard, click **"New +"** (top-right)
2. Select **"Web Service"**
3. You'll see "Create a new Web Service"

### Step 4: Connect Your Repository

1. Under "Connect a repository":
   - If you see your `wiki-quiz-app` repository, click **"Connect"**
   - If not, click **"Configure account"** → Select repositories → Choose `wiki-quiz-app` → Save

2. Click **"Connect"** next to your repository

### Step 5: Configure Web Service Settings

Fill in these settings carefully:

**Basic Information:**
- **Name:** `wiki-quiz-backend` (or any name you prefer)
  - This will be part of your URL: `wiki-quiz-backend.onrender.com`
- **Region:** Choose closest to you
  - 🇺🇸 Oregon (US West)
  - 🇺🇸 Ohio (US East)
  - 🇪🇺 Frankfurt (Europe)
  - 🇸🇬 Singapore (Asia)
- **Branch:** `main`
- **Root Directory:** Leave **blank**

**Build & Deploy:**
- **Runtime:** Select **"Python 3"**
- **Build Command:**
  ```bash
  pip install -r backend/requirements.txt
  ```
- **Start Command:**
  ```bash
  uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT
  ```

**Instance Type:**
- **Free** (for testing - spins down after 15 min inactivity)
- **Starter** ($7/month - always on, recommended for production)

### Step 6: Add Environment Variables

Scroll down to **"Environment Variables"** section.

Click **"Add Environment Variable"** and add these **3 variables**:

**1. POSTGRES_URL**
- **Key:** `POSTGRES_URL`
- **Value:** Your Neon connection string
- Example: `postgresql://neondb_owner:npg_xxx@ep-xxx.region.aws.neon.tech/neondb?sslmode=require`
- Get this from your `.env` file

**2. GEMINI_API_KEY**
- **Key:** `GEMINI_API_KEY`
- **Value:** Your Google Gemini API key
- Example: `AIzaSyD0xuBop4qLIR7_kSuCEgrPQfvOghqT6eU`
- Get this from your `.env` file

**3. USE_MOCK_LLM**
- **Key:** `USE_MOCK_LLM`
- **Value:** `false` (use real AI) or `true` (use demo quizzes)

### Step 7: Deploy Backend

1. Click **"Create Web Service"** at the bottom
2. Render will start deploying (takes 5-10 minutes)
3. Watch the deployment logs:
   - You'll see: Installing dependencies...
   - Then: Starting application...
   - Finally: **"Your service is live 🎉"**

### Step 8: Get Your Backend URL

Once deployed:
1. You'll see your service URL at the top
2. Example: `https://wiki-quiz-backend.onrender.com`
3. **COPY THIS URL** - you'll need it for frontend!

### Step 9: Test Your Backend

Visit your backend URL with `/docs`:
```
https://wiki-quiz-backend.onrender.com/docs
```

You should see the **Swagger API documentation**!

✅ **Backend is live!**

---

## 🎨 PART 3: Deploy Frontend on Render

### Step 1: Update Frontend API URL

**CRITICAL:** Update the API URL in your frontend code.

1. Open `frontend/app.html`
2. Find line ~649:
   ```javascript
   const API_URL = "http://127.0.0.1:8000";
   ```
3. Replace with your Render backend URL:
   ```javascript
   const API_URL = "https://wiki-quiz-backend.onrender.com";
   ```
   ⚠️ Replace with YOUR actual backend URL!

4. Save the file

### Step 2: Commit and Push Changes

```bash
git add frontend/app.html
git commit -m "Update API URL for production deployment"
git push
```

### Step 3: Create Static Site on Render

1. In Render Dashboard, click **"New +"**
2. Select **"Static Site"**
3. Connect your `wiki-quiz-app` repository
4. Click **"Connect"**

### Step 4: Configure Static Site

**Basic Settings:**
- **Name:** `wiki-quiz-frontend`
- **Branch:** `main`
- **Root Directory:** `frontend`
- **Build Command:** Leave **blank** (no build needed)
- **Publish Directory:** `.` (just a dot)

### Step 5: Deploy Frontend

1. Click **"Create Static Site"**
2. Wait for deployment (2-3 minutes)
3. You'll get a URL like: `https://wiki-quiz-frontend.onrender.com`

### Step 6: Test Your Live App! 🎉

1. Visit your frontend URL
2. Try generating a quiz from a Wikipedia article
3. Test all features:
   - ✅ Quiz generation
   - ✅ Interactive mode
   - ✅ View mode
   - ✅ History tab
   - ✅ Difficulty badges
   - ✅ Key entities display

---

## 🔧 PART 4: Troubleshooting

### Issue 1: CORS Error

**Symptom:** Browser console shows CORS error

**Solution:** Add CORS middleware to backend

1. Open `backend/app/main.py`
2. Add after imports:
   ```python
   from fastapi.middleware.cors import CORSMiddleware
   
   app = FastAPI()
   
   # Add CORS middleware
   app.add_middleware(
       CORSMiddleware,
       allow_origins=[
           "https://wiki-quiz-frontend.onrender.com",  # Your frontend URL
           "http://localhost:5500"  # For local testing
       ],
       allow_credentials=True,
       allow_methods=["*"],
       allow_headers=["*"],
   )
   ```

3. Commit and push:
   ```bash
   git add backend/app/main.py
   git commit -m "Add CORS configuration"
   git push
   ```

Render will auto-redeploy!

### Issue 2: Backend Not Starting

**Check logs in Render:**
1. Go to your backend service
2. Click "Logs" tab
3. Look for errors

**Common fixes:**
- Verify all environment variables are set
- Check `requirements.txt` has all dependencies
- Ensure start command is correct

### Issue 3: Database Connection Failed

**Solutions:**
- Verify `POSTGRES_URL` in Render matches your Neon connection string
- Check Neon database is active (not paused)
- Ensure connection string has `?sslmode=require` at the end

### Issue 4: Frontend Shows Old Code

**Solutions:**
- Hard refresh: Ctrl+Shift+R
- Clear Render build cache:
  - Go to service settings
  - Click "Manual Deploy" → "Clear build cache & deploy"

### Issue 5: "Module not found" Error

**Solution:**
```bash
# Regenerate requirements.txt
pip freeze > backend/requirements.txt
git add backend/requirements.txt
git commit -m "Update requirements"
git push
```

---

## 🔄 Updating Your Deployed App

Whenever you make changes:

```bash
# 1. Make your changes to code

# 2. Test locally first
# Start backend: uvicorn backend.app.main:app --reload
# Start frontend: python -m http.server 5500 --directory frontend

# 3. Commit changes
git add .
git commit -m "Description of what you changed"

# 4. Push to GitHub
git push

# 5. Render automatically redeploys! 🚀
# Watch the deployment in Render dashboard
```

---

## 📊 Deployment Checklist

### ✅ Before Deployment:
- [ ] Created `.gitignore` file
- [ ] Verified `.env` is NOT in Git
- [ ] Tested app locally
- [ ] All features working
- [ ] Have Neon database URL
- [ ] Have Gemini API key

### ✅ GitHub Upload:
- [ ] Initialized Git repository
- [ ] Created first commit
- [ ] Created GitHub repository
- [ ] Pushed code to GitHub
- [ ] Verified `.env` is not visible on GitHub

### ✅ Backend Deployment:
- [ ] Created Render account
- [ ] Connected GitHub repository
- [ ] Configured build command
- [ ] Configured start command
- [ ] Added all 3 environment variables
- [ ] Deployed successfully
- [ ] Tested `/docs` endpoint
- [ ] Copied backend URL

### ✅ Frontend Deployment:
- [ ] Updated API URL in `app.html`
- [ ] Committed and pushed changes
- [ ] Created static site on Render
- [ ] Configured publish directory
- [ ] Deployed successfully
- [ ] Tested live app

### ✅ Post-Deployment:
- [ ] All features work on live site
- [ ] No CORS errors
- [ ] Quiz generation works
- [ ] History loads correctly
- [ ] Mobile responsive
- [ ] Shared with friends! 🎉

---

## 💰 Cost Summary

### Free Tier (Perfect for Portfolio):
- **GitHub:** Free (unlimited public repos)
- **Render Backend:** Free (750 hours/month, spins down after 15 min)
- **Render Frontend:** Free (always on)
- **Neon Database:** Free (0.5 GB, pauses after 5 days inactivity)
- **Gemini API:** Free (15 req/min, 1500 req/day)

**Total: $0/month** ✅

### Paid Tier (For Production):
- **Render Backend Starter:** $7/month (always on)
- **Render Frontend:** Free
- **Neon Pro:** $19/month (always active, more storage)
- **Gemini API:** Pay-as-you-go (very cheap)

**Total: ~$26/month**

---

## 🎯 Your URLs After Deployment

**Backend API:**
```
https://wiki-quiz-backend.onrender.com
```

**API Documentation:**
```
https://wiki-quiz-backend.onrender.com/docs
```

**Frontend App:**
```
https://wiki-quiz-frontend.onrender.com
```

**Share this link with everyone!** 🌟

---

## 📱 Next Steps After Deployment

1. **Test thoroughly** on different devices
2. **Share on social media** (LinkedIn, Twitter)
3. **Add to your portfolio** website
4. **Get feedback** from users
5. **Monitor usage** in Render dashboard
6. **Check API usage** in Google AI Studio
7. **Consider custom domain** (optional)

---

## 🆘 Need Help?

**Render Support:**
- [Render Documentation](https://render.com/docs)
- [Render Community](https://community.render.com)

**GitHub Help:**
- [GitHub Guides](https://guides.github.com)
- [Git Documentation](https://git-scm.com/doc)

**Project Issues:**
- Check `EVALUATION.md` for improvements
- Review `README.md` for features
- See `TROUBLESHOOTING.md` (if exists)

---

## 🎉 Congratulations!

Your Wiki Quiz App is now **LIVE ON THE INTERNET!** 🌍

You've successfully:
- ✅ Uploaded code to GitHub
- ✅ Deployed backend on Render
- ✅ Deployed frontend on Render
- ✅ Connected everything together
- ✅ Made your project accessible worldwide!

**This is a huge achievement!** Add this to your resume and portfolio! 🚀

---

**Built with ❤️ and deployed with 🚀**

**Good luck with your project!** ⭐
