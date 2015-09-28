import requests
def get(id):
    r = requests.post("http://tweeterid.com/ajax.php", data={"input":id})
    return r.text

if __name__ == "__main__":
	print get(39753128)
