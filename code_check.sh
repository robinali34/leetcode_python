if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
pip install pytest coverage
pytest -v tests/ --junitxml=test-reports/report.xml
coverage run -m pytest -v tests/ --junitxml=test-reports/pycoverage.xml
coverage run --source=scripts -m unittest discover -v && coverage html && coverage report

pip install flake8
flake8 --max-line-length 130 . --extend-exclude=dist,build --show-source --statistics

if [ ! -d test-reports ]; then mkdir test-reports; fi
#pip install green
#python3 -m green --run-coverage --junit-report=test-reports/myproject-pytests.xml tests
python3 -m coverage xml -o test-reports/myproject-pycoverage.xml
python3 -m coverage html -d test-reports/myproject-pycoverage-html