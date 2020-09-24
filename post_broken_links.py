import find_broken_links
import post_data
import pdb
import login_instagram
import requests


url = "https://dev.xpal.com//"
project_name = "Xpal"
project_description = "To Check whether there are any Broken Links on "+url
#"To check Broken Links on" + " " + url
temp_list = find_broken_links._check_broken_links(url)
post_data.post_data_on_portal(temp_list, "Broken Links Check", project_description, project_name)

# temp=requests.get("https://twitter.com/xpal00")
# print(temp.status_code)


