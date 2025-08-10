# Selenium & Appium Test Automation Framework With Pytest in POM Style

It is a Page Object Model framework template to automate Web UI test through Selenium Webdriver library, written in Python and using pytest

To pull repo, install git:
https://git-scm.com/downloads
select item that regarding your OS

Install Python:
https://www.python.org/downloads/

To install plugins:

    pip install -r requirements.txt

to run test, go to main folder and run pytest:

    pytest --html=reports/report.htm --reruns 2 -n 4 --platform mobile|web --browser chrome|firefox

Note: in some CI/CD cases, pytest cannot be recognazied as PATH command, so need to run as `python` module
`python -m pytest`

parametres:
`--html` : to produce execution result file

`--reruns` : number of retry in case of test failed

`-n` : number of parallel running threads

`--platform` : to choose whether run mobile or web tests. Valid values: mobile or web. Default is web

`--browser` : To run web test on specific browsers. Valid values: chrome or firefox (support rest of browsers coming soon). Default is chrome

P.S. If you will never use mobile functions, you can remove "Appium-Python-Client" entity from requirements.txt and related part in conftest.py

# Mobile testing
To run mobile tests, you need to have Appium server running on your machine. You can download it from https://appium.io/
or install it via npm:
```bash
npm install -g appium
```

To start Appium server, run the following command in your terminal:
```bash
appium
``` 
## Mobile testing with Android
To run mobile tests, you need to have Android SDK installed and configured on your machine. 

### download and install Android SDK via Homebrew for macOS
install it via Homebrew on macOS:
```bash
brew install --cask android-sdk
``` 
### Set up Android SDK from command line and setup environment variables
You need to set up the following environment variables in your shell configuration file (e.g., `.bashrc`, `.zshrc`, `.bash_profile`, or `.profile`):

first set ANDROID_HOME to the path where Android SDK will be installed:
```bash
export ANDROID_HOME=<your_android_sdk_path>
export PATH=$PATH:$ANDROID_HOME
```
Replace `<your_android_sdk_path>` with the actual path where Android SDK is installed.

Download commandline tools from https://developer.android.com/studio#command-line-tools-only
choose for your OS and extract it to the Android SDK directory.

Create `latest` directory in cmdline-tools directory and then, move the extracted commandline tools to the `latest` directory:

```bash
mkdir -p $ANDROID_HOME/cmdline-tools/latest
```

```bash
add that directory to your PATH:
```bash
export PATH=$PATH:$ANDROID_HOME/cmdline-tools/latest/bin
```

Run the following command to install the necessary Android SDK components:
```bash
sdkmanager "platform-tools" "platforms;android-30"
```

For example, here's how to install the latest platform tools and the SDK tools for API level 33:
```bash
sdkmanager "platform-tools" "platforms;android-33"
sdkmanager "system-images;android-31;default;x86_64"
sdkmanager "sources;android-33"
sdkmanager "platforms;android-33"
sdkmanager "build-tools;33.0.0"
```

Then, add the following lines to your shell configuration file to include the necessary Android SDK tools in your PATH:
```bash
export PATH=$PATH:$ANDROID_HOME/tools
export PATH=$PATH:$ANDROID_HOME/tools/bin
export PATH=$PATH:$ANDROID_HOME/platform-tools
```

### Start Appium Inspector

Method 1: You can also download Appium Inspector as Desktop app from `https://github.com/appium/appium-inspector/releases`

Method 2: To start Appium Inspector from web go to following website:
`https://inspector.appiumpro.com/`

P.S. If you want to use Appium Inspector from web, you need to allow cors connections in Appium server. You can do it by running Appium with the following command:
```bash
appium --allow-cors
``` 
Capability builder is used to set up the desired capabilities for the Appium session. It allows you to specify various options such as the platform, device name, app package, and app activity.
JSON representation of the desired capabilities is generated and can be used to start the Appium session.
```json
{
  "platformName": "Android", //mandatory
  "appium:automationName": "UiAutomator2",//mandatory
  "appium:deviceName": "Android Emulator",
  "appium:platformVersion": "11.0",
  "appium:appPackage": "com.testpine.app",
  "appium:appActivity": "com.testpine.app.MainActivity",
  "appium:newCommandTimeout": 60,
  "appium:noReset": true,
  "appium:fullReset": false,
  "appium:autoGrantPermissions": true,
  "appium:skipDeviceInitialization": true
}
```

### Android SDK tips:
To check if Android SDK is installed correctly, run the following command:
```bash
sdkmanager --list
```

If there is error while running `sdkmanager`:
Specify it explicitly with `--sdk_root=<your_android_sdk_path>` parameter:
```bash
sdkmanager --sdk_root=<your_android_sdk_path> --list
```