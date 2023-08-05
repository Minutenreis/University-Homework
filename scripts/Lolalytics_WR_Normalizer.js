// ==UserScript==
// @name Lolalytics WR Normalizer
// @match https://lolalytics.com/lol/tierlist/*
// @run-at document-idle
// ==/UserScript==

var fireOnHashChangesToo = true;
var pageURLCheckTimer = setInterval(
    function () {
        if (this.lastPathStr !== location.pathname
            || this.lastQueryStr !== location.search
            || (fireOnHashChangesToo && this.lastHashStr !== location.hash)
        ) {
            this.lastPathStr = location.pathname;
            this.lastQueryStr = location.search;
            this.lastHashStr = location.hash;
            setTimeout(main, 250);
        }
    }
    , 111
);

function main() {

    //get average Winrate of Elo Bracket
    avgWRText = document.getElementsByClassName("Analysed_wrapper__o86fv")[0].innerText;
    avgWRArr = avgWRText.split("\n")[0].split(" ")
    avgWR = avgWRArr[avgWRArr.length - 1].slice(0, -2);

    //normalize Champion WR
    tableData = document.getElementsByClassName("TierList_list__j33gd")[0].children
    for (var div of tableData) {
        index = div.childNodes[0].className.startsWith("ListRow_rank") ? 5 : 4;
        WR = Math.round((div.childNodes[index].innerText.split("\n")[0] - avgWR + 50) * 100) / 100
        ogStat = div.childNodes[index].innerText.split("\n")
        div.childNodes[index].innerHTML = '<div> ' + WR + '<\div><div class="ListRow_wrdelta__dKTY+">' + ogStat[0] + "<br />" + ogStat[1] + "</div>"
        //coloring
        if (WR > 50.5) {
            div.childNodes[index].style["color"] = "green"
        } else if (WR > 49.5) {
            div.childNodes[index].style["color"] = "yellow"
        } else {
            div.childNodes[index].style["color"] = "red"
        }
    }
}