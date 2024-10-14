class Bill:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.status = "proposed"

    def update_status(self, status):
        self.status = status

    def get_details(self):
        return f"Title: {self.title}, Description: {self.description}, Status: {self.status}"
