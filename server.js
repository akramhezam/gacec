const express = require('express');
const fs = require('fs').promises;
const path = require('path');
const multer = require('multer');
const cors = require('cors');

const app = express();
const PORT = 3000;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static(__dirname)); // Serve static files

// Configure multer for image uploads
const storage = multer.diskStorage({
    destination: async (req, file, cb) => {
        const uploadDir = path.join(__dirname, 'images', 'uploads');
        try {
            await fs.mkdir(uploadDir, { recursive: true });
            cb(null, uploadDir);
        } catch (error) {
            cb(error, null);
        }
    },
    filename: (req, file, cb) => {
        const uniqueSuffix = Date.now() + '-' + Math.round(Math.random() * 1E9);
        cb(null, uniqueSuffix + path.extname(file.originalname));
    }
});

const upload = multer({
    storage: storage,
    limits: { fileSize: 5 * 1024 * 1024 }, // 5MB limit
    fileFilter: (req, file, cb) => {
        const allowedTypes = /jpeg|jpg|png|gif|webp/;
        const extname = allowedTypes.test(path.extname(file.originalname).toLowerCase());
        const mimetype = allowedTypes.test(file.mimetype);
        if (mimetype && extname) {
            return cb(null, true);
        } else {
            cb(new Error('Only image files are allowed!'));
        }
    }
});

// Helper function to read JSON file
async function readJsonFile(filename) {
    try {
        const filePath = path.join(__dirname, 'data', filename);
        const data = await fs.readFile(filePath, 'utf8');
        return JSON.parse(data);
    } catch (error) {
        console.error(`Error reading ${filename}:`, error);
        throw error;
    }
}

// Helper function to write JSON file
async function writeJsonFile(filename, data) {
    try {
        const filePath = path.join(__dirname, 'data', filename);
        await fs.writeFile(filePath, JSON.stringify(data, null, 2), 'utf8');
        return { success: true, message: `${filename} saved successfully` };
    } catch (error) {
        console.error(`Error writing ${filename}:`, error);
        throw error;
    }
}

// API Routes

// Get all data
app.get('/api/data/:type', async (req, res) => {
    try {
        const { type } = req.params;
        const validTypes = ['about', 'services', 'projects', 'testimonials', 'contact'];

        if (!validTypes.includes(type)) {
            return res.status(400).json({ error: 'Invalid data type' });
        }

        const data = await readJsonFile(`${type}.json`);
        res.json(data);
    } catch (error) {
        res.status(500).json({ error: 'Error loading data', details: error.message });
    }
});

// Save data
app.post('/api/data/:type', async (req, res) => {
    try {
        const { type } = req.params;
        const validTypes = ['about', 'services', 'projects', 'testimonials', 'contact'];

        if (!validTypes.includes(type)) {
            return res.status(400).json({ error: 'Invalid data type' });
        }

        const result = await writeJsonFile(`${type}.json`, req.body);
        res.json(result);
    } catch (error) {
        res.status(500).json({ error: 'Error saving data', details: error.message });
    }
});

// Upload image
app.post('/api/upload', upload.single('image'), (req, res) => {
    try {
        if (!req.file) {
            return res.status(400).json({ error: 'No file uploaded' });
        }

        const imageUrl = `/images/uploads/${req.file.filename}`;
        res.json({
            success: true,
            message: 'Image uploaded successfully',
            url: imageUrl,
            filename: req.file.filename
        });
    } catch (error) {
        res.status(500).json({ error: 'Error uploading image', details: error.message });
    }
});

// Delete image
app.delete('/api/upload/:filename', async (req, res) => {
    try {
        const { filename } = req.params;
        const filePath = path.join(__dirname, 'images', 'uploads', filename);

        await fs.unlink(filePath);
        res.json({ success: true, message: 'Image deleted successfully' });
    } catch (error) {
        res.status(500).json({ error: 'Error deleting image', details: error.message });
    }
});

// Get all uploaded images
app.get('/api/images', async (req, res) => {
    try {
        const uploadDir = path.join(__dirname, 'images', 'uploads');
        await fs.mkdir(uploadDir, { recursive: true });

        const files = await fs.readdir(uploadDir);
        const images = files
            .filter(file => /\.(jpg|jpeg|png|gif|webp)$/i.test(file))
            .map(file => ({
                filename: file,
                url: `/images/uploads/${file}`
            }));

        res.json(images);
    } catch (error) {
        res.status(500).json({ error: 'Error listing images', details: error.message });
    }
});

// Start server
app.listen(PORT, () => {
    console.log(`
╔════════════════════════════════════════════════════════╗
║                                                        ║
║       GACECCon Server Running                          ║
║                                                        ║
║   Website:     http://localhost:${PORT}/index.html       ║
║                                                        ║
║   API Endpoints:                                       ║
║   - GET  /api/data/:type                               ║
║   - POST /api/data/:type                               ║
║   - POST /api/upload                                   ║
║   - GET  /api/images                                   ║
║                                                        ║
╚════════════════════════════════════════════════════════╝
    `);
});

// Graceful shutdown
process.on('SIGINT', () => {
    console.log('\nShutting down gracefully...');
    process.exit(0);
});
