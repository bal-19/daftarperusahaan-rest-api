from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests

class DaftarPerusahaan:
    def company_by_category(base_url, url, total_hal):
        try:
            category = url.split("/")[-1].split("?")[0]
            total = 0
            
            data = {
                "link": url,
                "status": None,
                "category": category,
                "company_list": [],
                "total": None,
                "total_page": total_hal
            }
            
            while url:
                current_page = int(url.split("=")[1])
                if current_page > total_hal: break
                
                response = requests.get(url)

                data["status"] = response.status_code
                
                soup = BeautifulSoup(response.text, 'html.parser')
                
                for company in soup.select(".node"):
                    company_name = company.select_one("h2 > a").text
                    company_link = company.select_one("h2 > a")["href"]
                    company_ctg = []
                    for ctg in company.select("div:nth-child(3) > div > div.category > ul > li"):
                        company_ctg.append(ctg.text)
                    
                    company_area = []
                    for area in company.select("div:nth-child(3) > div > div.tags > ul.links > li"):
                        company_area.append(area.text)
                        
                    soup_company = BeautifulSoup(requests.get(urljoin(base_url, company_link)).text, 'html.parser')
                    
                    address = soup_company.select_one(".node > div.content.clear-block > p")
                    if address: address = address.text.strip()
                    
                    code = soup_company.select_one(".node > div.content.clear-block > div.field.field-type-text.field-field-kode > div.field-items > div")
                    if code: code = code.text.strip()
                    
                    telp = soup_company.select_one(".node > div.content.clear-block > div.field.field-type-text.field-field-telepon > div.field-items > div")
                    if telp: telp = telp.text.strip()
                    
                    fax = soup_company.select_one(".node > div.content.clear-block > div.field.field-type-text.field-field-fax > div.field-items > div")
                    if fax: fax = fax.text.strip()
                    
                    email = soup_company.select_one(".node > div.content.clear-block > div.field.field-type-text.field-field-email > div.field-items > div")
                    if email: email = email.text.strip()
                    
                    website = soup_company.select_one(".node > div.content.clear-block > div.field.field-type-text.field-field-website > div.field-items > div")
                    if website: website = website.text.strip()
                    
                    broker = soup_company.select_one(".node > div.content.clear-block > div.field.field-type-text.field-field-broker > div.field-items > div")
                    if broker: broker = broker.text.strip()
                    
                    npwp = soup_company.select_one(".node > div.content.clear-block > div.field.field-type-text.field-field-npwp > div.field-items > div")
                    if npwp: npwp = npwp.text.strip()
                    
                    
                    data["company_list"].append({
                        "link": urljoin(base_url, company_link),
                        "company": company_name,
                        "address": address,
                        "code": code,
                        "telp": telp,
                        "fax": fax,
                        "email": email,
                        "website": website,
                        "broker": broker,
                        "npwp": npwp,
                        "category": company_ctg,
                        "area": company_area,
                        "page": current_page
                    })
                    
                    total += 1
                    data["total"] = total
                
                next_link = soup.select_one('#squeeze > div > div > div.clear-block > div.item-list > ul > li.pager-next > a')
                if next_link:
                    url = next_link.get('href')
                    url = urljoin(base_url, url)
                else:
                    url = None
            return data
            
        except Exception as e:
            return {"error": str(e), "status": response.status_code}
        
    def company_by_area(base_url, url, total_hal):
        try:
            area = url.split("/")[-1].split("?")[0]
            total = 0
            
            data = {
                "link": url,
                "status": None,
                "area": area,
                "company_list": [],
                "total": None,
                "total_page": total_hal
            }
            
            while url:
                current_page = int(url.split("=")[1])
                if current_page > total_hal: break
                
                response = requests.get(url)

                data["status"] = response.status_code
                
                soup = BeautifulSoup(response.text, 'html.parser')
                
                for company in soup.select(".node"):
                    company_name = company.select_one("h2 > a").text
                    company_link = company.select_one("h2 > a")["href"]
                    company_ctg = []
                    for ctg in company.select("div:nth-child(3) > div > div.category > ul > li"):
                        company_ctg.append(ctg.text)
                    
                    company_area = []
                    for area in company.select("div:nth-child(3) > div > div.tags > ul.links > li"):
                        company_area.append(area.text)
                        
                    soup_company = BeautifulSoup(requests.get(urljoin(base_url, company_link)).text, 'html.parser')
                    
                    address = soup_company.select_one(".node > div.content.clear-block > p")
                    if address: address = address.text.strip()
                    
                    code = soup_company.select_one(".node > div.content.clear-block > div.field.field-type-text.field-field-kode > div.field-items > div")
                    if code: code = code.text.strip()
                    
                    telp = soup_company.select_one(".node > div.content.clear-block > div.field.field-type-text.field-field-telepon > div.field-items > div")
                    if telp: telp = telp.text.strip()
                    
                    fax = soup_company.select_one(".node > div.content.clear-block > div.field.field-type-text.field-field-fax > div.field-items > div")
                    if fax: fax = fax.text.strip()
                    
                    email = soup_company.select_one(".node > div.content.clear-block > div.field.field-type-text.field-field-email > div.field-items > div")
                    if email: email = email.text.strip()
                    
                    website = soup_company.select_one(".node > div.content.clear-block > div.field.field-type-text.field-field-website > div.field-items > div")
                    if website: website = website.text.strip()
                    
                    broker = soup_company.select_one(".node > div.content.clear-block > div.field.field-type-text.field-field-broker > div.field-items > div")
                    if broker: broker = broker.text.strip()
                    
                    npwp = soup_company.select_one(".node > div.content.clear-block > div.field.field-type-text.field-field-npwp > div.field-items > div")
                    if npwp: npwp = npwp.text.strip()
                    
                    
                    data["company_list"].append({
                        "link": urljoin(base_url, company_link),
                        "company": company_name,
                        "address": address,
                        "code": code,
                        "telp": telp,
                        "fax": fax,
                        "email": email,
                        "website": website,
                        "broker": broker,
                        "npwp": npwp,
                        "category": company_ctg,
                        "area": company_area,
                        "page": current_page
                    })
                    
                    total += 1
                    data["total"] = total
                
                next_link = soup.select_one('#squeeze > div > div > div.clear-block > div.item-list > ul > li.pager-next > a')
                if next_link:
                    url = next_link.get('href')
                    url = urljoin(base_url, url)
                else:
                    url = None
            return data
            
        except Exception as e:
            return {"error": str(e), "status": response.status_code}