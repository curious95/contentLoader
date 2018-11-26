from subprocess import check_output
import json

out = check_output(['./phantomjs', '--ssl-protocol=any', \
    '--web-security=false', 'getResources.js', 'www.google.com'])
data = json.loads(out)