from model import *
from datetime import *

def create_natas_levels(db):
	#Level 0  "You can find the password for the next level on this screen"
	db.session.add(Flag('level 0', 'Easy Peesy Password Squeezy', 10))
	
	#Level 1  "You can find the password for the next level on this screen but rightclicking has been blocked!"
	db.session.add(Flag('level 1', '', 15))
	
	#Level 2  "There is nothing on this page"
	db.session.add(Flag('level 2', '', 20))
	
	#Level 3  "Not even google will find it this time." #Robots.txt
	db.session.add(Flag('level 3', '', 25))
	
	#Level 4  "Access disallowed you are visiting from ..." #Referer Hack
	db.session.add(Flag('level 4', '', 50))
	
	#Level 5  "Access disallowed you are not logged in" #loggedin cookie hack
	db.session.add(Flag('level 5', '', 50))
	
	#
	db.session.add(Flag('level 6', '', 0))
	
	#
	db.session.add(Flag('level 7', '', 0))
	
	#
	db.session.add(Flag('level 8', '', 0))
	
	#
	db.session.add(Flag('level 9', '', 0))
	
	#
	db.session.add(Flag('level 10', '', 0))
	
	#
	db.session.add(Flag('level 11', '', 0))
	
	#
	db.session.add(Flag('level 12', '', 0))
	
	#
	db.session.add(Flag('level 13', '', 0))

def main():
	db.create_all()
	
	db.session.add(Player('jets', 'bmcmanus@gmail.com', '2b00042f7481c7b056c4b410d28f33cf', 1, 1))
	db.session.add(Board(1))
	create_natas_levels(db)
	db.session.commit()
	
	
if __name__ == "__main__":
	main()
