from .serializers import SecuritySerializer
from .models import Security

def updateDatabase(response, name):
    content_trunc = response.find_all('div', attrs = {"class": "P6K39c"})
    content_trunc1 = response.find_all('div', attrs = {"class": "mfs7Fc"})

    data_dict = {}

    for i in range(len(content_trunc)):
        data_dict[content_trunc1[i].text] = content_trunc[i].text

    final_dict = {}
    
    final_dict["name"] = name
    final_dict["prev_close"] = data_dict["Previous close"]
    final_dict["pe_ratio"] = data_dict["P/E ratio"]
    final_dict["dividend_yield"] = data_dict["Dividend yield"]
    final_dict["primary_exchange"] = data_dict["Primary exchange"]

    # modelized_data = Security(**final_dict)
    # modelized_data.save()

    return final_dict
