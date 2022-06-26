let buttonZoomIn = document.createElement('button');
let buttonZoomOut = document.createElement('button');
let buttonZoomReset = document.createElement('button');
buttonZoomIn.innerHTML = "Zoom In";
buttonZoomOut.innerHTML = "Zoom Out";
buttonZoomReset.innerHTML = "Zoom Reset";
let zoomDefault = 0.6;
let objsvg = document.createElement('object');
let docsvg;
let lines;
let dots;
let details = document.getElementById('details');
let csv;
let IDX_Type = 0;
let IDX_Name = 1;
let IDX_Info = 15;

objsvg.setAttribute('type', 'image/svg+xml');
objsvg.setAttribute('data', 'gnuclad/gnuclad.svg');
document.body.appendChild(buttonZoomIn);
document.body.appendChild(buttonZoomOut);
document.body.appendChild(buttonZoomReset);
document.body.appendChild(objsvg);

function display_details(event) {
    // get project name from event
    let proj = event.target.id;
    if (event.target.tagName === 'path') {
        proj = proj.substring(7);
    }
    else { // tagName === 'circle'
        proj = proj.substring(6);
    }
    proj = proj.replaceAll('__', ' ');

    let content = '';
    for (let row of csv.data) {
        if (row[IDX_Type] === "N" && row[IDX_Name] === proj) {
            for (let i = IDX_Name; i <= IDX_Info; i++) {
                content += csv.data[0][i];
                content += ': ';
                content += row[i];
                content += '\n';
            }
            break;
        }

    }
    details.style.visibility = 'visible';
    details.style.top = event.pageY + objsvg.offsetTop + 10 + 'px';
    details.style.left = event.pageX + objsvg.offsetLeft + 'px';
    details.textContent = content;
}

function undisplay_details(event) {
    details.style.visibility = 'hidden';
}

function after_load_csv(results) {
    lines.forEach(line => {
        line.addEventListener('mouseover', display_details, false);
    });
    dots.forEach(dot => {
        dot.addEventListener('mouseover', display_details, false);
    });
    docsvg.querySelector('#layer_background').addEventListener('click', undisplay_details, false);
    csv = results;
}

function after_load_svg() {
    docsvg = objsvg.contentDocument;
    docsvg.children[0].style.zoom = zoomDefault;
    docsvg.children[0].style["-moz-transform"] = "scale("+zoomDefault+")";
    docsvg.children[0].style["transform-origin"] = "top left";

    buttonZoomIn.addEventListener('click', (event) => {
        let zoomCurrent = parseFloat(docsvg.children[0].style.zoom);
        zoomCurrent *= 1.1;
        docsvg.children[0].style.zoom = zoomCurrent;
        docsvg.children[0].style["-moz-transform"] = "scale("+zoomCurrent+")";
    });
    buttonZoomOut.addEventListener('click', (event) => {
        let zoomCurrent = parseFloat(docsvg.children[0].style.zoom);
        zoomCurrent *= 0.9;
        docsvg.children[0].style.zoom = zoomCurrent;
        docsvg.children[0].style["-moz-transform"] = "scale("+zoomCurrent+")";
    });
    buttonZoomReset.addEventListener('click', (event) => {
        docsvg.children[0].style.zoom = zoomDefault;
        docsvg.children[0].style["-moz-transform"] = "scale("+zoomDefault+")";
    });

    lines = docsvg.querySelectorAll('[id^=__line]');
    dots = docsvg.querySelectorAll('[id^=__dot]');
    Papa.parse('runXonY.csv', {
        download: true,
        complete: after_load_csv
    });
}

objsvg.addEventListener('load', after_load_svg);
