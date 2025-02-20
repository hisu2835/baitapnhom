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
    "use strict";

    // Lấy giỏ hàng từ localStorage
    let cart = JSON.parse(localStorage.getItem("cart")) || [];

    function updateCart() {
        console.log("🔄 Bắt đầu cập nhật giỏ hàng...");
    
        $(".cart-list").empty();
        let totalPrice = 0;
        let totalQuantity = 0; // Thêm biến tổng số lượng
    
        if (cart.length === 0) {
            console.log("⚠️ Giỏ hàng trống! Không hiển thị tổng tiền.");
            $(".badge-bg-1").text(0);
            return;
        }
    
        cart.forEach(item => {
            const itemTotal = item.price * item.quantity;
            totalPrice += itemTotal;
            totalQuantity += item.quantity; // Cộng dồn số lượng sản phẩm
    
            console.log(`🛍️ Sản phẩm: ${item.name} | Số lượng: ${item.quantity} | Tổng: ${itemTotal.toLocaleString()} đ`);
    
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
    
        console.log("💰 Tổng tiền cuối cùng:", totalPrice.toLocaleString(), "đ");
    
        const totalPriceHtml = `
            <li class="single-cart-list cart-total">
                <div class="cart-total">
                    <h6>Tổng cộng: <span class="price">${totalPrice.toLocaleString()} đ</span></h6>
                </div>
            </li>`;
        $(".cart-list").append(totalPriceHtml);
        
        const checkoutButtonHtml = `
            <li class="single-cart-list">
                <button class="checkout-button">Thanh toán (${totalPrice.toLocaleString()} đ)</button>
            </li>`;
        $(".cart-list").append(checkoutButtonHtml);
    
        // Cập nhật lại số lượng hiển thị trên icon giỏ hàng
        $(".badge-bg-1").text(totalQuantity);
    
        localStorage.setItem("cart", JSON.stringify(cart));
    }

    // Đảm bảo updateCart có thể được gọi từ bên ngoài
    window.updateCart = updateCart;

    // Sự kiện khi thêm sản phẩm vào giỏ
    $(document).on("click", ".add-to-cart-button", function (e) {
        e.preventDefault();
    
        const productId = $(this).data("id");
        const existingItem = cart.find(item => item.id === productId);
    
        if (existingItem) {
            // Nếu sản phẩm đã tồn tại trong giỏ hàng, tăng số lượng
            existingItem.quantity++;
        } else {
            // Nếu chưa có, thêm mới vào giỏ hàng
            const product = {
                id: productId,
                name: $(this).data("name"),
                price: parseInt($(this).data("price")),
                image: $(this).data("image"),
                quantity: 1
            };
            cart.push(product);
        }
    
        updateCart();
    });
    

    // Sự kiện khi đóng sản phẩm trong giỏ
    $(document).on("click", ".cart-close", function () {
        const productId = $(this).data("id");
        cart = cart.filter(item => item.id !== productId);
        updateCart();
    });

    // Sự kiện khi nhấn vào nút thanh toán
    $(document).on("click", ".checkout-button", function () {
        window.location.href = "/checkout/";
    });

    // Gọi updateCart khi trang tải
    updateCart();
});


