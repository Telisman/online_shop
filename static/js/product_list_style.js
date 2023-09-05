// product_list_style.js

document.addEventListener("DOMContentLoaded", function () {
    // Get all the "Toggle Details" buttons
    const toggleButtons = document.querySelectorAll(".toggle-details-button");

    // Add click event listeners to each "Toggle Details" button
    toggleButtons.forEach((button) => {
        button.addEventListener("click", function () {
            const productDetails = this.nextElementSibling;
            productDetails.classList.toggle("show-details");
        });
    });

    // Add a fade-in animation to product list items
    const productItems = document.querySelectorAll("ul li");

    productItems.forEach((item, index) => {
        item.style.opacity = 0;
        item.style.transform = "translateY(20px)"; // Start with a slight vertical offset

        // Use setTimeout for staggered animations
        setTimeout(() => {
            item.style.transition = "opacity 0.5s ease-in-out, transform 0.5s ease-in-out";
            item.style.opacity = 1;
            item.style.transform = "translateY(0)";
        }, index * 100); // Delay each item's animation
    });
});
