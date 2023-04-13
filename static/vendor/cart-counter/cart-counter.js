document.getElementById('add').addEventListener('click', function () {
  var quantity = document.getElementById('quantity');
  var current = parseInt(quantity.innerHTML);
  quantity.innerHTML = current + 1;
});

document.getElementById('remove').addEventListener('click', function () {
  var quantity = document.getElementById('quantity');
  var current = parseInt(quantity.innerHTML);
  if (current > 1) {
    quantity.innerHTML = current - 1;
  }
});

function changeImage(element) {

    var main_prodcut_image = document.getElementById('main_product_image');
    main_prodcut_image.src = element.src;
    

}