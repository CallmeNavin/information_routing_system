# Purpose: Run application
from flask import Flask, render_template, request # render_template: function Flask cung cấp để đọc file HTML trong folder templates rồi gửi nó về browser. request là object Flask cung cấp để mình đọc request mà browser vừa gửi tới
from models import db, Information # db = công cụ để làm việc với database. Information = model/table đã định nghĩa trong models.py

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///routing.db' # app.config = chỗ chứa các cài đặt của app. ["SQLALCHEMY_DATABASE_URI"]: tên một setting mà Flask-SQLAlchemy quy định sẵn, nó hỏi database m nằm đâu. sqlite:///routing.db: Tao dùng SQLite, database nằm trong file routing.db
db.init_app(app) # db kết nối vào app này => Công cụ db sẽ làm việc với file database tên routing.db trong app này

with app.app_context(): # Trong phạm vi app này (do có thể có nhiều app)
    db.create_all() # dùng SQLAlchemy để tạo các table đã định nghĩa vào database routing.db

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/submit", methods=["POST"])
def submit():
    title = request.form["title"] # Trong dữ liệu form mà browser vừa gửi tới, lấy cho t giá trị của field có tên title
    description = request.form["description"]
    info_type = request.form["info_type"]
    area = request.form["area"]
    severity = request.form["severity"]
    new_information = Information(title=title, description=description, info_type=info_type, area=area, severity=severity) # Tạo một record Information mới, lấy dữ liệu từ 5 biến Python vừa nhận
    db.session.add(new_information) # Session, tao muốn thêm object new_information này vào database
    db.session.commit() # Xác nhận các thay đổi trong session và ghi chúng xuống database
    return "Information saved successfully"
@app.route("/information")
def information_list():
    information = Information.query.all()
    return render_template("information.html", information=information) # information=information: bên trái chính là biến Python vừa query all, còn bên phải nghĩa là: Flask cần nói rõ “Tao gửi giá trị này sang HTML, và ở bên HTML hãy gọi nó bằng tên information

if __name__ == "__main__":
    app.run(debug=True) # debug=True: bật chế độ debug, khi code có lỗi thì sẽ hiển thị chi tiết lỗi trên trình duyệt