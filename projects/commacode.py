#assignment asked to write a code t
paymentType = []

def errorHandler():
    if len(paymentType) < 1: #handle payment type
        print ('There are no list items. Please check payment list items before executing again!')

def listConcatenator():
    listItem = ('')
    for item in paymentType:
        if paymentType.index(item) < (len(paymentType)-1):
            listItem = listItem + item + ', '
        else:
            listItem = listItem + 'and ' + item + '.'
    return listItem

errorHandler()
result = listConcatenator()
print ('You may use: {} '.format(result))