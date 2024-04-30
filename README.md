# Daftarperusahaan Rest API

This project is an implementation of a RESTful API for the website daftarperusahaan.com. The API allows users to access data of companies listed on the daftarperusahaan.com website through a clear and well-documented interface. By utilizing this API, developers can easily integrate company information into their own applications, view details, and access up-to-date information about various companies.

## Getting Started

These instructions will give you a copy of the project up and running on
your local machine for development and testing purposes. See deployment
for notes on deploying the project on a live system.

### Installing

1. Clone Repository

       git clone https://github.com/bal-19/daftarperusahaan-rest-api.git

2. Navigate to Project Directory

        cd daftarperusahaan-rest-api

3. Create Virtual Environment (Optional)

        python3 -m venv env

4. Activate Virtual Environment (Optional)

   - Windows: 

            .\env\Scripts\activate

   - macOS/Linux:

            source env/bin/activate

5. Install Dependencies

        pip install -r requirements.txt

6. Run the FastAPI Server

        uvicorn main:app --reload

7. Access the Api

    [docs](http://127.0.0.1:8000/docs)    

## License

[MIT](LICENSE)
