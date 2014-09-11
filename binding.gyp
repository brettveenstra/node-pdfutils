{
	"targets": [{
		"target_name": "pdfutils",
		"sources": [
			"src/PdfController.cpp",
			"src/PdfDocumentController.cpp",
			"src/PdfDocument.cpp",
			"src/PdfEngine.cpp",
			"src/PdfEngineFactory.cpp",
			"src/PdfPage.cpp",
			"src/PdfPageController.cpp",
			"src/worker/PdfExportPageWorker.cpp",
			"src/worker/PdfSaveWorker.cpp",
			"src/init.cpp",
		],
		"include_dirs" : [
			"<!(node -e \"require('nan')\")"
		],
	}, {
		"target_name": "pdfiumEngine",
		"sources": [
			"src/PdfDocument.cpp",
			"src/PdfEngine.cpp",
			"src/PdfEngineFactory.cpp",
			"src/PdfPage.cpp",
			"src/pdfium/PdfiumEngine.cpp",
		],
		"include_dirs" : [
			"<!(node -e \"require('nan')\")"
		],
		"cflags": [
			"<!@(pkg-config --cflags poppler-glib)"
		],
		"libraries": [
			"<!@(pkg-config --libs poppler-glib)"
		]
	}, {
		"target_name": "popplerEngine",
		"sources": [
			"src/PdfDocument.cpp",
			"src/PdfEngine.cpp",
			"src/PdfEngineFactory.cpp",
			"src/PdfPage.cpp",
			"src/poppler/PopplerEngine.cpp",
		],
		"include_dirs" : [
			"<!(node -e \"require('nan')\")"
		],
		"cflags": [
			"<!@(pkg-config --cflags poppler-glib)"
		],
		"libraries": [
			"<!@(pkg-config --libs poppler-glib)"
		]
	}]
}
