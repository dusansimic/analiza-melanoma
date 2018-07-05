#!/bin/bash
while IFS='' read -r line || [[ -n "$line" ]]; do
	echo "$line"
	rm "../../Documents/melanoma-images/$line"
done < "$1"