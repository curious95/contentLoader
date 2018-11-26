from subprocess import check_output

out = check_output(['../phantomjs/phantomjs', '--ssl-protocol=any', \
    '--web-security=false', 'sniff.js', 'https://stackoverflow.com'])

print(out)
