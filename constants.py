class Color:
    RED    = 'red'
    ORANGE = 'orange'
    GREEN  = 'green'
    TEAL   = 'teal'
    BLUE   = 'blue'
    PINK   = 'pink'
    BLACK  = 'black'
ALL_COLORS = [attr for attr in dir(Color) if not callable(getattr(Color, attr)) and not attr.startswith("__")] 

DB_DIR = 'db'
