#!/usr/bin/env python3
"""
GACECCon Admin Panel Backend - Python Flask Version
Simple alternative to Node.js Express server
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import os
from datetime import datetime
from werkzeug.utils import secure_filename

app = Flask(__name__, static_folder='.')
CORS(app)

# Configuration
UPLOAD_FOLDER = 'images/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

# Ensure upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Serve static files
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

# API Routes

@app.route('/api/data/<data_type>', methods=['GET'])
def get_data(data_type):
    """Load data from JSON file"""
    valid_types = ['about', 'services', 'projects', 'testimonials', 'contact']

    if data_type not in valid_types:
        return jsonify({'error': 'Invalid data type'}), 400

    try:
        file_path = os.path.join('data', f'{data_type}.json')
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': 'Error loading data', 'details': str(e)}), 500

@app.route('/api/data/<data_type>', methods=['POST'])
def save_data(data_type):
    """Save data to JSON file"""
    valid_types = ['about', 'services', 'projects', 'testimonials', 'contact']

    if data_type not in valid_types:
        return jsonify({'error': 'Invalid data type'}), 400

    try:
        data = request.get_json()
        file_path = os.path.join('data', f'{data_type}.json')

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        return jsonify({
            'success': True,
            'message': f'{data_type}.json saved successfully'
        })
    except Exception as e:
        return jsonify({'error': 'Error saving data', 'details': str(e)}), 500

@app.route('/api/upload', methods=['POST'])
def upload_image():
    """Upload image file"""
    if 'image' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['image']

    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if file and allowed_file(file.filename):
        # Generate unique filename
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = secure_filename(file.filename)
        name, ext = os.path.splitext(filename)
        unique_filename = f'{timestamp}_{name}{ext}'

        filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(filepath)

        return jsonify({
            'success': True,
            'message': 'Image uploaded successfully',
            'url': f'/images/uploads/{unique_filename}',
            'filename': unique_filename
        })

    return jsonify({'error': 'Invalid file type'}), 400

@app.route('/api/images', methods=['GET'])
def list_images():
    """List all uploaded images"""
    try:
        upload_dir = app.config['UPLOAD_FOLDER']
        files = os.listdir(upload_dir)

        images = [
            {
                'filename': f,
                'url': f'/images/uploads/{f}'
            }
            for f in files
            if allowed_file(f)
        ]

        # Sort by modification time (newest first)
        images.sort(key=lambda x: os.path.getmtime(
            os.path.join(upload_dir, x['filename'])
        ), reverse=True)

        return jsonify(images)
    except Exception as e:
        return jsonify({'error': 'Error listing images', 'details': str(e)}), 500

@app.route('/api/upload/<filename>', methods=['DELETE'])
def delete_image(filename):
    """Delete uploaded image"""
    try:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename))

        if os.path.exists(filepath):
            os.remove(filepath)
            return jsonify({
                'success': True,
                'message': 'Image deleted successfully'
            })
        else:
            return jsonify({'error': 'File not found'}), 404
    except Exception as e:
        return jsonify({'error': 'Error deleting image', 'details': str(e)}), 500

if __name__ == '__main__':
    print("""
╔════════════════════════════════════════════════════════╗
║                                                        ║
║       GACECCon Server Running (Python)                 ║
║                                                        ║
║   Website:     http://localhost:5000/index.html       ║
║                                                        ║
║   API Endpoints:                                       ║
║   - GET  /api/data/:type                               ║
║   - POST /api/data/:type                               ║
║   - POST /api/upload                                   ║
║   - GET  /api/images                                   ║
║                                                        ║
╚════════════════════════════════════════════════════════╝
    """)
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
