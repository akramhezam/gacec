# How to Use GACECCon - Simple Guide

> **⚠️ DEPRECATED**: The admin panel has been removed for security reasons. This guide is kept for reference.
> 
> To manage content:
> - Edit JSON files in `data/` directory
> - Upload images to `images/uploads/` directory
> - Modify HTML files as needed

## Historical Documentation (Admin Panel - REMOVED)

## 🎯 Quick Start (3 Steps)

### Step 1: Start the Server
```bash
npm install    # First time only
npm start      # Every time you want to use admin panel
```

You'll see:
```
GACECCon Admin Server Running
Admin Panel: http://localhost:3000/admin.html
```

### Step 2: Login
1. Open browser → `http://localhost:3000/admin.html`
2. Enter password: `gaceccon2026`
3. Click "Access Admin Panel"

### Step 3: Start Editing!
- Choose section from sidebar (About, Services, Projects, Testimonials)
- Click "Add" or "Edit" buttons
- Make changes
- Click "Save Changes"
- Done! ✅

## 📸 Adding Images (Super Easy!)

When you see an image field:

1. **Click "Browse Images" button**
2. Two options:
   - **Upload New**: Click "Select Image" → choose file → "Upload"
   - **Use Existing**: Scroll and click "Select" on any image
3. Image URL automatically fills in!
4. Save your content

## 🎨 Common Tasks

### Adding a New Service

```
1. Click "Services" in sidebar
2. Click "Add Service" button
3. Fill in:
   - ID (slug): e.g., "consulting"
   - Title: "Engineering Consulting"
   - Short Description
   - Full Description
   - Features (comma-separated)
   - Image: Click "Browse Images"
4. Click "Save Changes"
5. ✅ Done! Check website to see it
```

### Adding a New Project

```
1. Click "Projects" in sidebar
2. Click "Add Project" button
3. Fill in basic info:
   - ID, Title, Category, Status
   - Short & Full Description
   - Client, Location, Budget, Timeline
4. Add images:
   - Click "Browse Images"
   - Upload or select multiple images
   - URLs appear comma-separated
5. Add tasks and requirements (comma-separated)
6. Check "Featured" if this is a highlight project
7. Click "Save Changes"
8. ✅ Done! Check website
```

### Adding a Team Member

```
1. Click "About Us" in sidebar
2. Scroll to "Team Members"
3. Click "Add Team Member"
4. Fill in:
   - Name
   - Position
   - Bio
   - Image (click "Browse Images")
5. Click "Save Changes"
6. ✅ Done!
```

### Adding a Testimonial

```
1. Click "Testimonials" in sidebar
2. Click "Add Testimonial"
3. Fill in:
   - Name
   - Position & Company
   - Quote
   - Rating (1-5)
   - Image (click "Browse Images")
   - Related Project
4. Click "Save Changes"
5. ✅ Done!
```

### Editing Existing Content

```
1. Find the item you want to edit
2. Click the ✏️ pencil icon
3. Modify any fields
4. Click "Save Changes"
5. ✅ Updated!
```

### Deleting Content

```
1. Find the item to delete
2. Click the 🗑️ trash icon
3. Confirm deletion
4. ✅ Deleted!
```

## 🖼️ Image Management Tips

### Good Image Practices
✅ Compress images before upload (max 5MB)
✅ Use descriptive file names
✅ Use consistent sizes for similar content
✅ JPG for photos, PNG for graphics

### Where Images Are Used
- **Team Members**: Headshots (square recommended)
- **Services**: Service illustrations (landscape)
- **Projects**: Project photos (landscape, multiple OK)
- **Testimonials**: Client photos (square)

## 🎯 Workflow Diagram

```
┌─────────────────┐
│  Start Server   │
│   npm start     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Open Admin     │
│  admin.html     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Enter Password │
│  gaceccon2026   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Choose Section  │
│ (sidebar menu)  │
└────────┬────────┘
         │
    ┌────┴────┐
    ▼         ▼
┌───────┐ ┌───────┐
│  Add  │ │ Edit  │
│  New  │ │ Exist │
└───┬───┘ └───┬───┘
    │         │
    └────┬────┘
         ▼
┌─────────────────┐
│  Fill Form +    │
│  Upload Images  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Save Changes   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ ✅ Content Saved │
│ JSON files      │
│ updated!        │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Refresh        │
│  Website        │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ ✅ See Changes  │
│ Live!           │
└─────────────────┘
```

## 💾 Where Everything Is Saved

```
gcc2/
├── data/
│   ├── about.json        ← Company info, team, values
│   ├── services.json     ← All services
│   ├── projects.json     ← All projects
│   └── testimonials.json ← All testimonials
│
└── images/uploads/       ← All uploaded images
```

**Important**: When you click "Save", the JSON file is automatically updated!

## ⚠️ Common Questions

### Q: Do I need to refresh the admin panel after saving?
**A:** No! Changes appear immediately in the admin panel.

### Q: When will changes appear on the website?
**A:** Immediately! Just refresh the website page.

### Q: What if I make a mistake?
**A:**
- Click "Edit" to fix it
- Or click "Delete" to remove it
- Or use "Export All Data" to backup first

### Q: Can I upload videos?
**A:** Not yet. Images only (JPG, PNG, GIF, WebP).

### Q: How many images can I upload?
**A:** Unlimited! But keep each under 5MB.

### Q: Can multiple people use the admin at once?
**A:** Yes, but be careful not to overwrite each other's changes.

### Q: What happens if the server stops?
**A:**
- Admin panel won't work
- Website still works (uses saved JSON files)
- Restart server with `npm start`

## 🎯 Best Practices

### Before Making Changes
1. ✅ Test on one item first
2. ✅ Keep original content as reference
3. ✅ Use "Export All Data" for backup

### When Adding Content
1. ✅ Write clear, concise descriptions
2. ✅ Use high-quality images
3. ✅ Check spelling and grammar
4. ✅ Fill all required fields

### After Saving
1. ✅ Check website to verify changes
2. ✅ Test on mobile if possible
3. ✅ Share preview with team

## 🆘 Troubleshooting

### Admin panel won't load
```
Problem: Can't access http://localhost:3000/admin.html
Solution:
1. Check if server is running
2. Look for "Server Running" message in terminal
3. If not, run: npm start
```

### Can't login
```
Problem: Password doesn't work
Solution:
1. Try: gaceccon2026 (case-sensitive)
2. Check for extra spaces
3. Clear browser cache
```

### Image won't upload
```
Problem: Upload fails
Solution:
1. Check file size (must be under 5MB)
2. Check file type (JPG, PNG, GIF, WebP only)
3. Try compressing image at tinypng.com
4. Check browser console for errors (F12)
```

### Changes not saving
```
Problem: Click save but nothing happens
Solution:
1. Check browser console (F12 → Console)
2. Look for red error messages
3. Check if server is running
4. Try refreshing admin panel
```

### Server won't start
```
Problem: npm start fails
Solution:
1. Run: npm install (again)
2. Check if port 3000 is available
3. Try: PORT=3001 npm start
4. See SETUP.md for more help
```

## 📱 Mobile Usage

The admin panel works on tablets and phones, but:
- ✅ Easier on desktop/laptop
- ✅ Use landscape mode on tablet
- ⚠️ Image upload may be slower on mobile

## 🎓 Learning Resources

### First Time Using?
1. Start with "About Us" section
2. Edit your company bio
3. Add one team member
4. Try uploading an image
5. Move to Services and Projects

### Want to Learn More?
- Read [README-ADMIN.md](README-ADMIN.md) - Full documentation
- Read [SETUP.md](SETUP.md) - Technical setup
- Read [IMPLEMENTATION-SUMMARY.md](IMPLEMENTATION-SUMMARY.md) - How it works

## ✅ Checklist for Success

- [ ] Server installed (`npm install`)
- [ ] Server running (`npm start`)
- [ ] Can login to admin panel
- [ ] Tried adding new content
- [ ] Tried uploading an image
- [ ] Verified changes on website
- [ ] Exported data backup
- [ ] Changed password (for production)

## 🎉 You're Ready!

You now have everything you need to manage your GACECCon website content. Don't be afraid to experiment - you can always delete or edit anything you add!

**Need Help?**
1. Check this guide
2. Check [README-ADMIN.md](README-ADMIN.md)
3. Check browser console (F12)
4. Check server terminal for errors

**Happy content managing! 🚀**

---

**Pro Tip**: Bookmark `http://localhost:3000/admin.html` for quick access!
