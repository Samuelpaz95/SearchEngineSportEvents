document.getElementById('searcher').addEventListener('focusin', (event) => {
    event.target.classList.add('expanded');
});
document.getElementById('searcher').addEventListener('focusout', (event) => {
    event.target.classList.remove('expanded');
});