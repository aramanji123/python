for file in strings/*.py
do
 echo "executing: $file"
 python "$file"
 echo "--"
done
