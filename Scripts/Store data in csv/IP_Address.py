#Use this to know your IP address to get the access code.
import requests as rq

if __name__ == "__main__":
    url="https://api.repec.org/call.cgi"
    payload={"whatismyip" : "1"}
    response = rq.get(url,params=payload)
    print ("url call form:", response.url)
    content=response.content
    IP=content.decode("utf-8")
    print ("ID address:", IP)
