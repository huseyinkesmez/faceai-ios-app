# FaceAI iOS App Test Automation

This project contains automated 2 tests for the FaceAI iOS application using Python and Appium.

## Setup Instructions

### Prerequisites
- macOS (Required for iOS app testing)
- Python 3.8+
- Appium 2.0 or later
- WebDriverAgent
- iOS device or simulator
- XCode (for iOS development)

### Environment Setup
1. Create a virtual environment:
```bash
python -m venv .venv
```

2. Activate virtual environment:
```bash
source .venv/bin/activate 
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Appium Setup
1. Install Appium:
```bash
npm install -g appium
```

2. Start Appium server:
```bash
appium
```


## Test Cases

### Test Case 1: Paywall Screen Verification

Verify paywall screen displays correct subscription options and UI elements.

**Preconditions:**
- App installed (https://apps.apple.com/us/app/faceai-video-ai-face-change/id6470990632)
- No active subscription exists

**Test Steps:**
1. Launch the FaceAi app
2. Wait for paywall screen to load (10s timeout) 
3. Verify subscription options (10s timeout):
  - 1 Week (₺349,99) with "POPULAR" label
  - 1 Year (₺2.299,99) with "TOP CHOICE" label 
  - Lifetime (₺2.499,99) with "BEST VALUE" label
  - Default selected price display (₺2.299,99 Per Year)
4. Verify UI elements:
  - Close button (top right)
  - 'Try Now' button (gradient button)
  - 'Privacy Policy' link
  - 'Restore' link 
  - 'Terms of' Use link

**Expected Results:**
- Screen loads within 10 seconds
- All elements present with correct pricing 
- All buttons/links clickable

### Test Case 2: Home Screen Navigation & Pro Feature Access

**Reasoning for choosing this particular feature:** 

I approached the this app feature from the perspective of testing a video feature for the end user. I wanted to test whether the user can successfully navigate between videos and, when they click on a Pro feature, if we correctly show them the paywall screen. The goal is to convert user attention into revenue, so it's essential to ensure that we can successfully display the paywall screen at the right moment.


Verify navigation flow from home screen to paywall via pro feature interaction.

**Preconditions:**
- App installed (https://apps.apple.com/us/app/faceai-video-ai-face-change/id6470990632)
- No active subscription exists

**Test Steps:**
1. Launch the FaceAi app
2. Close paywall via 'closeDark' button
3. Verify home screen:
  - 'Discover' text visible
4. Access pro feature:
  - Scroll to 'Movie Characters' section
  - Select first character video
5. Verify paywall screen:
  - 'Swap Faces For a Year!' text visible
  - 10s timeout for screen load

**Expected Results:**
- Successful navigation through screens
- Paywall appears when accessing pro video feature 
- All elements load correctly

## Running Tests

### Running Tests with HTML Reports
To run tests and generate HTML reports:
```bash
python test_home.py
python test_paywall.py
```

### HTML Report Configuration
The tests are configured to automatically generate HTML reports using HtmlTestRunner. When you run a test:
1. The test will execute all test cases
2. An HTML report will be automatically generated in the `reports` directory
3. Report files will be named as follows:
   - `home_test_report.html` for home screen tests
   - `paywall_test_report.html` for paywall screen tests


### Viewing Reports
1. Navigate to the `reports` directory
2. Open the generated HTML report in a web browser
3. Reports are named with the following format:
   - `home_test_report.html`
   - `paywall_test_report.html`

###  A proposal for CI pipeline integration;

- Please navigate to the `ci_pipeline_proposal.txt` for CI pipeline using GitHub Actions
- Pipeline Configuration generated in the `.github/workflows/ios_tests.yml` file (example)

### - If you experience any issues;

Please feel free to reach out to me via `hsynksmz@outlook.com`
