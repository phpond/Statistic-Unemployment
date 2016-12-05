"""make graph"""
import pygal                                                       # First import pygal
from xlrd import open_workbook
def make_graph():
    """make graph in section center"""

    #open worksheet
    book = open_workbook('C:/project_sex_v2.xlsx')
    type_sex = input().lower() #type_sex have > male, female and all
    if type_sex == "male":
        row = 1
    elif type_sex == "female":
        row = 2
    else:
        row = 3
    value_s = {}

    for i in range(1, 5):
        sheet = book.sheet_by_index(i) #code select sheet
        value_s[i] = [sheet.cell(row, col_index).value for col_index in range(1, 13)]

    #make graph แนกประเภท
    line_chart = pygal.Line() #รูปแบบของ graph
    line_chart.title = 'อัตราการว่างงาน แยกตามเพศ(%s)' %(str(sheet.cell(row, 0).value))
    year = []
    for i in ["2556", "2557", "2558"]:
        for j in range(1, 5):
            year.append(i+"/"+str(j))

    line_chart.x_labels = map(str, year)
    for i in range(1, 5): #add to graph
        sheet = book.sheet_by_index(i) #code select sheet
        title_left = str(sheet.cell(0, 0).value).split(' ')
        line_chart.add(title_left[1], value_s[i])
    storage = 'bar_chart'+type_sex+'.svg'
    line_chart.render_to_file(storage)

make_graph()
