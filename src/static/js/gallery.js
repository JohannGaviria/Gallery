var elem = document.querySelector('.grid-container');
imagesLoaded(elem, () => {
    var msnry = new Masonry(elem, {
        itemSelector: '.grid-item',
        columnWidth: 230,
        gutter: 20,
        isFitWidth: true
    });
});

//-------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------

function openModal(imageSrc) {
    var modal = document.getElementById("myModal");
    var modalImage = document.getElementById("modalImage");
    
    modal.style.display = "block";
    modalImage.src = imageSrc;
}

function closeModal() {
    var modal = document.getElementById("myModal");
    modal.style.display = "none";
}

var images = document.querySelectorAll(".grid-item");

images.forEach(function (image) {
    image.addEventListener("click", function () {
        openModal(image.src);
    });
});

//-------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------

var modalImage = document.getElementById("modalImage");
var currentImageIndex = 0;

function changeImage(offset) {
    currentImageIndex += offset;
    if (currentImageIndex < 0) {
        currentImageIndex = images.length - 1;
    } else if (currentImageIndex >= images.length) {
        currentImageIndex = 0;
    }
    modalImage.src = images[currentImageIndex].src;
}
