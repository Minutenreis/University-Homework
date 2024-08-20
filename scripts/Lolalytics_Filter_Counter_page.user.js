// ==UserScript==
// @name Lolalytics Filter Counters
// @match https://lolalytics.com/lol/*/counters/*
// @run-at document-idle
// ==/UserScript==

let cutoff = 1000; // minimum games played
let timeout = 250; // time to wait before executing function after button click

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
    filter()
    btn = document.querySelector("[q\\:id='3q']");
    btn.onclick = filterAfterTimeoutOnce;
}

let first = true;
function filterAfterTimeoutOnce() {
    if (first) {
        first = false;
        setTimeout(filter, timeout);
    }
}

function filter() {
    let counters = document.querySelectorAll("[q\\:key='yJ_1']")[2];
    let champSpans = counters.children[0].children[1].children;
    console.log(champSpans.length);
    for (const champSpan of champSpans) {
        console.log(champSpan.tagName);
        if (champSpan.tagName !== "SPAN") {
            continue;
        }
        let gamesText = champSpan.children[0].children[0].children[0].children[5].innerText;
        let games = Number(gamesText.slice(0, -6).replace(/\,|\./g, ""));
        if (games < cutoff) {
            champSpan.style.display = "none";
        } else {
            champSpan.style.display = "";
        }
    }
}