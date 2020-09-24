import base64
import initchrome
from datetime import date
import post_data
import json
import pdb
import xlrd
import return_list_to_post
mainlist = {}
# sample_values={}
device_parent_list = []
# def read_data():




def toJson(a):
    return json.dumps(a, default=lambda o: o.__dict__)


def convert_base64(a):
     temp = a[1::]
     temp = temp[1::]
     temp = temp[:-1]
     return temp


def test_ui_return_list(url):
     # getting size
     loc = "C:\\Users\\ENSX-PC\\Desktop\\workspace\\Enabling\\data\\resolutions.xlsx"
     wb = xlrd.open_workbook(loc)
     sheet = wb.sheet_by_index(0)
     for i in range(1, sheet.nrows):
          device = sheet.cell_value(i, 0)
          width = int(sheet.cell_value(i, 1))
          height = int(sheet.cell_value(i, 2))
          driver = initchrome.start()
          url =url
          driver.get(url)

          device_data = "temp_dict" + str(i)
          device_data = {}
          device_data["device"] = device
          device_data["width"] = width
          device_data["height"] = height

          # mainlist["resolution"] = "500*500"
          # mainlist["image_base64"] = str(encoded_string)
          # sample_values["sample_Values"] = mainlist
          # sample_values = toJson(sample_values)
          driver.set_window_size(width, height)
          driver.refresh()
          driver.save_screenshot("arsal.png")
          with open("arsal.png", "rb") as image_file:
               encoded_string = base64.b64encode(image_file.read())
          temp = str(encoded_string)
          temp = convert_base64(temp)
          # file1 = open(r"C:\Users\ENSX-PC\Desktop\arsalazeem.txt", "a")
          # file1.write("*****")
          # file1.close()
          device_data["page_url"] = url
          device_data["screenshot"] = temp
          device_parent_list.append(device_data)
          driver.quit()

     return device_parent_list


def ui_testing(project_name,url):
     sample_values={}
     # post_data_hook.post_data_hook(mainlist)
     sample_values["sample_values"] = test_ui_return_list(url)
     sample_values = return_list_to_post.toJson(sample_values)
     mainlist["Id"] = "0"
     mainlist["Test"] = "UI Testing"
     mainlist["Project"] = project_name
     mainlist["Description"] = "To view UI in different provided resolutions"
     mainlist["MetaData"] = sample_values
     mainlist["DateAdded"] = str(date.today())
     mainlist["DateUpdated"] = str(date.today())
     mainlist["ProjectName"] = project_name
     post_data.post_data_on_portal(mainlist)
     file1 = open(r"C:\Users\ENSX-PC\Desktop\arsalazeem.txt", "a")
     file1.write(str(mainlist))
# test_ui_return_list("https://gardne.com/")
ui_testing("Gardne","https://gardne.com/")