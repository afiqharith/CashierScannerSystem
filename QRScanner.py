from pyzbar import pyzbar
import cv2
import winsound

IMAGEPATH = 'C:/Users/Afiq/Desktop/code.png'
FORMAT = 'utf-8'
COLOR = (0, 0, 255)
FREQUENCY = 2700
DURATION = 50


class QrScanner:
    def __init__(self, IMAGEPATH):
        self.image = cv2.imread(IMAGEPATH)
        self.barcodes = pyzbar.decode(self.image)
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

                print(f'[STATUS] Success!')
                print(f'[ INFO ] Type: {barcodeType}')
                print(f'[ INFO ] Data: {barcodeData}')
                cv2.imshow('QR Reader', self.image)
                cv2.waitKey(0)


if __name__ == '__main__':
    QrScanner(IMAGEPATH)