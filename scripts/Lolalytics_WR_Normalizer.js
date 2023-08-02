// ==UserScript==
// @name Lolalytics WR Normalizer
// @match https://lolalytics.com/lol/tierlist/*
// @run-at document-idle
// ==/UserScript==

setTimeout(main, 250)

function main() {
    marker = "_"
    avgWRText = document.getElementsByClassName("Analysed_wrapper__o86fv")[0].innerText;
    if (!avgWRText.startsWith(marker)) {
        avgWRArr = avgWRText.split("\n")[0].split(" ")
        avgWR = avgWRArr[avgWRArr.length - 1].slice(0, -2);
        console.log(avgWR)
        //mark WR for site selection
        document.getElementsByClassName("Analysed_wrapper__o86fv")[0].innerHTML = marker + document.getElementsByClassName("Analysed_wrapper__o86fv")[0].innerHTML

        tableData = document.getElementsByClassName("TierList_list__j33gd")[0].children
        for (var div of tableData) {
            index = div.childNodes[0].className.startsWith("ListRow_rank") ? 5 : 4;
            WR = Math.round((div.childNodes[index].innerText.split("\n")[0] - avgWR + 50) * 100) / 100
            ogStat = div.childNodes[index].innerText.split("\n")
            div.childNodes[index].innerHTML = '<div> ' + WR + '<\div><div class="ListRow_wrdelta__dKTY+">' + ogStat[0] + "<br />" + ogStat[1] + "</div>"
            if (WR > 50.5) {
                div.childNodes[index].style["color"] = "green"
            } else if (WR > 49.5) {
                div.childNodes[index].style["color"] = "yellow"
            } else {
                div.childNodes[index].style["color"] = "red"
            }
        }
    }
}