document.addEventListener("DOMContentLoaded", function() {
    var postImage = document.querySelector(".post-image");
        postImage.onclick = function() {
            this.classList.toggle("large");
        };
});