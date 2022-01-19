for file in *; do
		  if [ -f "$file" ]; then
					 name=$(echo "$file" | sed 's/\.[^.]*$//');
					 ext="-ent.md"
					 new_name="$name$ext"
					 cp $file $new_name

		  fi	
done		  
