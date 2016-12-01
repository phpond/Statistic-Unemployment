"""make graph"""
import pygal                                                       # First import pygal
line_chart = pygal.Bar()
line_chart.title = 'อัตราการว่างงานภาคเกลาง'
line_chart.x_labels = map(str, ["2556/1", "2556/2"])
line_chart.add('ผู้หญิง', [0.6, 0.9, 0.7, 0.6, 0.7, 1.0, 0.9, 0.4, 0.9, 0.8, 1.0, 0.8])
line_chart.add('ผู้ชาย', [0.6, 0.7, 0.9, 0.8, 0.9, 1.2, 0.9, 0.8, 1.1, 0.8, 1.0, 0.9])
line_chart.render_to_file('bar_chart.svg')
def make_graph():
    """make graph in section center"""
    line_chart = pygal.Bar()
    line_chart.title = 'อัตราการว่างงานภาคกลาง'
    year = []
    for i in ["2556", "2557", "2558"]:
        for j in range(1, 5):
            year.append(i+"/"+str(j))
    line_chart.x_labels = map(str, year)
    line_chart.add('ผู้หญิง', [0.6, 0.9, 0.7, 0.6, 0.7, 1.0, 0.9, 0.4, 0.9, 0.8, 1.0, 0.8])
    line_chart.add('ผู้ชาย', [0.6, 0.7, 0.9, 0.8, 0.9, 1.2, 0.9, 0.8, 1.1, 0.8, 1.0, 0.9])
    line_chart.render_to_file('bar_chart.svg')
make_graph()
