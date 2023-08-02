// ==UserScript==
// @name Lolalytics WR Normalizer Champs
// @match https://lolalytics.com/lol/*/build/*
// @run-at document-idle
// ==/UserScript==

setTimeout(main, 250)
console.log("test")

function main() {
    marker = "_"
    avgWRText = document.getElementsByClassName("Analysed_wrapper__o86fv")[0].innerText;
    if (!avgWRText.startsWith(marker)) {
        avgWRArr = avgWRText.split("\n")[0].split(" ")
        avgWR = avgWRArr[avgWRArr.length - 1].slice(0, -2);
        //mark WR for site selection
        document.getElementsByClassName("Analysed_wrapper__o86fv")[0].innerHTML = marker + document.getElementsByClassName("Analysed_wrapper__o86fv")[0].innerHTML


        StatContainer = document.getElementsByClassName("ChampionStats_stats__26e3l")[0].children
        ogWR = StatContainer[0].childNodes[0].innerText.slice(0, -1)
        WR = Math.round((ogWR - avgWR + 50) * 100) / 100
        StatContainer[0].childNodes[0].innerText = WR
        color = "grey"
        if (WR > 50.5) {
            color = "green"
        } else if (WR > 49.5) {
            color = "yellow"
        } else {
            color = "red"
        }
        console.log(WR)
        StatContainer[0].childNodes[0].innerHTML = '<div style="color:' + color + '"> ' + WR + '<\div><div style="font-size: 8px; color: grey">' + ogWR + "</div>"
    }
}