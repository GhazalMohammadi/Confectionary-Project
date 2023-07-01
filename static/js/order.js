// "use strict";

// $("#shoppingBtn").click(function (e) {
//   e.preventDefault();
//   var product_id = $("#prod_id").val();
//   var product_qty = $("#quantityValue").val();
//   var product_unit = $("#unitValue").val();
//   var token = $("input[name=csrfmiddlewaretoken]").val();

//   $.ajax({
//     method: "POST",
//     url: "/add_to_cart",
//     data: {
//       product_id: product_id,
//       product_qty: product_qty,
//       product_unit: product_unit,
//       csrfmiddlewaretoken: token,
//     },
//     success: function (response) {
//       console.log(response);
//     },
//   });
// });
