document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('button');
  
    buttons.forEach(button => {
      button.addEventListener('click', () => {
        alert('Sản phẩm đã được thêm vào giỏ hàng!');
      });
    });
  });
  