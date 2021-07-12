from copy import Error
import pyqrcode


def generateCodes(params):
    if 'code' not in params :
        raise ValueError('Enter Valid Code')
    
    generated = []
    for x in range(1,params["amt"]+1):
        route = "{0}?batch={1}&id={2}".format(params["code"],params["tracking"],str(x))
        qr = pyqrcode.create(route)
        qr_xbm = qr.xbm(scale=3,quiet_zone=0)
        generated.append(qr_xbm)
    return generated



def createQR():
    code = pyqrcode.create('Knights who say ni!')
    code_xbm = code.xbm(scale=5)

    return code_xbm



data = {
    "tracking":"demo",
    "amt" : 2,
    "code" : 'https://www.dealerops.com'
}


try:
    generateCodes(data)
except ValueError as err:
    print(err)




