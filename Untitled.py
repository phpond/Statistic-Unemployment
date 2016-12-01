"""make graph"""
import pygal                                                       # First import pygal
from xlrd import open_workbook
def make_graph():
    """make graph in section center"""

    #open worksheet
    book = open_workbook('C:/project_sex_v2.xlsx')
    choose_sheet = int(input()) #ืีnumber_sheet >> 0.ทั่วราชอาณาจักร 1.กลาง 2.เหนือ 3.ตะวันออกเฉียงเหนือ 4.ใต้
    sheet = book.sheet_by_index(choose_sheet) #code select sheet
    male = [sheet.cell(1, col_index).value for col_index in range(1, 13)]
    female = [sheet.cell(2, col_index).value for col_index in range(1, 13)]

    #make graph
    line_chart = pygal.Line() #รูปแบบของ graph
    line_chart.title = sheet.cell(0, 0).value
    year = []
    for i in ["2556", "2557", "2558"]:
        for j in range(1, 5):
            year.append(i+"/"+str(j))

    line_chart.x_labels = map(str, year)
    line_chart.add(sheet.cell(2, 0).value, female)
    line_chart.add(sheet.cell(1, 0).value, male)
    storage = 'bar_chart'+str(choose_sheet)+'.svg'
    line_chart.render_to_file(storage)

make_graph()
