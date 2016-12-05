"""make graph"""
import pygal                                                       # First import pygal
from xlrd import open_workbook
def make_graph():
    """make graph in section center"""

    #open worksheet
    book = open_workbook('C:/projet_psit.xlsx')
    sheet = book.sheet_by_index(0) #code select sheet
    primary = [sheet.cell(1, col_index).value for col_index in range(1, 13)]
    junior = [sheet.cell(2, col_index).value for col_index in range(1, 13)]
    senior = [sheet.cell(3, col_index).value for col_index in range(1, 13)]
    vocational = [sheet.cell(4, col_index).value for col_index in range(1, 13)]
    high_vocational = [sheet.cell(5, col_index).value for col_index in range(1, 13)]
    undergraduate = [sheet.cell(6, col_index).value for col_index in range(1, 13)]

    #make graph
    line_chart =  pygal.Box() #รูปแบบของ graph
    line_chart.title = sheet.cell(0, 0).value
    year = []
    for i in ["2556", "2557", "2558"]:
        for j in range(1, 5):
            year.append(i+"/"+str(j))

    line_chart.x_labels = map(str, year)
    line_chart.add(sheet.cell(1, 0).value, primary)
    line_chart.add(sheet.cell(2, 0).value, junior)
    line_chart.add(sheet.cell(3, 0).value, senior)
    line_chart.add(sheet.cell(4, 0).value, vocational)
    line_chart.add(sheet.cell(5, 0).value, high_vocational)
    line_chart.add(sheet.cell(6, 0).value, undergraduate)
    line_chart.render_to_file('education.svg')

make_graph()
