from pyzbar import pyzbar
import cv2
import winsound
import json

IMAGEPATH = 'barcode/fish.png'
FORMAT = 'utf-8'
COLOR = (0, 0, 255)
FREQUENCY = 2700
DURATION = 50


class QrScanner:
    def __init__(self, IMAGEPATH, START = True):
        self.image = cv2.imread(IMAGEPATH)
        self.barcodes = pyzbar.decode(self.image)

        if START == True:
            self.get()

    def get(self):
        if self.barcodes:
            for i in range(2):
                winsound.Beep(FREQUENCY, DURATION)

            for barcode in self.barcodes:
                (x, y, w, h) = barcode.rect
                cv2.rectangle(self.image, (x, y), (x + w, y + h), COLOR, 5,
                            cv2.LINE_AA)

                barcodeData = barcode.data.decode(FORMAT)
                barcodeType = barcode.type

                self.getData(barcodeData)
                cv2.imshow('QR Reader', self.image)
                

    def getData(self, barcodeData):
        listItems = barcodeData[2:] 
        with open("ItemsData.json") as file:
            data = json.load(file)
            details = data.get(f'ID{listItems}')
            print(f'[ ITEMS ] {details[0]}')
            print(f'[ PRICE ] {details[1]} MYR')


if __name__ == '__main__':
    QrScanner(IMAGEPATH)
    cv2.waitKey(0)