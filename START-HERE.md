# 🚀 GACECCon Website - Quick Start Guide

## ✅ Your Website is NOW RUNNING!

**Main Website**: http://localhost:5000/index.html

---

## 📋 What's Running

✅ **Flask Backend Server** (Python) - Port 5000
✅ **REST API** for data management
✅ **Image Upload** functionality
✅ **Static File Server** for website

---

## 🎯 Quick Actions

### View the Website
```
Open your browser: http://localhost:5000/index.html
```

### Stop the Server
```bash
# Press Ctrl+C in the terminal
# Or kill the process:
pkill -f "python3 app.py"
```

### Start Again Later
```bash
cd /home/akram/Desktop/gcc2
./start.sh

# Or manually:
python3 app.py
```

---

## 🎨 What You Can Do

### 1️⃣ Browse the Website
- **Home**: http://localhost:5000/index.html
- **About**: http://localhost:5000/about.html
- **Services**: http://localhost:5000/services.html
- **Projects**: http://localhost:5000/projects.html
- **Contact**: http://localhost:5000/contact.html

### 2️⃣ Manage Content
- Edit JSON files in the `data/` directory to update content
- Upload images to the `images/uploads/` directory
- Modify HTML files to customize pages

---

## 📁 Project Structure

```
gcc2/
├── app.py                  ← Python Flask backend (RUNNING)
├── start.sh                ← Startup script
├── requirements.txt        ← Python dependencies
│
├── index.html              ← Main website homepage
├── about.html              ← About page
├── services.html           ← Services page
├── projects.html           ← Projects page
├── contact.html            ← Contact page
│
├── script.js               ← Website JavaScript
├── styles.css              ← Website styles
│
├── data/                   ← JSON data files
│   ├── about.json
│   ├── services.json
│   ├── projects.json
│   ├── testimonials.json
│   └── contact.json
│
└── images/
    └── uploads/            ← Uploaded images go here
```

---

## 🔄 Workflow Example

### Scenario: Add a New Project

1. **Edit Projects Data**
   ```
   Edit data/projects.json
   ```

2. **Add Project Details**
   ```json
   {
     "id": 1,
     "title": "New Office Building",
     "category": "Buildings",
     "description": "Description here"
   }
   ```

3. **Upload Images**
   - Add images to `images/uploads/` directory
   - Reference them in the JSON file

4. **Save and Refresh**
   - Save the JSON file
   - Refresh: http://localhost:5000/projects.html
   - New project appears immediately!

---

## 🎯 API Endpoints (For Developers)

The backend provides these REST APIs:

### Get Data
```bash
GET http://localhost:5000/api/data/about
GET http://localhost:5000/api/data/services
GET http://localhost:5000/api/data/projects
GET http://localhost:5000/api/data/testimonials
```

### Save Data
```bash
POST http://localhost:5000/api/data/about
POST http://localhost:5000/api/data/services
POST http://localhost:5000/api/data/projects
POST http://localhost:5000/api/data/testimonials

Content-Type: application/json
Body: { ... JSON data ... }
```

### Upload Image
```bash
POST http://localhost:5000/api/upload
Content-Type: multipart/form-data
Field: image (file)
```

### List Images
```bash
GET http://localhost:5000/api/images
```

---

## ⚙️ Server Commands

### Check if Server is Running
```bash
curl http://localhost:5000
```

### View Server Logs
```bash
# Server logs appear in the terminal where you ran app.py
```

### Test API
```bash
# Get services data
curl http://localhost:5000/api/data/services

# Get projects data
curl http://localhost:5000/api/data/projects
```

---

## 🔒 Security Notes

### Current Setup (Development)
⚠️ No HTTPS (localhost only)
⚠️ No user authentication
⚠️ Debug mode enabled

### Before Production
- [ ] Disable Flask debug mode
- [ ] Add proper authentication (OAuth, JWT)
- [ ] Enable HTTPS
- [ ] Add rate limiting
- [ ] Set up proper CORS restrictions
- [ ] Use environment variables for secrets

---

## ❓ Troubleshooting

### Server Won't Start
```bash
# Check if port 5000 is in use
lsof -i :5000

# Kill existing process
pkill -f "python3 app.py"

# Try starting again
python3 app.py
```

### Flask Not Installed
```bash
pip3 install flask flask-cors --user
```

### Can't Access Website
```bash
# Make sure server is running
curl http://localhost:5000

# Check firewall settings
# Try: http://127.0.0.1:5000
```

### Images Not Uploading
- Check `images/uploads/` directory exists
- Check file size (max 5MB)
- Check file type (JPG, PNG, GIF, WebP only)
- Check server logs for errors

### Changes Not Saving
- Check browser console (F12)
- Verify server is running
- Check file permissions on `data/` directory
- Check server logs for errors

---

## 📚 Documentation Files

1. **[START-HERE.md](START-HERE.md)** - This file (quick start)
2. **[HOW-TO-USE.md](HOW-TO-USE.md)** - Step-by-step user guide
3. **[README-ADMIN.md](README-ADMIN.md)** - Complete admin documentation
4. **[SETUP.md](SETUP.md)** - Installation & setup guide
5. **[IMPLEMENTATION-SUMMARY.md](IMPLEMENTATION-SUMMARY.md)** - Technical overview

---

## 🎉 You're All Set!

Your GACECCon website is now running!

### Next Steps:
1. ✅ Browse the website at http://localhost:5000
2. ✅ Edit JSON files in `data/` to update content
3. ✅ Upload images to `images/uploads/`
4. ✅ See your changes on the website!

---

## 💡 Tips

- **Keep Terminal Open**: Server runs in the terminal
- **Check Logs**: Server shows all API requests
- **Backup Data**: Keep copies of your JSON files
- **Test Changes**: Refresh website after editing files

---

## 🆘 Need Help?

1. Check the documentation files listed above
2. Check browser console (F12 → Console)
3. Check server terminal for errors
4. Review error messages carefully

---

**Happy content managing! 🚀**

Your website is live and ready to use!
