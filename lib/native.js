/*
 * native.js
 * Copyright (C) 2014 tox <tox@rootkit>
 *
 * Distributed under terms of the MIT license.
 */


var env = process.env.PDFUTILS_ENV;
module.exports = require('../build/'+env+'/pdfutils');