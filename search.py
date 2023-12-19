print("Loading Data...")
with open("turkishdata.txt", "r") as file:
	data = file.read().split("\n")
print("Data sucessfuly loaded √\n")
isim = input("Name: ").replace("i", "İ").upper()
soyisim = input("Surname: ").replace("i", "İ").upper()
query = f"{isim} {soyisim}"
print(f"Search Query: {query}\nSearching...\n")
founds = []
for d in data:
	if query in d:
		print(d)
