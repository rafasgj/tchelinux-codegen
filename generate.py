import qrcode
import qrcode.image.svg
import yaml
import sys


ymlfile = 'example.yml'
if len(sys.argv) > 0:
    ymlfile = sys.arvg[0]

data = None
with open(ymlfile, 'r') as f:
    data = yaml.safe_load(f)

print(data)

for cname in data['cname']:
    url = "https://%s.tchelinux.org" % cname
    img = qrcode.make(data=url, image_factory=qrcode.image.svg.SvgImage)
    img.save("%s.svg" % cname)
