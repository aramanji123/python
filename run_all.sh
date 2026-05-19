#!/bin/usr/env bash

set -euo pipefail

#list  folders
folders=("functions" "Numeric" "regex" "strings")

for folder in "${folders[@]}"
do 
 echo "checking  the folder : $folder"
 
 # Skip if folder does not exist
  if [ ! -d $folder ];then
  echo " foldernot found : $folder"
  continue
  fi

  for file in "$folder"/*.py
  do
   [-f "$file" ] || continue

   echo "executing $file "
   python "$file"
  done
  done
echo "all python files executed successfully"
  


