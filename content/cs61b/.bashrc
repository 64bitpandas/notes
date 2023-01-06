# Filename: .bashrc
# Description: Sources in on the class MASTER version for settings information
# Author: Ben Cuan
# Last Edited 30 Jan 2020 for CS61B
# Please  edit this file unless you are sure of what you are doing.
# This file and other dotfiles have been written to work with each other.
# Any change that you are not sure off can break things in an unpredicatable
# ways.

# Set the Class MASTER variable and source the class master version of .cshrc

[[ -z ${MASTER} ]] && export MASTER=${LOGNAME%%-*}
[[ -z ${MASTERDIR} ]] && export MASTERDIR=$(eval echo ~${MASTER})

# Set up class wide settings
for file in ${MASTERDIR}/adm/bashrc.d/* ; do [[ -x ${file} ]] && . "${file}"; done

# Set up local settings
for file in ${HOME}/bashrc.d/* ; do [[ -x ${file} ]] && . "${file}"; done

# Vim master race
export EDITOR='vim'
export VISUAL='vim'

# Git helper
gb() {
        echo -n '(' && git branch 2>/dev/null | grep '^*' | colrm 1 2 | tr -d '\n' && echo  -n ')'
}
git_branch() {
        gb | sed 's/()//'
}

# Some PS1 ricing
export PS1="\[\033[38;5;219m\]\u\
\[$(tput sgr0)\]\[\033[38;5;15m\]@\
\[$(tput sgr0)\]\[\033[38;5;214m\]\h\
\[$(tput sgr0)\]\[\033[38;5;15m\] \
\[$(tput sgr0)\]\[\033[38;5;39m\]\w\
\[$(tput sgr0)\]\[\033[38;5;15m\] \
\[$(tput sgr0)\]\[\033[38;5;85m\]\t\
\[$(tput sgr0)\]\[\033[0;32m\] \$(git_branch)\
\[$(tput sgr0)\]\[\033[38;5;15m\]\n\
\[\033[38;5;11m\]🠶\
\[$(tput sgr0)\]\[\033[38;5;15m\] \
\[$(tput sgr0)\]"
