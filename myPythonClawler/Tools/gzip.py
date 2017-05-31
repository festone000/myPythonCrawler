import gzip

def ungzip(data):
    try:
        print("unzipping...")
        data = gzip.decompress(data)
        print("unzip finished")
    except:
        print("not gzipped,no need to unzip")
    return data;