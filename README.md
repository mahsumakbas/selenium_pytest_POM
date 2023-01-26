# selenium_pytest_POM
it is a Page Object Model framework template to automate Web UI test through Selenium Webdriver library, written in Python and using pytest

To install plugins:
    pip install -r requirements.txt

to run test, go to main folder and run pytest:
    pytest --html=reports/report.htm --reruns 2 -n 4

parametres:
--html to produce execution result file
--reruns number of retry in case of test failed
-n number of parallel running threads

