import re
import subprocess
import pafy
import os
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open("SPREADSHEET").sheet1

data = str(sheet.get_all_records())

#data = ["https://www.youtube.com/watch?v=9lwkMQOjzo0", "00:10-00:20", "https://www.youtube.com/watch?v=8Pa9x9fZBtY", "01:00-02:00"]

links = []
urlpattern = r"(https?\://(www)?.?y[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3}(/[^<'\";]*)?)"
url_matches = re.findall(urlpattern, str(data))
for match in url_matches:
	links.append(match[0])


times = []
start_times = []
end_times = []

timepattern = r"((([0-9]\d:[0-9]\d-[0-9]\d:))\w+)"
time_matches = re.findall(timepattern, str(data))
for match in time_matches:
	times.append(match[0])

for time in times:
    start = time[:(-(time.find("-")+1))]
    end = time[(-(time.find("-"))):]
    start_times.append(start)
    end_times.append(end)

"""
for link in links:
	bashCommand = ('youtube-dl -o ORIGINAL/%(title)s.%(ext)s --extract-audio --audio-format mp3 {}').format(link)
	process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
	output, error = process.communicate()
"""
	
samples = os.listdir("/ORIGINAL/")

counter = 0
for sample in samples:
	audio_file = "/ORIGINAL/" + sample
	video = (pafy.new(links[counter]))
	out_file = "/SHORTENED/" + str(video.title) + ".mp3"

	start_time = "00:" +start_times[int(counter)]
	end_time = "00:" + end_times[int(counter)]

	bashCommand = ('avconv -i {} -ss {} -t {} -codec copy {}').format(audio_file, start_time, end_time, out_file)
	#process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
	#output, error = process.communicate()
	
	#LAST TWO LINES COMMENTED OUT TO CUMPLY WITH YOUTUBE'S POLICY.

	counter += 1
	


