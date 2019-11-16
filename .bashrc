# Define a shell variable to the top of the project
x=$HOME/Documents/DjangoWorkshop

echo $x

# Run the web server
alias x='./manage.py runserver 8005'

# Django Workshop
alias djw='. ~/Documents/DjangoWorkshop/.bashrc'

# Setup shell context
alias bashrc='. $x/.bashrc'

# Git status
alias g='cd $x && git status'


# Django Management commands
alias m=./manage.py


# Git commit of all project code
function com {
    git add -A $x &&
    git commit -m "$*" &&
    git pull &&
    git push
}

function d {
    cd $1
    ls -al
}


# Show the context
cat <<EOF
 ____  _                         
|  _ \(_) __ _ _ __   __ _  ___  
| | | | |/ _' | '_ \ / _' |/ _ \ 
| |_| | | (_| | | | | (_| | (_) |
|____// |\__,_|_| |_|\__, |\___/ 
    |__/             |___/       
__        __         _        _                 
\ \      / /__  _ __| | _____| |__   ___  _ __  
 \ \ /\ / / _ \| '__| |/ / __| '_ \ / _ \| '_ \ 
  \ V  V / (_) | |  |   <\__ \ | | | (_) | |_) |
   \_/\_/ \___/|_|  |_|\_\___/_| |_|\___/| .__/ 
                                         |_|    
EOF

d $x
