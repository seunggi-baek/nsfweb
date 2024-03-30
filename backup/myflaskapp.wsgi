#import os 

#activate_script = '/var/www/myflaskapp/flask-venv/bin/activate'
#os.system(f'source {activate_script}')

import sys
import site

# 가상 환경의 site-packages 디렉터리 경로
site.addsitedir('/var/www/myflaskapp/flask-venv/lib/python3.9/site-packages')

# 애플리케이션의 경로 추가
sys.path.insert(0, '/var/www/myflaskapp')

from app import app as application
