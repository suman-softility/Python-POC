from models.models import Result


dummy_url = "https://www.google.com"
dummy_word_count = [["GoogleSearch", 1], ["Images", 1], ["Maps", 1], ["Play", 1], ["YouTube", 1], 
["News", 1], ["Gmail", 1], ["Drive", 1], ["Web", 1], ["History", 1], ["Settings", 1], ["Sign", 1], 
["Advanced", 1], ["searchHave", 1], ["questions", 1], ["COVID-19", 1], ["vaccine", 1], ["Get", 1], [
    "factsGoogle", 1], ["offered", 1], ["Advertising", 1], ["ProgramsBusiness", 1], ["SolutionsAbout", 1], 
    ["GoogleGoogle.co.in\u00a9", 1], ["Privacy", 1], ["Terms", 1]]
dummy_word_count_dict = {"GoogleSearch": 1, "Images": 1, "Maps": 1, "Play": 1, "YouTube": 1, 
"News": 1, "Gmail": 1, "Drive": 1, "Web": 1, "History": 1, "Settings": 1, "Sign": 1, 
"Advanced": 1, "searchHave": 1, "questions": 1, "COVID-19": 1, "vaccine": 1, "Get": 1, 
    "factsGoogle": 1, "offered": 1, "Advertising": 1, "ProgramsBusiness": 1, "SolutionsAbout": 1, 
    "GoogleGoogle.co.in\u00a9": 1, "Privacy": 1, "Terms": 1}
dummy_result = Result(dummy_url, dummy_word_count_dict, dummy_word_count_dict)