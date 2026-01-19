class AppState:
    def __init__(self):
        self.BREAK_UNTIL_TIMESTAMP = 0
        self.BREAK_WARNING_SENT = False

current_state = AppState()