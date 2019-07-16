var TurndownService = require('turndown');
var stream = require('stream');

var html2md = new stream.Transform({
    decodeStrings: false, 
    encoding: 'utf-8', 
    transform: function (chunk, encoding, callback) {
        this.html += chunk;
        callback(null, '');
    }, 
    flush: function (callback) {
        var turndownService = new TurndownService();
        var md = turndownService.turndown(this.html);
        //文字化けしそうな空白文字を置換する
        md = md.replace(/[ \u00a0\u1680\u180e\u2000-\u200a\u2028\u2029\u202f\u205f\u3000\ufeff]/g , ' ' );
        this.push(md);
        callback(null);
    }
});
html2md.html = '';
html2md.on('error', function (err) {
    console.error(err);
    process.exit(1);
});

process.stdin.pipe(html2md).pipe(process.stdout);

