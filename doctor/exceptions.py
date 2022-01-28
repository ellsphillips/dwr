class InvalidChartTypeError(Exception):
    def __init__(self):
        Exception.__init__(self, "Invalid chart type provided.")


class NoDataSuppliedError(Exception):
    def __init__(self):
        Exception.__init__(self, "No data provided to Doctor environment.")
