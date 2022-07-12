def myFunction(inputData,spLetter):
    txt = inputData.lower().split(spLetter)

    sumTxt = ""
    for text in txt:
        sumTxt += text.capitalize() + " "

    sumTxt = sumTxt.strip()
    return sumTxt


















