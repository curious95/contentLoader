from subprocess import check_output
import re
import csv


with open('../data/output.csv', mode='a+') as domain_file:
    domain_writer = csv.writer(domain_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    domain_writer.writerow(['Domain', 'JSLibs', 'sourceDomain'])

with open('../data/data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(row[1])
            line_count += 1
        elif row[1] != '':
            print(row[1])
            out = check_output(['../phantomjs/phantomjs', '--ssl-protocol=any', \
                                '--web-security=false', 'sniff.js', row[1]]).decode("utf-8")
            # regex to find urls
            domains = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', out)

            uniqueDomains = set()
            for url in domains:
                url = url.split("://")[1].split("/")[0]
                uniqueDomains.add(url)

            urls = re.findall('[\-\.a-z 0-9]*\.js',out)
            uniqueUrl = set(urls)

            with open('../data/output.csv', mode='a+') as domain_file:
                domain_writer = csv.writer(domain_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                domain_writer.writerow([row[1], str(uniqueUrl).replace('{','').replace('}','').replace('\'',''), str(uniqueDomains).replace('{','').replace('}','').replace('\'','')])

            line_count += 1