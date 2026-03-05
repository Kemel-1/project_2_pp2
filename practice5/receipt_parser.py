import re
import json
# Читаем файл
with open("raw.txt", encoding="utf-8") as f:
   text = f.read()
# Проверка на дубликат
is_duplicate = "ДУБЛИКАТ" in text
# Извлекаем названия товаров
products = re.findall(r"\d+\.\n(.+?)\n\d", text, re.DOTALL)
# Извлекаем цены после слова "Стоимость"
# Берём только число перед новой строкой
prices_raw = re.findall(r"Стоимость\n([\d\s,]+)\n", text)
# Убираем пробелы в числах и заменяем запятую на точку
prices = [float(p.replace(" ", "").replace(",", ".")) for p in prices_raw]
# Извлекаем итог
total_match = re.search(r"ИТОГО:\n([\d\s,]+)", text)
total = None
if total_match:
   total = float(total_match.group(1).replace(" ", "").replace(",", "."))
# Дата и время
datetime_match = re.search(r"Время:\s(.+)", text)
datetime_value = datetime_match.group(1) if datetime_match else None
# Способ оплаты
payment_match = re.search(r"(Банковская карта|Наличные)", text)
payment_method = payment_match.group(1) if payment_match else None
# Формируем словарь
data = {
   "is_duplicate": is_duplicate,
   "products": products,
   "prices": prices,
   "total": total,
   "datetime": datetime_value,
   "payment_method": payment_method
}
# Вывод JSON
print(json.dumps(data, ensure_ascii=False, indent=4))