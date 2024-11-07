const printedTooltips = new Set();
const printedTexts = new Set();
function checkTooltipContent() {
    const tooltip = document.querySelector('.custom-tooltip');
    if (tooltip && !printedTooltips.has(tooltip) && tooltip.innerHTML.trim() !== "") {
        //console.log(tooltip.outerHTML);
        printedTooltips.add(tooltip);
        const paragraphs = tooltip.querySelectorAll('p');
        paragraphs.forEach((p) => {
            const text = p.innerText.trim();
            if (!printedTexts.has(text)) {
                console.log(text);
                printedTexts.add(text);
            }
        });
    }
}
const observer = new MutationObserver((mutationsList) => {
    mutationsList.forEach((mutation) => {
        mutation.addedNodes.forEach((node) => {
            if (node.nodeType === 1 && node.classList.contains('custom-tooltip')) {
                // Tooltip eklendiğinde içerik kontrolüne başla
                const intervalId = setInterval(() => {
                    checkTooltipContent();
                    if (printedTooltips.has(node)) {
                        clearInterval(intervalId);
                    }
                }, 10);
            }
        });
    });
});
observer.observe(document.body, { childList: true, subtree: true });

function moveMouseAcrossDiv() {
    const watermarkDiv = document.querySelector('.recharts-wrapper.watermark');
    if (!watermarkDiv) {
        console.error('Div bulunamadı!');
        return;
    }

    const rect = watermarkDiv.getBoundingClientRect();
    const width = rect.width;
    const steps = 100;
    const interval = 20;

    for (let i = 0; i <= steps; i++) {
        setTimeout(() => {
            const x = rect.left + (i / steps) * width;
            const y = rect.top + rect.height / 2;
            const mouseEvent = new MouseEvent('mousemove', {
                bubbles: true,
                clientX: x,
                clientY: y
            });
            watermarkDiv.dispatchEvent(mouseEvent); // Olayı div'e gönder
        }, i * interval);
    }
}

moveMouseAcrossDiv();
