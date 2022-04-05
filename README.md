
# TraDel: Shipping platform for less developed countries
Many people leave their home countries temporarily or even permamently for studies abroad, as expats or for other, diverse social or economic reasons. Nowadays, in a highly globalized and digitalized world it is easy to stay in contact with the loved ones at home but it is expensive or in the case of less-developed countries sometimes simply not possible at all to ship private packages, globally. 


The solution? 

*TraDel* – Travel Delivery – is a non-commercial Crowd Shipping platform for private shipping connecting travelers who have some luggage space left to people who search for an affordable shipping option around the globe. Using available travel routes for private shipping can open new, more flexible and cheaper shipping options while reducing emissions and allowing travelers to compensate travel costs as well as doing something good. The website has a straightforward structure with a register and login function and the options to post a delivery request or offer and to search for available posts. Once a match is found all shipping conditions including price and date are privately discussed between the users.


## How to Setup and Run

In order to setup and run the project, please proceed as follows:

Start by creating an isolated virtual command.

```bash
python -m venv venv
.\venv\Scripts\activate.bat
```

```bash
pip install -r requirements.txt
```

After successful installation use the following command to run the project:

```bash
uvicorn src.main:app --reload
```

## Access

After starting open the following URL: [http://127.0.0.1:8000/static/index.html](http://127.0.0.1:8000/static/index.html)

For getting access to the FastAPI open the following URL: http://127.0.0.1:8000/docs


## Examples

The website includes general descriptions of the project (*About*) including the benefits and a descriptions of the functionalities as well as FAQs (*FAQ*). 
There is a register and login function for users to sign up. Afterwards they can post delivery requests and offers using the post form. A third form was added for searching available delivery requests or offers, i.e. receiving existing posts from the database. This search function is prepared in the frontend and backend and will be fully integrated and will be integrated in the next steps. Furthermore, contact options such as a chat function as well as a user rating system will be added next.

You can see the first design of the TraDel website here: 

![TraDel - Header](https://github.com/TechLabs-Dortmund/shipping-platform-for-less-developed-countries/blob/d1c197004209235952d9c872fd8330473d87fe5f/Screenshots/1_Tradel_Home.png)

![TraDel - About](https://github.com/TechLabs-Dortmund/shipping-platform-for-less-developed-countries/blob/d1c197004209235952d9c872fd8330473d87fe5f/Screenshots/2_Tradel_About.png) 

![TraDel - About2](https://github.com/TechLabs-Dortmund/shipping-platform-for-less-developed-countries/blob/d1c197004209235952d9c872fd8330473d87fe5f/Screenshots/3_Tradel_About_Benefits.png)

![TraDel - Options](https://github.com/TechLabs-Dortmund/shipping-platform-for-less-developed-countries/blob/d1c197004209235952d9c872fd8330473d87fe5f/Screenshots/4_Tradel_DeliveryOptions.png) 

  
## Roadmap

- main frontend development 
- adding descriptive texts in the frontend, incl. FAQs
- adding login, posting and search function, incl. backend communication 
- adding database using SQLite and database connection using fastAPI
- updating frontend (updating colours, texts and search function)  - ONGOING

- adding chat function & user rating system - PLANNED

  
## Authors

- [@Hikmat](https://www.github.com/hiko91)
- [@Taylan](https://github.com/taylanyild)
- [@Paulinus](https://github.com/PaulAyere)
- [@Nele](https://github.com/NelM3004)
- Paul 
- Michael


## Mentors
- [@Florian](https://github.com/TheMerphin)
- [@Tom](https://github.com/ScholliYT)


  

