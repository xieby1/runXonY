let buttonZoomIn = document.getElementById('buttonZoomIn');
let buttonZoomOut = document.getElementById('buttonZoomOut');
let buttonZoomReset = document.getElementById('buttonZoomReset');
let zoomInputBox = document.getElementById('zoomInputBox');
let buttonZoomSet = document.getElementById('buttonZoomSet');
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

function get_default_zoom() {
    zoom = objsvg.parentElement.clientWidth / docsvg.children[0].getBBox().width;
    return zoom;
}

function set_zoom(zoom) {
    // only keep 2 decimal
    zoom = zoom.toFixed(2);
    docsvg.children[0].style.zoom = zoom;
    docsvg.children[0].style["-moz-transform"] = "scale("+zoom+")";
    zoomInputBox.value = zoom;
}

function after_load_svg() {
    docsvg = objsvg.contentDocument;
    // for debug
    objsvg.setAttribute("id", "runXonYsvg");

    // fit width
    docsvg.children[0].style["transform-origin"] = "top left";
    set_zoom(get_default_zoom());

    buttonZoomIn.addEventListener('click', (event) => {
        let zoomCurrent = parseFloat(docsvg.children[0].style.zoom);
        zoomCurrent *= 1.1;
        set_zoom(zoomCurrent);
    });
    buttonZoomOut.addEventListener('click', (event) => {
        let zoomCurrent = parseFloat(docsvg.children[0].style.zoom);
        zoomCurrent *= 0.9;
        set_zoom(zoomCurrent);
    });
    buttonZoomReset.addEventListener('click', (event) => {
        set_zoom(get_default_zoom());
    });
    buttonZoomSet.addEventListener('click', (event) => {
        let zoomCurrent = parseFloat(zoomInputBox.value);
        set_zoom(zoomCurrent);
    });

    lines = docsvg.querySelectorAll('[id^=__line]');
    dots = docsvg.querySelectorAll('[id^=__dot]');
    Papa.parse('runXonY.csv', {
        download: true,
        complete: after_load_csv
    });
}

objsvg.addEventListener('load', after_load_svg);
