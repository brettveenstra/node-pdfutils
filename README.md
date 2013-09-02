[![Flattr this git repo](http://api.flattr.com/button/flattr-badge-large.png)](https://flattr.com/submit/auto?user_id=Gottox&url=https://github.com/Gottox/node-pdfutils&title=node-pdfutils&language=&tags=github&category=software)

PDF Utils for node
==================

This library contains tools for analysing and converting PDF files. You can
get metadata, extract text, render pages to svg or png, all with our beloved
asynchronous programming style.

It is planed to support extracting links from the document and create ImageMaps
([You remember them, don't you?](http://en.wikipedia.org/wiki/Image_map)) on
the fly. Also pdfutils should support password locked files.
But that's still on the todo.

The library is currently beta. This means it has incomplete error handling and
it lacks a testing suite.

Installation
------------

To install pdfutils you have to install libpoppler-glib first.

Using Debian execute:

	apt-get install libpoppler-glib-dev libpoppler-glib8 libcairo2-dev libcairo2

Using MacOS and Macports:

	port install poppler
	
or if you prefere brew:

	brew install poppler --with-glib
	PKG_CONFIG_PATH=/usr/X11/lib/pkgconfig npm install pdfutils

Then install pdfutils

	npm install pdfutils

Usage
-----

See this very basic example:

	var pdfutils = require('pdfutils').pdfutils;

	pdfutils("document.pdf", function(err, doc) {
		doc[0].asPNG({maxWidth: 100, maxHeight: 100}).toFile("firstpage.png");
	});

3sloc to generate thumbnails of PDFs. Awesome!

Here a bit more documentation:

### pdfutils(source, callback)

this function is a factory for Documents

arguments:

 * __source__: can be a Buffer or a String. If it's a string, read from the
  file. If it's a buffer, treat the buffer content as in-memory PDF.
  Please make sure to not change the buffer while using it by pdfutils!
 * __callback(err, doc)__: a callback with the following arguments:
   * _err_: an error string when the pdf couldn't be loaded successfully,
     otherwise `null`
   * _doc_: an instance of `Document` when the pdf is loaded successfully,
     otherwise `undefined`

### Class PDFDocument

This class is generated by pdfutils(source, callback) described above.

members:

 * __0, 1, 2, 3, 4, ... , n__ instances of the `Page`s contained by the
  Document. See description of `Page` below
 * __length__: number of `Page`s in a document
 * __author__: the author of the document or `null` if not known
 * __creationDate__: the creation date as integer since 1970-01-01
 * __creator__: creator of the document or null if unknown
 * __format__: exact format of this PDF file or null if unknown
 * __keywords__: keywords of the document as string or null if unknown
 * __linearized__: true if document is [linearized](http://www.citationsoftware.com/faqPDFlinearization.htm),
   otherwise false
 * __metadata__: Metadata as string
 * __modDate__: last modification of pdf as integer since 1970-01-01
 * __pageLayout__: the layout of the pages. Can be on of the following strings or null if unknown:
   * _singlePage_
   * _oneColumn_
   * _twoColumnLeft_
   * _twoColumnRight_
   * _twoPageLeft_
   * _twoPageRight_
 * __pageMode__: the suggested viewing mode of a page. Can be one of the following strings or null if unkown:
   * _none_
   * _useOutlines_
   * _useThumbs_
   * _fullscreen_
   * _useOc_
   * _useAttachments_
 * __permissions__: the permissions of this document. Is an object with the following members:
   * _print_: whether the user is allowed to print
   * _modify_: whether the user is allowed to modify the document
   * _copy_: whether the user is allowed to take copies of this document
   * _notes_: whether the user is allowed to make notes
   * _fillForm_: whether the user is allowed to fill out forms
 * __producer__: producer of a document or null if unknown
 * __subject__: subject of this document or null if unknown
 * __title__: title of the document or null if unknown

### Class PDFPage

This class represents a page of a document

members:

 * __width__: width of the document
 * __height__: width of the document
 * __index__: number of this page.
 * __label__: label of this page or null if no label was defined.
 * __links__: array containing links of a page
 * __asSVG(opts)__: returns an instance of PageJob described below, opts is an
   optional argument with an Object with the following optional fields:
   * _maxWidth_: maximal width of the resulting SVG in px.
   * _minWidth_: minimal width of the resulting SVG in px.
   * _maxHeight_: maximal height of the resulting SVG in px.
   * _minHeight_: minimal height of the resulting SVG in px.
   * _width_: the width of the resulting SVG in px. Overwrites minWidth and
     maxWidth.
   * _height_: the height of the resulting SVG in px. Overwrites minHeight and
     maxHeight.
 * __asPDF(opts)__: returns an instance of PageJob described below, opts is an
   optional argument with an Object with the following optional fields:
   * _maxWidth_: maximal width of the resulting PDF in pt.
   * _minWidth_: minimal width of the resulting PDF in pt.
   * _maxHeight_: maximal height of the resulting PDF in pt.
   * _minHeight_: minimal height of the resulting PDF in pt.
   * _width_: the width of the resulting PDF in pt. Overwrites minWidth and
     maxWidth.
   * _height_: the height of the resulting PDF in pt. Overwrites minHeight and
     maxHeight.
 * __asPNG(opts)__: returns an instance of PageJob described below, opts is an
   optional argument with an Object with the following optional fields:
   * _maxWidth_: maximal width of the resulting PNG in px
   * _minWidth_: minimal width of the resulting PNG in px
   * _maxHeight_: maximal height of the resulting PNG in px
   * _minHeight_: minimal height of the resulting PNG in px
   * _width_: the width of the resulting PNG in px. Overwrites minWidth and
     maxWidth.
   * _height_: the height of the resulting PNG in px. Overwrites minHeight and
     maxHeight.
 * __asText(opts)__: returns an instance of PageJob described below. opts is an
   optional argument with an Object, which is currently ignored.

### Class PDFPageJob

This class inherits [Stream](http://nodejs.org/api/stream.html). It handles
converting a Page (described above) to SVG, PNG or Text

members:

 * __links__: array containing links of a page, translated to fit the output page.

events:

 * __data__: emitted when a new chunk of the converted file is available
 * __end__: emitted when the file is successfully converted
 * __error__: emitted when the file cannot be converted. Is not implemented yet.

members:

 * toFile(path, \[options\]): writes a page to the file in the desired format.
 * see [Stream](http://nodejs.org/api/stream.html) for further members. 

License
-------

This module is licensed under GPL.
