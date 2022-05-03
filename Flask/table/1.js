var array = [];
var matrix = [];
var i = 0;
$("table tr td").each(
    function (index, val) {
        array.push($(val).text());
        i++;
        if (i % 3 == 0) {
            matrix.push(
                array
            );
            array = [];
        }
    }
)