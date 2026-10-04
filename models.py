# Purpose: Define database (cols, tables, etc.)
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
db = SQLAlchemy()
class Information(db.Model): # db.Model: báo cho SQLAlchemy rằng class này là một database model và cần được map với một table
    id = db.Column(db.Integer, primary_key=True) # db.Column: tạo col, primary_key=True: Chọn cột này làm Khóa chính (Primary Key) của table
    created_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False) # phải có date để quản lý. Chú ý thêm timezone vì Timestamp này là timezone-aware. Đừng coi nó là một ngày giờ không có timezone
    title = db.Column(db.String(200), nullable=False) # db.String: tạo col kiểu text
    description = db.Column(db.Text) # db.String: tạo col kiểu text dài
    info_type = db.Column(db.String(50), nullable=False) # nullable=False: không cho phép nhận giá trị Null
    area = db.Column(db.String(50), nullable=False)
    severity = db.Column(db.String(20), nullable=False)