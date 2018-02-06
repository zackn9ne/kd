import readline, glob, shutil, os.path, os
def complete(text, state):
    return (glob.glob(text+'*')+[None])[state]

readline.set_completer_delims(' \t\n;')
readline.parse_and_bind("tab: complete")
readline.set_completer(complete)
newfilename = raw_input('file? ')
home = os.path.expanduser("~")
dest = '/.ssh/'
fulldest = home + dest
head, tail = os.path.split(newfilename)
cleaned = home + dest + tail
cmd="chmod 600 "+cleaned

print newfilename,'copying to:',fulldest
shutil.copy2 (newfilename,fulldest)
print 'setting permissions on...',cleaned
os.system(cmd)
print 'now making public key for use'
os.system("ssh-keygen -y -f ~/.ssh/id_rsa > ~/.ssh/id_rsa.pub")
print 'recalculating splines...'

while True:
    # your code


    user = raw_input('Enter your name:')
    server = raw_input('Enter your server:')

    cmd2="ssh-copy-id -i {0} {1}@{2}".format(cleaned,user,server)
    os.system(cmd2)

    cont = raw_input("Another one? yes/no > ")
    while cont.lower() not in ("yes","no"):
        cont = raw_input("Another one? yes/no > ")
    if cont == "no":
        break

