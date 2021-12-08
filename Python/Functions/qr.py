import pyqrcode

url = pyqrcode.create("https://www.facebook.com/KhallidKonnections/shop/?ref_code=shops_messaging_share_storefront&ref_surface=shops_messaging_share_storefront")
print(url.terminal(quiet_zone=1))