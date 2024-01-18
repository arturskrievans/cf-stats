import requests
from bs4 import BeautifulSoup
import random

url = "https://codeforces.com/problemset"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

options = soup.find_all('option')


tag_names = {}
success_rate = {}
for option in options:
    tag = option.get('value')
    if tag != "" and tag != "combine-tags-by-or":
        tag_names[tag] = 0
        success_rate[tag] = 0
    

url_beginning = "https://codeforces.com/profile/"
username = input("Provide your codeforces USERNAME or FULL LINK: ")

if url_beginning not in username:
    username = url_beginning + username

name = username[len(url_beginning):]

response = requests.get(username)
actual_url = response.url

if actual_url != username:
    print("The name you provided is not correct or does not exist! Please run the program again and provide a valid username.")
    exit()

soup = BeautifulSoup(response.text, 'html.parser')
div_container = soup.find(class_="info")
li_elements = div_container.find_all('span', style = "font-weight:bold;")

rating = 0
if len(li_elements) > 0:
    rating = li_elements[0].text

rating = int(rating)
rating_lowerbound = min(3000, max(800, rating - 200 - rating%100))
rating_upperbound = min(3500, max(1200, rating + 400 - rating%100))


all_problems = set()
cur_page = 1

total_difficulty = 0
difficulty_count = 0

while True:

    cur_url =  "https://codeforces.com/submissions/" + name + "/page/" + str(cur_page)
    response = requests.get(cur_url)


    soup = BeautifulSoup(response.text, 'html.parser')

    successful_submission = False

    submission_data = soup.find_all("td")
    for cell in submission_data:
        parsed = cell.text.replace("  ", "").replace("\n", "")
        if "Accepted" in parsed:
            successful_submission = True
 
    
  
    sub_count = 0
    all_links = soup.find(class_="datatable").find_all("a")
    for link in all_links:
        href_value = link.get('href')
        if "contest" and "problem" in href_value:
            build_link = "https://codeforces.com" + href_value
            if build_link not in all_problems:

                response = requests.get(build_link)
                soup = BeautifulSoup(response.text, 'html.parser')

                tags = soup.find_all("span", class_="tag-box")
                for tag in tags:

                    parsed = tag.text.replace("\n", "").replace("  ", "")
                    filtered = [x for x in tag_names.keys() if x in parsed]

                    for x in filtered:
                        tag_names[x] += 1
                        if successful_submission:
                            success_rate[x] += 1
                        
                    digits = [x for x in parsed if x >= "0" and x <= "9"]
                    if len(digits) > 0:
                        total_difficulty += int("".join(digits))
                        difficulty_count  += 1
    
                   

                all_problems.add(build_link)
            sub_count += 1
        
   
    if sub_count < 50:
        break

    cur_page += 1



avg_rate = 0
rate_count = 0
avg_tag_frequency = 0

for key in tag_names:
    avg_tag_frequency += tag_names[key]
    if tag_names[key] == 0:
        continue
    success_rate[key] = success_rate[key]/tag_names[key]*100
    avg_rate += success_rate[key]
    rate_count += 1

avg_rate /= rate_count
avg_tag_frequency /= len(tag_names)


problem_url = "https://codeforces.com/problemset/?tags={}-{}".format(rating_lowerbound, rating_upperbound)
response = requests.get(problem_url)
soup = BeautifulSoup(response.text, 'html.parser')

print(rating_lowerbound, rating_upperbound)

last_page = int(soup.find_all("span", class_="page-index")[-1].text)
recommended_problems = []


valid_length = True
while valid_length:
    page = random.randint(1, last_page)
    problem_url = "https://codeforces.com/problemset/page/{}?tags={}-{}".format(page, rating_lowerbound, rating_upperbound)
    response = requests.get(problem_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    td_con = soup.find_all("td")
    for div in td_con:
        for elements in div.find_all("div", style="float: right; font-size: 1.1rem; padding-top: 1px; text-align: right;"):
            for li in elements.find_all("a"):
                if li.text == "*special problem":
                    continue
            
                if success_rate[li.text] <= avg_rate or tag_names[li.text] <= avg_tag_frequency:
                    if len(recommended_problems) < 5:
                        problem_id = div.find("div", style="float: left;").find("a").get("href")
                        build_link = "https://codeforces.com" + problem_id
                        if build_link not in all_problems and build_link not in recommended_problems and len(recommended_problems) < 5:
                            recommended_problems.append(build_link)


                        if len(recommended_problems) == 5:
                            valid_length = False
                            break

                if not valid_length:
                    break

        if not valid_length:
            break
    
        
for problem in recommended_problems:
    print(problem)



