# GACECCon Admin Panel Guide

> **⚠️ DEPRECATED**: The admin.html file has been removed from the repository for security reasons. This documentation is kept for reference purposes only.
> 
> To manage content:
> - Edit JSON files in the `data/` directory directly
> - Upload images to `images/uploads/` directory
> - Modify HTML files as needed

---

## Historical Documentation (Admin Panel - REMOVED)

Welcome to the GACECCon Content Management System! This admin panel allows you to manage all website content including services, projects, team members, testimonials, and more.

## 🚀 Getting Started

### Prerequisites
- Node.js (version 14 or higher)
- npm (comes with Node.js)

### Installation

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Start the server:**
   ```bash
   npm start
   ```

3. **Access the admin panel:**
   - Open your browser and go to: `http://localhost:3000/admin.html`
   - Default password: `gaceccon2026`

4. **View the website:**
   - Main website: `http://localhost:3000/index.html`

## 📋 Features

### Content Management
- **About Us**: Edit company bio, mission, vision, values, and team members
- **Services**: Add, edit, and delete services with descriptions and images
- **Projects**: Manage project portfolio with images, details, and status
- **Testimonials**: Collect and display client testimonials

### Image Management
- **Upload Images**: Upload images up to 5MB (JPG, PNG, GIF, WebP)
- **Image Library**: Browse and select from uploaded images
- **Direct Integration**: Browse images button in all image input fields

### Data Persistence
- All changes are saved to JSON files in the `data/` folder
- Changes persist after page refresh
- Data is immediately reflected on the website

## 🎨 How to Use

### Adding New Content

1. **Navigate to the section** you want to edit using the sidebar
2. **Click the "Add" button** (e.g., "Add Service", "Add Project")
3. **Fill in the form** with all required information
4. **For images:**
   - Click "Browse Images" button
   - Either upload a new image or select from existing ones
   - The image URL will be automatically filled
5. **Click "Save Changes"** to save your content

### Editing Existing Content

1. Find the item you want to edit
2. Click the **edit icon** (pencil) on the item card
3. Modify the information
4. Click "Save Changes"

### Deleting Content

1. Find the item you want to delete
2. Click the **delete icon** (trash can)
3. Confirm the deletion

### Uploading Images

**Method 1: Through Image Library Modal**
1. Click any "Browse Images" button
2. Click "Select Image" to choose a file from your computer
3. Click "Upload" to upload the image
4. Once uploaded, click "Select" on the image to use it

**Method 2: Direct URL**
You can also paste image URLs directly if you have images hosted elsewhere (e.g., Unsplash, your CDN).

## 📁 File Structure

```
gcc2/
├── admin.html              # Admin panel interface
├── index.html              # Main website
├── server.js               # Backend API server
├── package.json            # Node.js dependencies
├── data/                   # JSON data files
│   ├── about.json
│   ├── services.json
│   ├── projects.json
│   ├── testimonials.json
│   └── contact.json
└── images/
    └── uploads/            # Uploaded images stored here
```

## 🔒 Security Notes

### For Development
- Default password is hardcoded for testing
- Runs on localhost only

### For Production
**IMPORTANT**: Before deploying to production:

1. **Change the admin password** in `admin.html` (line 354):
   ```javascript
   const ADMIN_PASSWORD = 'your-secure-password-here';
   ```

2. **Add proper authentication**:
   - Consider using bcrypt for password hashing
   - Implement JWT or session-based authentication
   - Add user management system

3. **Secure the API**:
   - Add authentication middleware to all API routes
   - Implement rate limiting
   - Add CORS restrictions
   - Use HTTPS only

4. **Environment Variables**:
   - Move sensitive config to `.env` file
   - Use `dotenv` package
   - Never commit `.env` to version control

## 🌐 Production Deployment

For a production-ready CMS, consider integrating:

1. **[Decap CMS](https://decapcms.org/)** (formerly Netlify CMS)
   - Git-based content management
   - Works great with static site generators
   - Free and open source

2. **[Strapi](https://strapi.io/)**
   - Headless CMS with admin UI
   - REST & GraphQL APIs
   - User & role management

3. **[Sanity](https://www.sanity.io/)**
   - Real-time collaborative CMS
   - Flexible content modeling
   - Great developer experience

## 🛠️ Troubleshooting

### Server won't start
```bash
# Check if port 3000 is already in use
lsof -i :3000

# Kill the process using port 3000
kill -9 <PID>

# Or use a different port
PORT=3001 npm start
```

### Images not uploading
- Check file size (max 5MB)
- Verify file format (JPG, PNG, GIF, WebP only)
- Ensure `images/uploads/` directory exists and is writable
- Check browser console for errors

### Changes not saving
- Check browser console for API errors
- Verify server is running
- Check file permissions on `data/` directory
- Ensure you're connected to the server

### Password not working
- Default password: `gaceccon2026`
- Password is case-sensitive
- Clear browser cache and try again
- Check `admin.html` line 354 for current password

## 📞 Support

For issues or questions:
1. Check the browser console for errors (F12 → Console)
2. Check the server terminal for backend errors
3. Review this README for common solutions

## 🎯 Quick Tips

1. **Save Often**: Click save after making changes to avoid losing work
2. **Preview**: Open the website in a new tab to see changes immediately
3. **Optimize Images**: Compress images before uploading for better performance
4. **Backup**: Export all data regularly using "Export All Data" button
5. **Test**: Always test changes on the website after saving

## 📝 License

Copyright © 2024 GACECCon. All rights reserved.

---

**Made with ❤️ for GACECCon**
