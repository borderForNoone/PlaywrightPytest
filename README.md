# Playwright Pytest Python

The Playwright Pytest Python project.

# Preconditions

1. Install Python3;
2. Install Playwright;
3. Install Pytest;
3. Install any code editor.
4. Install Allure commandline.

# Steps to run

Run the command below

```
pytest -n 6 --alluredir=allure-results
```

# Report

To generate report run: 
```
npx allure generate allure-results --clean -o allure-report
```
The report is generated in the file `index.html` inside the allure-report folder.

# CI

Testing runs in GitHub actions and deploys a report in the [gh-pages](https://borderfornoone.github.io/PlaywrightPytest/) branch.

Report link: https://borderfornoone.github.io/PlaywrightPytest/
