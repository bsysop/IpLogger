# Burp Extension - IpLogger

**IpLogger** is a basic Burp Extension that will make a request to `https://api.ipify.org` every time Burp is opened and will store the IP and date in `iplogger.json`.

> iplogger.json can be found in the same directory as IpLogger.py is stored.

**Log Example:**
```json
{
    "date": "2022-12-27 19:23:54.039000", 
    "ip": "74.21.1.45"
}
{
    "date": "2022-12-27 19:24:07.281000", 
    "ip": "80.61.9.22"
}
```

The logs can be read with any text editor or using an JSON library like `jq`.
```bash
$ cat iplogger.json | jq -r .ip

74.21.1.45
80.61.9.22
```