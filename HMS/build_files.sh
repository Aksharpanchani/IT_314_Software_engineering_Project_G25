echo " BUILD START"
python4.11.1 -m pip install -r requirements.txt
python4.11.1 manage.py collectstatic --noinput --clear
echo " BUILD END"