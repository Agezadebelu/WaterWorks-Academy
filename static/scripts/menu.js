document.querySelector('.md:hidden').addEventListener('click', function() {
    document.querySelector('.md:hidden + nav').classList.toggle('hidden');
    document.querySelector('.md:hidden + div').classList.toggle('hidden');
});
document.querySelector('.fixed.inset-0.bg-opacity-50').addEventListener('click', function() {
    document.querySelector('.md:hidden + nav').classList.toggle('hidden');
    document.querySelector('.md:hidden + div').classList.toggle('hidden');
});