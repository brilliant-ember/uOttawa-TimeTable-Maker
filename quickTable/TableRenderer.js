'use strict';

//
// This function accepts an array containing all possible valid course schedules
// and returns an array formatted html used to render each timetable
//
// data has the following format
// [timetable, timetable, ...]
// where timetable = [[period, metadata], [period, metadata], ... ]
// where period is an integer 1 to 45
// and metadata is an object containing popover info for that period
//
// second argument is a look up object [courseName] -> cssClass
var TableRenderer = function(data, cssClassLookup){

    var rtn = [];
    data.forEach((timetable, t) => {

        var table = $('<table>');
        table.attr('id', 'timetable-' + t);

        for(var i=0; i<9; i++){ // nine rows (periods)

            var row = $("<tr>");

            for(var j=0; j<5; j++){ // five cols (days)
                var col = $("<td>");
                col.addClass("cell");

                //
                // check for period in timetable
                //
                timetable.forEach((period, p) => {

                    var absPeriod = 9 * j + i + 1; // 9 * column + row

                    if( period[0] == absPeriod ){

                        var cName = period[1].courseName;
                        col.addClass(" " + cssClassLookup[cName]);
                        col.addClass(" " + period[1].courseName);

                        var content = "";
                        for(let key in period[1]){
                            var value = period[1][key];
                            content += key + ": " + value + "<br>";
                        }

                        col.attr({
                            "data-toggle": "popover",
                            //"data-trigger": "focus",
                            "title": "Period Details",
                            "data-content": content,
                            "tabindex": "0",
                            "data-html": "true",
                        });

                    }
                });

                row.append(col);
            }
            table.append(row);
        }
        rtn.push(table);

    }); // data.forEach ends

    return rtn; // array or jQuery objects representing timetables
};
