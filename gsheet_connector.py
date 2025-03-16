import gspread


class Sheet:
    def __init__(self, sheet_name, worksheet_name=None):
        self.sheet_tickets = None
        self.sheet_name = sheet_name
        self.client = gspread.service_account(filename="client_secret.json")
        self.set_worksheet_id(worksheet_name)

    def get_worksheet_id(self, worksheet_name):
        sheets = self.client.open(self.sheet_name).worksheets()
        if worksheet_name is None:
            return sheets[0].id
        for sheet in sheets:
            if sheet.title == worksheet_name:
                return sheet.id
        raise ValueError(f"Worksheet with name {worksheet_name} not found")

    def set_worksheet_id(self, worksheet_name):
        self.worksheet_id = self.get_worksheet_id(worksheet_name)
        self.sheet = self.client.open(self.sheet_name).get_worksheet_by_id(
            self.worksheet_id
        )

    def insert_paper_horizontal(self, start_row, start_col, data):
        for idx, col in enumerate(range(start_col, start_col + len(data))):
            self.sheet.update_cell(start_row, col, data[idx])

    def insert_paper_vertical(self, start_row, start_col, data):
        for idx, row in enumerate(range(start_row, start_row + len(data))):
            self.sheet.update_cell(row, start_col, data[idx])
