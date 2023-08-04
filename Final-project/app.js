const events = document.querySelectorAll(".event");

function isElementInViewport(el) {
    const rect = el.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

function fadeInElements() {
    events.forEach((event) => {
        if (isElementInViewport(event)) {
            event.classList.add("visible");
        }
    });
}

window.addEventListener("scroll", fadeInElements);