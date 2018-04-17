import entry
import datetime

today = datetime.date.today().isoformat()

x = entry.create(today,
        '19:32:46.064759',
        None,
        'red',
        'Example description',
        [])
entry.persist(x)

y = entry.create(today,
        '19:42:46.064759',
        None,
        'red',
        'Example description',
        [])
entry.persist(y)
