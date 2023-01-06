pytest -v -m "sanity" --html=Reports\reports.html .\testCases\ --browser chrome
pytest -v -m "sanity" --html=Reports\reports.html .\testCases\ --browser firefox
rem pytest -v -m "sanity or regression" --html=Reports\reports.html .\testCases\ --browser chrome
rem pytest -v -m "sanity and regression" --html=Reports\reports.html .\testCases\ --browser chrome
rem pytest -v -m "regression" --html=Reports\reports.html .\testCases\ --browser chrome