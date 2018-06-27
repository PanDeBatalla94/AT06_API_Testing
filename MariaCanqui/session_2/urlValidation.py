start = "http://"
def validate_url(url):
    global start
    count = 0
    for word in url.split(" "):
        if word.find(start) != -1 and url.find(start)+len(word) < len(url) and url[url.find(start)+len(word)] == " ":
            count = 1
            break

    if count == 0:
        print(url, "not contains a valid url")
    else:
        print(url, "contains a valid url")

validate_url("sentence http://sdfsd valid")
validate_url("http://sdfsd")
validate_url("http://sdfsd ")