from flask import render_template
class admin_overviewBoundary:
    def __init__(self):
        pass

    def displayPage(self):
        return render_template('admin_overview.html')