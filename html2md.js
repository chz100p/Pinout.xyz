const commandLineArgs = require('command-line-args');

const optionDefinitions = [
	  {
		      name: 'verbose',
		      alias: 'v',
		      type: Boolean
		    },
	  {
		      name: 'html',
		      alias: 'i',
		      type: String,
		    },
	  {
		      name: 'markdown',
		      alias: 'o',
		      type: String,
		    }
];
const options = commandLineArgs(optionDefinitions);

//console.log(options);

if (! options.html) {
	console.error("require '--html'");
	process.exit(1);
}


if (! options.markdown) {
	console.error("require '--markdown'");
	process.exit(1);
}

var fs = require('fs');
var TurndownService = require('turndown');

var turndownService = new TurndownService();

var html = fs.readFileSync(options.html, {encoding: 'utf-8'});
var md = turndownService.turndown(html);
//文字化けしそうな空白文字を置換する
md = md.replace(/[ \u00a0\u1680\u180e\u2000-\u200a\u2028\u2029\u202f\u205f\u3000\ufeff]/g , ' ' );
//console.log(md);
fs.writeFileSync(options.markdown, md);

