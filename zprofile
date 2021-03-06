# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
setopt autocd beep extendedglob nomatch notify
bindkey -v
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/logan/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall

# Promp information
# the prompt shapes
PS1='%n@%m %* %/ -> '
PS2='-> '
PS3='-> '

alias duck='w3m duckduckgo.com'
alias google='w3m google.com'