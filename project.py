'''
Project : Statistic Unemployment
'''

from xlrd import open_workbook
def main():
    ''' import statistic from excel to make a graph'''
    book = open_workbook('D:/project1.xlsx')
    sheet = book.sheet_by_index(0)
    keys = [sheet.cell(0, col_index).value for col_index in range(sheet.ncols)]
    dict_list = []
    for row_index in range(1, sheet.nrows):
        d = {keys[col_index]: sheet.cell(row_index, col_index).value
        for col_index in range(sheet.ncols)}
        if d != {'': ''}:
            dict_list.append(d.get(''))
        print(d)
    print(dict_list)
    #ทดลองง
main()
