#!/bin/bash

# This is a script to mitigate possibility of multiple parallel cron jobs being triggered(discussed here: https://facebook.com/timgrossmann/FacebookPy/issues/1235)
# The following is an example of a cron scheduled every 10 mins
# */10 * * * * bash /path/to/FacebookPy/run_facebookpy_only_once_for_mac.sh /path/to/FacebookPy/quickstart.py $USERNAME $PASSWORD $USERID

TEMPLATE_PATH=$1
USERNAME=$2
PASSWORD=$3
USERID=$4
if [ -z "$4" ]
then
   echo "Error: Missing arguments"
   echo "Usage: bash $0 <script-path> <username> <password>"
   exit 1
fi

if ps aux | grep $TEMPLATE_PATH | awk '{ print $11 }' | grep python
then
   echo "$TEMPLATE_PATH is already running"
else
   echo "Starting $TEMPLATE_PATH"
   /Users/ishandutta2007/.pyenv/shims/python $TEMPLATE_PATH -u $USERNAME -p $PASSWORD -ui $USERID --disable_image_load
   #/Users/ishandutta2007/.pyenv/shims/python $TEMPLATE_PATH -u $USERNAME -p $PASSWORD -ui $USERID --headless-browser --disable_image_load
fi

