from sqlalchemy.util.deprecations import pending_deprecation
from app import db,users
db.create_all()
sam = users('shan')
frank=users('frank')
print(sam.id)
print(frank.id)
db.session.add_all([sam,frank])
db.session.add(frank)
db.session.add(sam)
db.session.commit()
print(sam.id)
print(frank.id)