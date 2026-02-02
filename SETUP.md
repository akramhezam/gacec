# Quick Setup Guide

> **⚠️ NOTE**: The admin panel has been removed for security reasons. This setup guide remains valid for running the website.

## Step 1: Install Dependencies

You need Node.js installed. If you don't have it, download from [nodejs.org](https://nodejs.org/)

Then run:
```bash
npm install
```

This will install:
- `express` - Web server framework
- `cors` - Cross-origin resource sharing
- `multer` - File upload handling

## Step 2: Start the Server

```bash
npm start
```

You should see:
```
╔════════════════════════════════════════════════════════╗
║                                                        ║
║       GACECCon Admin Server Running                    ║
║                                                        ║
║   Admin Panel: http://localhost:3000/admin.html       ║
║   Website:     http://localhost:3000/index.html       ║
║                                                        ║
╚════════════════════════════════════════════════════════╝
```

## Step 3: Access Admin Panel

1. Open browser: `http://localhost:3000/admin.html`
2. Enter password: `gaceccon2026`
3. Start managing content!

## Troubleshooting

### If npm install fails with old Node.js version:

**Option 1: Update Node.js**
```bash
# Download and install latest LTS from nodejs.org
# Then run npm install again
```

**Option 2: Manual installation**
If npm doesn't work, you can try:
```bash
# Update npm first
curl -L https://www.npmjs.com/install.sh | sh

# Then install packages
npm install express@4.18.2 cors@2.8.5 multer@1.4.5-lts.1
```

**Option 3: Use yarn instead**
```bash
# Install yarn
npm install -g yarn

# Install dependencies
yarn install

# Start server
yarn start
```

### Port already in use
```bash
# Find what's using port 3000
lsof -i :3000

# Kill it
kill -9 <PID>

# Or change the port in server.js (line 6)
const PORT = 3001; // Change to any available port
```

## What the Admin Panel Does

### ✅ Add New Content
- Services
- Projects
- Team members
- Testimonials
- Core values

### ✏️ Edit Existing Content
- Click edit icon on any item
- Modify fields
- Save changes

### 🗑️ Delete Content
- Click delete icon
- Confirm deletion
- Content removed permanently

### 🖼️ Upload & Manage Images
- Upload images (max 5MB)
- Browse uploaded images
- Select images for content

### 💾 Data Persistence
- All changes saved to JSON files in `data/` folder
- Changes persist after refresh
- Immediately reflected on website

## File Structure

```
gcc2/
├── admin.html           ← Admin interface
├── index.html           ← Main website
├── server.js            ← Backend API
├── package.json         ← Dependencies
├── data/                ← JSON data files (auto-saved)
│   ├── about.json
│   ├── services.json
│   ├── projects.json
│   └── testimonials.json
└── images/
    └── uploads/         ← Uploaded images stored here
```

## Quick Start Commands

```bash
# Install dependencies
npm install

# Start server
npm start

# Start with auto-reload (for development)
npm run dev

# Stop server
Ctrl + C
```

## Default Login

- **URL**: http://localhost:3000/admin.html
- **Password**: `gaceccon2026`

⚠️ **Change this password before production!** (see README-ADMIN.md)

## Next Steps

1. ✅ Read [README-ADMIN.md](README-ADMIN.md) for full documentation
2. ✅ Start adding/editing content
3. ✅ Upload your own images
4. ✅ Customize the password
5. ✅ Deploy to production

Happy content managing! 🚀
