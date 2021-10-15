from prettytable import PrettyTable
table = PrettyTable(['No', 'Name', 'ARC', 'Date', 'Phone'])

table.align = '1'

table.add_row(['1', 'Naing', '0909', 'Friday', '0909'])

print(table)
