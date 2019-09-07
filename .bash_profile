export PS1="\u@[\[$(tput sgr0)\]\[\033[38;5;70m\]\w\[$(tput sgr0)\]\[\033[38;5;15m\]] \\$ \[$(tput sgr0)\]"

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi

# ls always after cd
function cd {
    builtin cd "$@" && ls -F
}
