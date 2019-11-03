import openpyxl
from commons import dump, process, save_yaml_file

velocity = 30


def process_worksheet(ws):
    header = []
    data_set = []

    for row in ws.iter_rows(max_row=1):
        for cell in row:
            header.append(cell.value.lower().replace(' ', '_'))
    for row in ws.iter_rows(min_row=2):
        data = {}
        for idx, cell in enumerate(row):
            data[header[idx]] = cell.value
        data_set.append(data)
    return data_set


def process_excel_file(file):
    wb = openpyxl.load_workbook(file)
    cfg = {x['area']: x['velocity'] for x in process_worksheet(wb.get_sheet_by_name('teams'))}
    for ws in wb.worksheets:
        area = ws.title.lower()
        if area.startswith('arkusz') or area.startswith('sheet') or area.startswith('common'):
            continue

        data_set = process_worksheet(ws)

        if area == "teams":
            output = dump(data_set)
        else:
            output = process(data_set, cfg.get('velocity', 1))
        save_yaml_file(output, area)


process_excel_file('base_excel_file.xlsx')
