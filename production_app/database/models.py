from production_app.database import db as mysql

class DBCopy(mysql.Model):
    __tablename__ = ''
    copy = mysql.Column(mysql.String(128), nullable=False)
