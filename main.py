from py1337x import py1337x
import sys

if sys.argv[1] == "-s" or sys.argv[1] == "--search":
    torrent_query = sys.argv[2]
    torrents = py1337x(proxy='1337x.to', cache='py1337xCache', cacheTime=500) 
    results = torrents.search(torrent_query)
    print(type(results))
