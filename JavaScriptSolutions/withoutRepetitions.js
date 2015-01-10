var WithoutRepetitions = function(sentenceCheck){
    for(i=0; i<sentenceCheck.length; i++){
        var newSentence='';
        for(j=0; j<sentenceCheck.length; j++){
            if(sentenceCheck[j]!==sentenceCheck[j+1]){
            newSentence+=sentenceCheck[j];
            }
        }
        return newSentence;
    }
};

var fs  = require("fs");
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line !== "") {
        var result = WithoutRepetitions(line);
        console.log(result);
    }
});
