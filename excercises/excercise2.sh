export LC_ALL=C; find $1 -type f -exec grep -ha '^#!/' {} \; | awk '{print $1}' | sort -n | uniq -c | sort -nr
