// ==UserScript==
// @name Lolalytics WR Normalizer Champs
// @match https://lolalytics.com/lol/*/build/*
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
    console.log("test")

    avgWRText = document.getElementsByClassName("Analysed_wrapper__o86fv")[0].innerText;
    avgWRArr = avgWRText.split("\n")[0].split(" ")
    avgWR = avgWRArr[avgWRArr.length - 1].slice(0, -2);

    //normalize WR of champ
    StatContainer = document.getElementsByClassName("ChampionStats_stats__26e3l")[0].children
    if (!StatContainer[0].marked) {
        StatContainer[0].marked = true
        ogWR = StatContainer[0].childNodes[0].innerText.slice(0, -1)
        //shifted Normalization (ogWR - (avgWR - 50))
        WR = Math.round((ogWR - avgWR + 50) * 100) / 100
        StatContainer[0].childNodes[0].innerText = WR
        //coloring
        color = getColor(WR)
        StatContainer[0].childNodes[0].innerHTML = '<div style="color:' + color + '"> ' + WR + '<\div><div style="font-size: 8px; color: grey">' + ogWR + "</div>"
    }
}

function getColor(WR) {
    high = { r: 0, g: 255, b: 0 }
    mid = { r: 230, g: 220, b: 215 }
    low = { r: 255, g: 0, b: 0 }

    if (WR > 55) {
        return toRgb(high)
    } else if (WR > 50) {
        return toRgb(getGradientColor((WR - 50) / 5, high, mid))
    } else if (WR > 45) {
        return toRgb(getGradientColor((WR - 45) / 5, mid, low))
    } else {
        return toRgb(low)
    }
}

function getGradientColor(percentage, high, low) {
    var r = high.r * percentage + low.r * (1 - percentage);
    var g = high.g * percentage + low.g * (1 - percentage);
    var b = high.b * percentage + low.b * (1 - percentage);
    return { r: r, g: g, b: b };
}

function toRgb(color) {
    return "rgb(" + color.r + "," + color.g + "," + color.b + ")"
}