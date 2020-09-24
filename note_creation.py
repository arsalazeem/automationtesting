import android_login
import create_notes
import locktill_check_empty_screen
import variable_names
import post_data




fail = 0
total = 1
exception = "none"
# removing all notes through reverse PIN
android_login.valid_login("arsal11211@yopmail.com", "12345678", "654321")
# creating a new note
driver = create_notes.create_notes(1)
temp_result = locktill_check_empty_screen.check_empty(driver)
if temp_result:
    result = variable_names.failed
    fail = 1
    print("No note is created")
else:
    result = variable_names.passed
    print("A note has been created")
# end of note creation

sample_values = {}
sample_values["form_name"] = "Note Creation"
sample_values["note_title"] = "note title"
sample_values["note_description"] = "note description"
sample_values["recipent"] = "none"
sample_values["share_note"] = "now"
sample_values[variable_names.actualresult] = result
sample_values[variable_names.expectedresult] = variable_names.passed
sample_values[variable_names.totalcount] = str(1)
sample_values[variable_names.totalfailed] = str(fail)
sample_values[variable_names.n_exception] = exception

jsonlist = []
jsonlist.append(sample_values)
print(jsonlist)
# creation of passlist
mainlist = {}
mainlist[variable_names.sample_values] = jsonlist
mainlist[variable_names.currenttime] = variable_names.get_time()
mainlist[variable_names.pageurl] = "com.lock.till"
mainlist[variable_names.innerdata] = ""
mainlist[variable_names.totalcount] = str(total)
mainlist[variable_names.totalfailed] = str(fail)
mainlist[variable_names.actualresult] = result
mainlist[variable_names.expectedresult] = variable_names.passed
#end of passlist creation

#posting result over portal API
list=variable_names.show_project_name()
post_data.post_data_on_portal(mainlist,"Note Creation","To check wheather user is able to create a note or not",list[1],list[0])
