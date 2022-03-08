from google_images_download import google_images_download

kw = input("Enter keywords: ")
numpic = int(input("Enter number of pics: "))

response = google_images_download.googleimagesdownload()
arguments = {"keywords":kw,
             "limit":numpic,
             "print_urls":False}
paths = response.download(arguments)

#print complete paths to the downloaded images\
print(type(paths))
print(paths[0])