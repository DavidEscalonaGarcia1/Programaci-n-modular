// ==UserScript==
// @name         Copy URL Button
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  Afegeix un botó per copiar l'URL actual al porta-retalls
// @author       AI Assistant
// @match        *://*/*
// @grant        GM_setClipboard
// ==/UserScript==

(function() {
    'use strict';

    // Crear el botó
    const btn = document.createElement('button');
    btn.textContent = 'Copy URL';
    btn.style.position = 'fixed';
    btn.style.bottom = '10px';
    btn.style.right = '10px';
    btn.style.padding = '10px';
    btn.style.zIndex = 10000;
    btn.style.backgroundColor = '#007bff';
    btn.style.color = '#fff';
    btn.style.border = 'none';
    btn.style.borderRadius = '5px';
    btn.style.cursor = 'pointer';
    btn.style.fontSize = '14px';

    // Funció per copiar l'URL actual
    btn.addEventListener('click', () =&gt; {
        if (typeof GM_setClipboard !== 'undefined') {
            GM_setClipboard(window.location.href);
            alert('URL copied to clipboard!');
        } else {
            navigator.clipboard.writeText(window.location.href).then(() =&gt; {
                alert('URL copied to clipboard!');
            }).catch(() =&gt; {
                alert('Failed to copy URL.');
            });
        }
    });

    document.body.appendChild(btn);
})();