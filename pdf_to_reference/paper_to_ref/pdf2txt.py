#!/usr/bin/env python
import sys
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice, TagExtractor
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.cmapdb import CMapDB
from pdfminer.layout import LAParams
from pdfminer.image import ImageWriter

# main
def main(fname, k, v):

    # debug option
    debug = 0
    # input option
    password = ''
    pagenos = set()
    maxpages = 0
    # output option
    outfile = None
    outtype = None
    imagewriter = None
    rotation = 0
    stripcontrol = False
    layoutmode = 'normal'
    codec = 'utf-8'
    pageno = 1
    scale = 1
    caching = True
    showpageno = True
    laparams = LAParams()

    if k == '-d':
        debug += 1
    elif k == '-p':
        pagenos.update( int(x)-1 for x in v.split(',') )
    elif k == '-m':
        maxpages = int(v)
    elif k == '-P':
        password = v
    elif k == '-o':
        outfile = v
    elif k == '-C':
        caching = False
    elif k == '-n':
        laparams = None
    elif k == '-A':
        laparams.all_texts = True
    elif k == '-V':
        laparams.detect_vertical = True
    elif k == '-M':
        laparams.char_margin = float(v)
    elif k == '-L':
        laparams.line_margin = float(v)
    elif k == '-W':
        laparams.word_margin = float(v)
    elif k == '-F':
        laparams.boxes_flow = float(v)
    elif k == '-Y':
        layoutmode = v
    elif k == '-O':
        imagewriter = ImageWriter(v)
    elif k == '-R':
        rotation = int(v)
    elif k == '-S':
        stripcontrol = True
    elif k == '-t':
        outtype = v
    elif k == '-c':
        codec = v
    elif k == '-s':
        scale = float(v)
    #
    PDFDocument.debug = debug
    PDFParser.debug = debug
    CMapDB.debug = debug
    PDFPageInterpreter.debug = debug
    #
    rsrcmgr = PDFResourceManager(caching=caching)
    if not outtype:
        outtype = 'text'
        if outfile:
            if outfile.endswith('.htm') or outfile.endswith('.html'):
                outtype = 'html'
            elif outfile.endswith('.xml'):
                outtype = 'xml'
            elif outfile.endswith('.tag'):
                outtype = 'tag'
    if outfile:
        outfp = file(outfile, 'w')
    else:
        outfp = sys.stdout
    if outtype == 'text':
        device = TextConverter(rsrcmgr, outfp, codec=codec, laparams=laparams,
                               imagewriter=imagewriter)
    elif outtype == 'xml':
        device = XMLConverter(rsrcmgr, outfp, codec=codec, laparams=laparams,
                              imagewriter=imagewriter,
                              stripcontrol=stripcontrol)
    elif outtype == 'html':
        device = HTMLConverter(rsrcmgr, outfp, codec=codec, scale=scale,
                               layoutmode=layoutmode, laparams=laparams,
                               imagewriter=imagewriter, debug=debug)
    elif outtype == 'tag':
        device = TagExtractor(rsrcmgr, outfp, codec=codec)
    else:
        return usage()
 
    fp = file(fname, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.get_pages(fp, pagenos,
                                  maxpages=maxpages, password=password,
                                  caching=caching, check_extractable=True):
        page.rotate = (page.rotate+rotation) % 360
        interpreter.process_page(page)
    fp.close()
    device.close()
    outfp.close()
    return

if __name__ == '__main__': sys.exit(main(sys.argv))
