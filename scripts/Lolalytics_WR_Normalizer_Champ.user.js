// ==UserScript==
// @name Lolalytics WR Normalizer Champs & Delta2 Calc
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
    normalizeChampWR()
    // calculateDelta2() todo: find a way to load the matchup data
}

function normalizeChampWR() {
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

function calculateDelta2() {
    const lane = getSelectedLane()
    const laneIndex = laneToIndex(lane)
    const laneMatchups = document.getElementsByClassName("CountersPanel_counters__U8zc5")[laneIndex].children[1].children[0].children
    const delta2SquaredScaled = Array.from(laneMatchups, (matchup) => (matchup.children[3].innerText ** 2 * matchup.children[4].innerText / 100))
    const delta2SquaredScaledSum = delta2SquaredScaled.reduce((a, b) => a + b, 0)
    StatContainer = document.getElementsByClassName("ChampionStats_stats__26e3l")[0].children
    if (!StatContainer[3].marked) {
        StatContainer[3].marked = true
        const pickrate = StatContainer[3].childNodes[0].innerHTML
        console.log(pickrate)
        StatContainer[3].childNodes[0].innerHTML = '<div> ' + pickrate + '<\div><div style="font-size: 8px; color: grey">' + Math.round(delta2SquaredScaledSum * 100) / 100 + "</div>"
    }
}

/**
 * get the selected lane
 * @returns "top" | "jungle" | "middle" | "bottom" | "support"
 */
function getSelectedLane() {
    const classSymbol = document.getElementsByClassName("LanePicker_inneractive__bEJGw")[0]
    return classSymbol.children[0].alt
}

function laneToIndex(lane) {
    switch (lane) {
        case "top":
            return 0
        case "jungle":
            return 1
        case "middle":
            return 2
        case "bottom":
            return 3
        case "support":
            return 4
        default:
            return -1
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