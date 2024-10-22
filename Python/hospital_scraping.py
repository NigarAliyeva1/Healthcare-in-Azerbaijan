from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd # type: ignore


chrome_options = Options()

chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")


service = Service(executable_path=f"C:/Users/Chrome Driver/chromedriver-win64/chromedriver.exe")


driver = webdriver.Chrome(service=service, options=chrome_options)

main_url = f"https://doctortap.az/hospital_list/az"
driver.get(main_url)

time.sleep(2)


hospital_data = []


hospital_links = driver.find_elements(By.XPATH, "//a[@style='text-decoration: none;']")
hospital_urls = [link.get_attribute('href') for link in hospital_links]


for index, hospital_url in enumerate(hospital_urls):
    try:
        driver.get(hospital_url)
        time.sleep(1) 


        hospital_info = {}

        hospital_name = driver.find_element(By.XPATH, "//div[@class='col-md-12 cs_dc_title']/h1").text.strip()
        hospital_info['HospitalName'] = hospital_name

        try:
            hospital_type = driver.find_element(By.XPATH, "//div[@class='col-md-12 cs_dc_type']/p").text.strip()
        except:
            hospital_type = "Unknown"
        hospital_info['HospitalType'] = hospital_type

        try:
            rating = driver.find_element(By.XPATH, "//span[@class='cs_dc_star_number']").text.strip()
        except:
            rating = "No rating"
        hospital_info['Ratings'] = rating

        try:
            address = driver.find_element(By.XPATH, "//div[@class='col-md-12']/p").text.strip()
        except:
            address = "No address"
        hospital_info['Address'] = address

        try:
            phone_number = driver.find_element(By.XPATH, "//button[contains(@class, 'btn btn-success cs_rounded_button cs_btn_gray')]").text.strip()
        except:
            phone_number = "No phone number"
        hospital_info['PhoneNumber'] = phone_number

        try:
            creation_date = driver.find_element(By.XPATH, "//div[@class='col-md-12']//ul/li").text.strip()
            hospital_info['LastRenovationDate'] = creation_date.split(" ")[0] 
        except:
            hospital_info['LastRenovationDate'] = "No renovation date"

        try:

            service_elements = driver.find_elements(By.XPATH, "//div[@class='row mb-3'][2]//p")
            services = [service.text.strip() for service in service_elements if service.text.strip()]
            hospital_info['Specialties'] = ", ".join(services) 
        except:
            hospital_info['Specialties'] = "No specialties"

        hospital_data.append(hospital_info)

        print(f"Scraped hospital: {hospital_name}")

    except Exception as e:
        print(f"Error while scraping hospital {hospital_name}: {e}")


driver.quit()

df = pd.DataFrame(hospital_data)
df.to_csv('raw_hospital_dataset.csv', index=False)

print("Data scraping complete. Data saved to hospital_dataset.csv")