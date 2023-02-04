# selenium_pytest_POM
it is a Page Object Model framework template to automate Web UI test through Selenium Webdriver library, written in Python and using pytest

To install plugins:

    pip install -r requirements.txt

to run test, go to main folder and run pytest:

    pytest --html=reports/report.htm --reruns 2 -n 4 --platform mobile|web --browser chrome|firefox

parametres:
`--html` : to produce execution result file

`--reruns` : number of retry in case of test failed

`-n` : number of parallel running threads

`--platform` : to choose whether run mobile or web tests. Valid values: mobile or web. Default is web

`--browser` : To run web test on specific browsers. Valid values: chrome or firefox (support rest of browsers coming soon). Default is chrome

P.S. If you will never use mobile functions, you can remove "Appium-Python-Client" entity from requirements.txt and related part in conftest.py
