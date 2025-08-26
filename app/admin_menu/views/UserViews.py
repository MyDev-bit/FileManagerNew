from flask_admin.contrib.sqla import ModelView
from flask_admin.base import AdminIndexView,expose

class NewUserView(ModelView):
    create_modal = True
    edit_modal = False
    can_delete = False
    can_create = True
    can_edit = True
    page_size = 300
    can_set_page_size = False
    can_export = True




class FileLoad(ModelView):
    can_delete = False
    can_edit = False
    can_create = False
    page_size = 300
    can_set_page_size = True
    can_export = True


class LogPanel(ModelView):
    can_delete = False
    can_edit = False
    can_create = False
    create_modal = False
    can_export = True
    can_view_details = False
    create_template = False
    column_formatters_detail = False


class MyAdminIndexView(AdminIndexView):
    def is_visible(self):
        return False

    @expose("/")
    def index(self):
        return redirect(url_for("users.index_view"))