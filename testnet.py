import speedtest
net = speedtest.Speedtest()
download = "{:.2f}".format(net.download()/1024/1024)
upload ="{:.2f}".format(net.upload()/1024/1024)
ping = net.results.ping
print(f"upload : {upload} mb")
print(f"download : {download} mb")
print(f"ping : {ping} ms")
