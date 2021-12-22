from flask import render_template
class admin_manageAdministratorsBoundary:
    def __init__(self):
        pass

    def displayPage(self):
        return render_template('admin_manageAdministrators.html')