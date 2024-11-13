const container = document.querySelector('.section-notes');
let currentIndex = 0;

function scrollToNext() {
    const items = container.querySelectorAll('.note');
    if (currentIndex < items.length - 1) {
        currentIndex++;
    } else {
        currentIndex = 0; // Optional: loop back to start
    }
    items[currentIndex].scrollIntoView({ behavior: 'smooth', inline: 'start' });
}

function scrollToPrevious() {
    const items = container.querySelectorAll('.note');
    if (currentIndex > 0) {
        currentIndex--;
    } else {
        currentIndex = items.length - 1; // Optional: loop back to end
    }
    items[currentIndex].scrollIntoView({ behavior: 'smooth', inline: 'start' });
}
