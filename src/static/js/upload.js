const fileInput = document.getElementById('file');
const dropArea = document.getElementById('drop-area');

fileInput.addEventListener('change', function () {
    const form = this.closest('form');
    form.submit();
});

dropArea.addEventListener('dragover', function (e) {
    e.preventDefault();
    dropArea.classList.add('drag-over');
});

dropArea.addEventListener('dragleave', function () {
    dropArea.classList.remove('drag-over');
});

dropArea.addEventListener('drop', function (e) {
    e.preventDefault();
    dropArea.classList.remove('drag-over');
    
    fileInput.files = e.dataTransfer.files;

    const form = fileInput.closest('form');
    form.submit();
});