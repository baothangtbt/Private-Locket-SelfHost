import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

# --- CẤU HÌNH SERVER ---
app = Flask(__name__)
app.config['SECRET_KEY'] = 'khoa-bi-mat-cua-tui-123' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///locket.db'
app.config['UPLOAD_FOLDER'] = 'uploads'

# Khởi tạo các công cụ
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Tạo thư mục upload nếu chưa có
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# --- CẤU TRÚC DỮ LIỆU (DATABASE) ---
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    comments = db.relationship('Comment', backref='author', lazy=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(500)) # Caption bài viết
    timestamp = db.Column(db.String(50), default=lambda: datetime.now().strftime("%H:%M %d/%m"))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comments = db.relationship('Comment', backref='post', lazy=True)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    timestamp = db.Column(db.String(50), default=lambda: datetime.now().strftime("%H:%M")) # Giờ chat
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# --- CÁC ĐƯỜNG DẪN (ROUTES) ---

@app.route('/')
@login_required
def index():
    # Lấy bài viết mới nhất lên đầu
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('index.html', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        action = request.form.get('action') # Kiểm tra xem user ấn nút Login hay Register

        user = User.query.filter_by(username=username).first()

        if action == 'register':
            if user:
                flash('Tên này có người dùng rồi, chọn tên khác đi!')
            else:
                new_user = User(username=username, password=generate_password_hash(password, method='scrypt'))
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user)
                return redirect(url_for('index'))
        
        elif action == 'login':
            if not user or not check_password_hash(user.password, password):
                flash('Sai tài khoản hoặc mật khẩu rồi!')
            else:
                login_user(user)
                return redirect(url_for('index'))
                
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/upload', methods=['POST'])
@login_required
def upload():
    if 'file' not in request.files: return redirect(url_for('index'))
    file = request.files['file']
    caption = request.form.get('caption') # Lấy nội dung caption
    
    if file.filename == '': return redirect(url_for('index'))
    
    # Tạo tên file an toàn kèm thời gian để không bị trùng
    filename = secure_filename(f"{datetime.now().timestamp()}_{file.filename}")
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
    # Lưu vào Database
    new_post = Post(filename=filename, content=caption, user_id=current_user.id)
    db.session.add(new_post)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/comment/<int:post_id>', methods=['POST'])
@login_required
def add_comment(post_id):
    content = request.form.get('content')
    if content:
        new_comment = Comment(content=content, user_id=current_user.id, post_id=post_id)
        db.session.add(new_comment)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# --- KHỞI CHẠY ---
if __name__ == '__main__':
    with app.app_context():
        db.create_all() # Tự động tạo file database nếu chưa có
    app.run(port=3000, debug=True)