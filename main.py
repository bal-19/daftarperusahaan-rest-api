from scrape.daftar_perusahaan import DaftarPerusahaan
from fastapi import FastAPI
from enum import Enum

class Category(str, Enum):
    bei = "bei"
    migas = "migas"
    farmasi = "farmasi"
    konstruksi = "konstruksi"
    pertambangan = "pertambangan"
    perbankan = "perbankan"
    properti = "properti"
    asuransi_jiwa = "asuransi-jiwa"
    asuransi_umum = "asuransi-umum"
    bumn = "bumn"

app = FastAPI()

@app.get("/daftarperusahaan/category/")
def get_data_by_category(category:Category, total_halaman:int = 0):
    """
    <h3>INPUT EXAMPLE: </h3>
    category = just select the value
    <br>
    total_halaman = 2, 1, 10 (default = 0)
    """
    link = f"https://www.daftarperusahaan.com/bidang/{category.value}?page=0"
    base_url = "https://www.daftarperusahaan.com/"
    scraped_data = DaftarPerusahaan.company_by_category(base_url=base_url, url=link, total_hal=total_halaman)

    return scraped_data 

@app.get("/daftarperusahaan/area/")
def get_data_by_area(area:str, total_halaman:int = 0):
    """
    <h3>INPUT EXAMPLE: </h3>
    area = jakarta selatan, jakarta
    <br> 
    total_halaman = 2, 1, 10 (default = 0)
    """
    area = area.lower().replace(" ", "-")
    link = f"https://www.daftarperusahaan.com/area/{area}?page=0"
    base_url = "https://www.daftarperusahaan.com/"
    scraped_data = DaftarPerusahaan.company_by_area(base_url=base_url, url=link, total_hal=total_halaman)

    return scraped_data