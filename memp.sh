#!/bin/bash

param="$1"

if [[ $# -eq 0 || $param == "-h" ]]; then
  echo -en "Usage: memp <option>\n\n"
  echo -en "-h         help menu\n"
  echo -en "-a         add a command or payload to memp.txt. you can add any other command or payload\n"
  echo -en "-e         Edit model, using any editor you like to open memp.txt\n"

  echo -en "\nExamples:\n"
  echo -en "./memp.sh ffuf                          Search keyword contain 'ffuf'\n"
  echo -en "./memp.sh -a 'nmap -sV 1.1.1.1'         Append 'nmap -sV 1.1.1.1' to memp.txt\n"
  echo -en "./memp.sh -e vim                        Using vim open memp.txt. replace vim with code is using vscode open it. And so on.\n"
  
  exit 1 

elif [ $# -eq 1 ]; then  
  echo -en "Search key word contain $param.\n"
  echo -en "The starting number indicates the original file line number.\n"
  echo -en "==============================================================\n\n"
  echo -en "#     Search results\n"
  echo -en "-     --------------\n"
  grep -in $param /home/ttmachine/Desktop/google_drive/command/memp.txt --color=always | sed 's/:/:  /'    #try using comtext search

else

  while getopts "a:e:" OPTION; do
    case $OPTION in
      a)
        echo -ne "\n$OPTARG\n" >> /home/ttmachine/Desktop/google_drive/command/memp.txt
        echo "Append $OPTARG to original file"
        ;;
      e)
        echo "Open original file with $OPTARG"
        $OPTARG /home/ttmachine/Desktop/google_drive/command/memp.txt
        ;;
      ?)
        echo "Invalid option";;
    esac
  done  
  # Shift positional arguments if needed
  # shift $((OPTIND - 1))
  # if [[ $1 ]]

fi


# getopts "m:" OPTION

# if [ $1 == "-h" ]; then
#     printf "-h"
# https://github.com/dwisiswant0/findom-xss/blob/master/findom-xss.sh


# alias scmd='cat ~/Desktop/google_drive/command/memp.txt | grep -i'
# alias Ecmd='vim ~/Desktop/google_drive/command/memp.txt'
# alias addcmd='~/Desktop/google_drive/command/addcm.sh'


#According to cognitive science, human memory is only good at recognition, not at retrieval. Moreover, Einstein once said, don't try to remember everything you can find, so how to query (retrieve) becomes a problem. The purpose of this project is to make it easy for you to find everything you have learned!
