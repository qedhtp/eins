#!/bin/sh

new_line="$1"

if [ $# -ne 1 ]; then
  echo "Usage: $0 new_line"
  exit 1
fi


echo "\n$new_line" >> ~/Desktop/google_drive/command/commands.txt

