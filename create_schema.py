from model import *
from datetime import *

def create_natas_levels(db):
    #Level 0  "You can find the password for the next level on this screen"
    db.session.add(Flag('level 0', 'Easy Peesy Password Squeezy', 50))

    #Level 1  "You can find the password for the next level on this screen but rightclicking has been blocked!"
    db.session.add(Flag('level 1', 'How did all the pretty color get here?', 50))

    #Level 2  "There is nothing on this page"
    db.session.add(Flag('level 2', 'Nothing but the password that is', 100))

    #Level 3  "Not even google will find it this time." #Robots.txt
    db.session.add(Flag('level 3', 'Mr. Roboto..', 150))

    #Level 4  "Access disallowed you are visiting from ..." #Referer Hack
    db.session.add(Flag('level 4', 'How do you know what site I\'m visiting from?', 200))

    #Level 5  "Access disallowed you are not logged in" #loggedin cookie hack
    db.session.add(Flag('level 5', 'I want candy and cookies and milk!', 200))

    #Level 6 "Input secret:" #view the include
    db.session.add(Flag('level 6', 'Don\'t overthink it', 100))

    #Level 7 "Home About" #include file through url
    db.session.add(Flag('level 7', 'Is that really a good idea?', 225))

    #Level8 "Input secret: View sourcecode" #decoding
    db.session.add(Flag('level 8', 'Do you understand what the code is doing?', 275))

    #Level9 "Input secret: View sourcecode" #code injection
    db.session.add(Flag('level 9', 'PHP has commands to read in files, you don\'t need to do it this way.', 300))

    #Level10 "For security reasons, we now filter on certain characters" #grep '' /etc/natas_webpass/natas11 #
    db.session.add(Flag('level 10', 'You filter, but not enough.  Go grep Go!', 350))

    #Level11 "Cookies are protected with XOR encryption" # xor cookie/original text to get key.  key is repeating pattern
    db.session.add(Flag('level 11', 'It\'s like algrebra.  Notice anything about the key you recovered', 500))

    #Level12 "Choose a JPEG to upload (max 1KB):" # filename is passed from client 
    db.session.add(Flag('level 12', 'Do you trust your users?', 425))

    #Level13 "For security reasons, we now only accept image files!" # magic header (16 bytes from JPEG into PHP)
    db.session.add(Flag('level 13', 'It\'s magic!', 500))

    #Level14 "Username: Password:" # sql injection 
    db.session.add(Flag('level 14', 'Popular with the skiddies', 200))

    #Level15 "Username: Check existence" # SQL returns true/false, blind sql data extraction a letter at a time
    db.session.add(Flag('level 15', 'I\'m blind where is the data?', 550))

    #Level16 "For security reasons, we now filter even more on certain characters  Find words containing:" 
    #parameters to grep are quoted, command substitution to test characters a letter at a time from 
    #/etc/natas_webpass/natas17 if true then display something from dictionary, if not nothing.  Brute forces
    #one character at a time.  
    db.session.add(Flag('level 16', 'Substitute what with what?', 550))

def main():
    db.create_all()
    db.session.add(Player('jets', 'Brian McManus', 'bmcmanus@gmail.com', '2b00042f7481c7b056c4b410d28f33cf', 1, 1))
    db.session.add(Board(1))
    create_natas_levels(db)
    db.session.commit()

if __name__ == "__main__":
    main()
