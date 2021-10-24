let objsvg = document.createElement('object');
let docsvg;
let lines;
let dots;
let details = document.getElementById('details');
let csv;

objsvg.setAttribute('type', 'image/svg+xml');
// objsvg.setAttribute('data', 'gnuclad.svg');
objsvg.setAttribute('data', 'gnuclad.svg');
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
        if (row[0] === proj) {
            for (let i = 0; i < csv.data[0].length; i++) {
                if (csv.data[0][i] === '') {
                    break;
                }

                content += csv.data[0][i];
                content += ': ';
                content += row[i];
                content += '\n';
            }
            break;
        }

    }
    details.style.visibility = 'visible';
    details.style.top = event.pageY + 10 + 'px';
    details.style.left = event.pageX + 'px';
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
    lines = docsvg.querySelectorAll('[id^=__line]');
    dots = docsvg.querySelectorAll('[id^=__dot]');
    Papa.parse('runXonY.csv', {
        download: true,
        complete: after_load_csv
    });
}

objsvg.addEventListener('load', after_load_svg);
