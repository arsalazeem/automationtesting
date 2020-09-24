import search_text
import post_data
print("Note:This Module is only written for Terms&Condition,Privacy Policy pages or pages where text is placed in Paragraph tags.")
print("Incase of any internal page always call the login module first in order to perform the module operation or the test will fail")
print("Please enter Page Url")
print("")
url=input()
print("Please enter Search Query")
print("")
query=input()
print("Main fucntion")
k=search_text.search_whole_page(url,query)
if k>0:
    messege="Fail"
else:
    messege="Pass"
# datalist
data_list={}
data_list["page_url"]=url
data_list["search_query"]=query
data_list["No of occurances"]=str(k)
#datalist_ends
# mainlist
mainlist={}
mainlist["sample_values"]=data_list
mainlist["result"]=messege
# mainlist_ends
#posting results on portal
post_data.post_data_on_portal(mainlist, "Search Term", "To check whether a Term is present on the provided WebPage", "Gardne")
#


