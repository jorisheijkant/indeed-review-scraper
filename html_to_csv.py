import os 
from bs4 import BeautifulSoup
import csv

jobs_folder = "html"
listings = []
limit = 10000

for (folder, labels, files) in os.walk(jobs_folder):
    for file_index, file in enumerate(files):
        if file_index < limit:
            file_path = f"{jobs_folder}/{file}"
            print(f"Parsing file {file_index}, {file}")
            with open(file_path, "r") as html_file:
                soup = BeautifulSoup(html_file, 'html.parser')
                reviews = soup.find_all("div", {"itemprop": "review"})

                print(f"{len(reviews)} reviews on this page")

                for review in reviews:
                    company = file.split('_')[0]
                    review_title = ""
                    review_text = ""

                    review_title_element = review.find("h2")
                    if review_title_element is not None:
                        review_title = review_title_element.text

                    review_text_element = review.find("span", {"itemprop": "reviewBody"})
                    if review_text_element is not None:
                        review_text = review_text_element.text
                    else:
                        print(f"No text found")
                
                    listings.append({
                        "company": company,
                        "review_title": review_title,
                        "review_text": review_text
                    })

with open("output.csv", "w") as csv_output:
    csv_writer = csv.writer(csv_output)
    csv_writer.writerow(["company", "title", "text"])

    for job in listings:
        csv_writer.writerow([job["company"], job["review_title"], job["review_text"]])

print(f"All data added to the csv")
            