# Remove all the cache files / folders
echo '######## Removing all the cache files ########'
find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf
echo '######## Done ########'


echo 'Removing project.zip (if exists)'
rm -rf project.zip > /dev/null 2>&1
echo 'Done'

echo '######## Zipping the project deliverables ########'
# This script will be used to zip the final project deliverables. Keep adding stuffs as required
zip -r project.zip README.md requirements.txt online_video_platform 
echo '######## Done ########'


# delete testing folder if any and recreate
rm -rf test_final_deliverables
mkdir -p test_final_deliverables

cp project.zip test_final_deliverables
cd test_final_deliverables
unzip project.zip
echo '######## Creating virtual env ########'
# create virtual env
python3 -m venv env
echo '######## Done ########'

echo '######## Activating virtual env and installing required libraries ########'
# activate
source env/bin/activate
# install all required libraries
pip install -r requirements.txt
echo '######## Done ########'

cd online_video_platform

echo '######## Applying migrations and running server ########'
# make migrations
python manage.py makemigrations
# migrate
python manage.py migrate --run-syncdb
# runserver
python manage.py runserver

