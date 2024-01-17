import selenium
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from openpyxl import Workbook, load_workbook 


service = Service()
option = webdriver.ChromeOptions()
##option.add_argument("--headless")
driver = webdriver.Chrome(service=service, options=option)

url = "https://codeforces.com/problemset"
user_url = input("Provide your codeforces USERNAME or FULL LINK: ")
url_beginning = "https://codeforces.com/profile/"
if (url_beginning not in user_url):
    user_url = url_beginning + user_url

name = user_url[len(url_beginning):]


driver.get(url)


tag_options = driver.find_element(By.TAG_NAME, "select")
tag_elements = [x for x in tag_options.find_elements(By.TAG_NAME, "option")] 

tag_names = {}
for item in tag_elements:
    tag = item.get_attribute("value")
    if tag is not None and tag != "" and tag != "combine-tags-by-or":
        tag_names[tag] = 0;



driver.get(user_url)


if (driver.current_url == "https://codeforces.com/"):
    print("The provided uersname does not exist! Please run the program again and enter a valid/existing username.")
    driver.quit()
    exit()

profile_overview = driver.find_element(By.CLASS_NAME, "info")
rating = 0
for line in profile_overview.text.splitlines():
    if "Contest rating" in line:
        rating = int(line.split()[2])

rating_lowerbound = min(3000, max(800, rating - 200 - rating%100))
rating_upperbound = min(3500, max(1200, rating + 400 - rating%100))


driver.get("https://codeforces.com/submissions/" + name)

solved_problems = set()
difficulty = 0

for i in range(1, 3):

    submission_url = "https://codeforces.com/submissions/" + name + "/page/" + str(i)
    driver.get(submission_url)

    if driver.current_url == "https://codeforces.com/":
        break

    submission_status = driver.find_elements(By.TAG_NAME, "tr")

    for submission in submission_status:
        if "Accepted" in submission.text:
            href_tags = submission.find_elements(By.TAG_NAME, "a")
            for tag in href_tags:
                if "contest" and "problem" in tag.get_attribute("href"):
                    solved_problems.add(tag.get_attribute("href"))
      
problem_count = len(solved_problems)


for problem_link in solved_problems:

    driver.get(problem_link)
    current_tags = driver.find_elements(By.CLASS_NAME, "tag-box")
    difficulty_found = False
    for tag in current_tags:
        if tag.text in tag_names.keys():
            tag_names[tag.text] += 1
        else:
            difficulty += int(tag.text[1:]) if tag.text[0]=="*" else int(tag.text)
            difficulty_found = True

    if not difficulty_found:
        problem_count -= 1



if problem_count == 0 and len(solved_problems) > 0:
    print("Difficulty is not yet determined")
elif problem_count == 0:
    print("User has not solved any problems.")
else:
    print("Average Difficulty: ", difficulty//problem_count)

for tags in tag_names:
    print(tags, tag_names[tags])

