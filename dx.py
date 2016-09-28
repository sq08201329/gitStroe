#!/usr/bin/env.exe python
# -*-	coding: utf-8 -*-
import docx

docName = 'D:\Python\me\gitStroe\doc test.docx'

def readDocx(docName):
    fullText = []
    doc = docx.Document(docName)
    paras = doc.paragraphs
    for p in paras:
        fullText.append(p.text)
    return '\n'.join(fullText)

print(readDocx(docName))

