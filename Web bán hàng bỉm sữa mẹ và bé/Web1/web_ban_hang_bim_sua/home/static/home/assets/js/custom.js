$(document).ready(function(){
	"use strict";
    
        /*==================================
* Author        : "ThemeSine"
* Template Name : Furniture E- commarce HTML Template
* Version       : 1.0
==================================== */




/*=========== TABLE OF CONTENTS ===========
1. Scroll To Top 
2. owl carousel
3. welcome animation support
4. cart close
======================================*/

    // 1. Scroll To Top 
		$(window).on('scroll',function () {
			if ($(this).scrollTop() > 600) {
				$('.return-to-top').fadeIn();
			} else {
				$('.return-to-top').fadeOut();
			}
		});
		$('.return-to-top').on('click',function(){
				$('html, body').animate({
				scrollTop: 0
			}, 1500);
			return false;
		});
	
	
	// 2. owl carousel
	
		// i. client (carousel)
		
			$('#client').owlCarousel({
				items:5,
				loop:true,
				smartSpeed: 1000,
				autoplay:true,
				dots:false,
				autoplayHoverPause:true,
				responsive:{
						0:{
							items:2
						},
						415:{
							items:3
						},
						600:{
							items:3

						},
						1200:{
							items:5
						}
					}
				});
				
				
				$('.play').on('click',function(){
					owl.trigger('play.owl.autoplay',[1000])
				})
				$('.stop').on('click',function(){
					owl.trigger('stop.owl.autoplay')
				})

		// ii.  testimonial-carousel
		
			$("#collection-carousel").owlCarousel({
				items: 1,
				autoplay: true,
				loop: true,
				dots:false,
				mouseDrag:true,
				nav:false,
				smartSpeed:1000,
				transitionStyle:"fade",
				animateIn: 'fadeIn',
				animateOut: 'fadeOutLeft'
				// navText:["<i class='fa fa-angle-left'></i>","<i class='fa fa-angle-right'></i>"]
			});


    // 3. welcome animation support

        $(window).load(function(){
        	$(".welcome-hero-txt h4,.welcome-hero-txt h2,.welcome-hero-txt p").removeClass("animated fadeInUp").css({'opacity':'0'});
            $(".welcome-hero-txt button").removeClass("animated fadeInDown").css({'opacity':'0'});
        });

        $(window).load(function(){
        	$(".welcome-hero-txt h4,.welcome-hero-txt h2,.welcome-hero-txt p").addClass("animated fadeInUp").css({'opacity':'0'});
            $(".welcome-hero-txt button").addClass("animated fadeInDown").css({'opacity':'0'});
        });


	// 4. cart-close
		$(".cart-close").click(function(){
			$(this).parents(".single-cart-list").fadeOut();
		});

});
$(document).ready(function () {
    updateCartTotal();

    // Xóa sản phẩm khỏi giỏ hàng khi nhấn vào dấu "X"
    $(".cart-close").on("click", function () {
        $(this).closest(".single-cart-list").remove();
        updateCartTotal();
    });

    function updateCartTotal() {
        let total = 0;
        $(".single-cart-list").each(function () {
            let priceText = $(this).find(".price").text().replace("$", "");
            let price = parseFloat(priceText);
            total += price;
        });

        // Cập nhật tổng tiền
        $(".total span").text(`Total: $${total.toFixed(2)}`);

        // Cập nhật số lượng sản phẩm trong badge giỏ hàng
        $(".badge-bg-1").text($(".single-cart-list").length);
    }
});
$(".add-to-cart-button").on("click", function () {
    // Thêm sản phẩm vào giỏ (giả sử bạn có logic thêm sản phẩm ở đây)
    
    updateCartTotal(); // Cập nhật lại tổng tiền sau khi thêm
});
$(document).ready(function () {
    let cart = JSON.parse(localStorage.getItem('cart')) || []; // Lưu cart vào localStorage

    // Hàm cập nhật giỏ hàng
    function updateCart() {
        // Xóa nội dung cũ
        $(".cart-list").empty();
        
        let totalPrice = 0;
        
        // Thêm từng item vào DOM
        cart.forEach(item => {
            const itemTotal = item.price * item.quantity;
            totalPrice += itemTotal;
            
            const itemHtml = `
                <li class="single-cart-list">
                    <a href="#" class="photo">
                        <img src="${item.image}" class="cart-thumb" alt="${item.name}">
                    </a>
                    <div class="cart-list-txt">
                        <h6><a href="#">${item.name}</a></h6>
                        <p>${item.quantity} x - <span class="price">${item.price.toLocaleString()} đ</span></p>
                    </div>
                    <div class="cart-close" data-id="${item.id}">
                        <span class="lnr lnr-cross"></span>
                    </div>
                </li>`;
            
            $(".cart-list").append(itemHtml);
        });

        // Cập nhật tổng tiền
        $(".total span").text(`Tổng cộng: ${totalPrice.toLocaleString()} đ`);
        
        // Cập nhật badge
        $(".badge-bg-1").text(cart.length);
        
        // Lưu vào localStorage
        localStorage.setItem('cart', JSON.stringify(cart));
    }

    // Thêm sản phẩm
    $(document).on('click', '.add-to-cart-button', function(e) {
        e.preventDefault();
        
        const product = {
            id: $(this).data('id'),
            name: $(this).data('name'),
            price: parseInt($(this).data('price')),
            image: $(this).data('image'),
            quantity: 1
        };
        
        // Kiểm tra đã có trong giỏ chưa
        const existingItem = cart.find(item => item.id === product.id);
        if (existingItem) {
            existingItem.quantity++;
        } else {
            cart.push(product);
        }
        
        updateCart();
    });

    // Xóa sản phẩm
    $(document).on('click', '.cart-close', function() {
        const productId = $(this).data('id');
        cart = cart.filter(item => item.id !== productId);
        updateCart();
    });

    // Khởi tạo giỏ hàng
    updateCart();
});
$(document).on("click", ".add-to-cart-button", function (e) {
    e.preventDefault(); // Ngăn trang load lại
    const product = {
        id: $(this).data("id"),
        name: $(this).data("name"),
        price: parseInt($(this).data("price")),
        image: $(this).data("image"),
        quantity: 1
    };

    let existingItem = cart.find(item => item.id === product.id);
    if (existingItem) {
        existingItem.quantity++;
    } else {
        cart.push(product);
    }

    updateCart();
});
