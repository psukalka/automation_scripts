#!/bin/sh
echo "Clearing db"
python clear_db.py
echo "Downloading kurmacore"
pip install kurmacore==0.1.0
echo "installing kurma"
cd /home/stsys/kurma
pip install .
echo "installing kurmacore"
cd /home/stsys/kurma-core
pip install .
cd ~
echo "Stopping kurma"
kurma stop -s all
echo "Starting kurma"
kurma start -s all
echo "cldearing older logs"
cd /data/kūrma-xenon/logs/
rm -rf *
cd -
python update_analysis_status.py
