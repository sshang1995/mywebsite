import csv
ref_filename = '/Users/shangshu/shushang.me/reference.csv'
air_filename = '/Users/shangshu/shushang.me/airquality/annual_aqi_by_county_2019.csv'
out_filename = '/Users/shangshu/shushang.me/combined.csv'

state_county_to_lat_long = {}
# key is (state,county)
# value is (lat, long)
with open(ref_filename, 'r') as ref_file:
	# format: state, country, lat, long
	ref_csv_reader = csv.reader(ref_file)
	next(ref_csv_reader) # skip th first line
	for line in ref_csv_reader:
		ref_key = (line[0], line[1])
		lat_long = (line[2], line[3])
		state_county_to_lat_long[ref_key] = lat_long

for key in state_county_to_lat_long.keys():
 	# print(f"key: {key}, val:{state_county_to_lat_long[key]}")
 	pass

# air_header is "State,County,Year,Days with AQI,Good Days,Moderate Days,Unhealthy for Sensitive Groups Days,Unhealthy Days,Very Unhealthy Days,Hazardous Days,Max AQI,90th Percentile AQI,Median AQI,Days CO,Days NO2,Days Ozone,Days SO2,Days PM2.5,Days PM10"
out_header = ["State","County","Year","Days with AQI","Good Days","Moderate Days","Unhealthy for Sensitive Groups Days","Unhealthy Days","Very Unhealthy Days","Hazardous Days","Max AQI","90th Percentile AQI","Median AQI","Days CO","Days NO2","Days Ozone","Days SO2","Days PM2.5","Days PM10","Latitude","Longitude"]


with open(air_filename, 'r') as air_file,\
     open(out_filename, 'w') as out_file:

	air_csv_reader = csv.reader(air_file)
	next(air_csv_reader) # skip th first line
	out_csv_writer = csv.writer(out_file)

	# write the out csv header
	out_csv_writer.writerow(out_header)

	for line in air_csv_reader:
		ref_key = (line[0], line[1])
		lat_long = state_county_to_lat_long[ref_key]
		new_line = line + list(lat_long)
		# print(new_line)
		out_csv_writer.writerow(new_line)




