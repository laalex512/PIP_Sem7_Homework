# Модуль input.py содержит функции для получения
# информации из txt или csv файлов
# Модуль writer.py содержит функции для записи информации
# с последующим хранением в csv файл
# Модуль output.py выводит информацию, отфильтрованную по ключу
# и значению в консоль или в csv файл
# keys.py содержит набор ключей, по которым хранится информация
# controller.py сводит все функции всех модулей в один
# main.py - порядок выполнения команд


from controller import *

WriteInCsv(InputTxtData("input.txt"))
WriteInCsv(InputCsvData("input.csv"))
OutputDataInConsole("Last Name", "Иванов")
OutputDataInCsv("Status", "Работает")
