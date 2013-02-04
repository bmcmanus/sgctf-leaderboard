from model import *
from datetime import *
db.create_all()

admin = Player('jets', 'bmcmanus@gmail.com', '2b00042f7481c7b056c4b410d28f33cf', 1, 1)
board = Board(1)
db.session.add(admin)
db.session.add(board)
db.session.commit()