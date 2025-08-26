from flask import Flask,redirect,url_for,abort
from flask_admin import Admin
from app.src.models.models import Base,Users,Files,Logging
from flask_sqlalchemy import SQLAlchemy
from app.admin_menu.views import NewUserView,FileLoad,LogPanel,MyAdminIndexView







app = Flask(__name__)
app.secret_key = "SECRET"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:root123@localhost:3306/mydb"


db = SQLAlchemy(model_class=Base)
db.init_app(app)
admin = Admin(app,name="Админ Панель",template_mode="bootstrap4",index_view=MyAdminIndexView())





admin.add_view(NewUserView(Users,db.session,name="Пользователи"))
admin.add_view(FileLoad(Files,db.session,name="Файлы"))
admin.add_view(LogPanel(Logging,db.session,name="Логирование"))

@app.get('/')
def main():
    abort(code=403,description="Доступ к этой панели запрещен")




if __name__ == '__main__':
    app.run()