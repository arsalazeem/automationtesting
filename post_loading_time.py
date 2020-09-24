import post_data
import checkloadingtime
import pdb

url="https://gardne.com/index.html"
project_name="Gardne Web"
description="To check the loading time of "+url+" "+"and status of site."
getalist=checkloadingtime.checkk_loading_Time(project_name,description,url)
post_data.post_data_on_portal(getalist)