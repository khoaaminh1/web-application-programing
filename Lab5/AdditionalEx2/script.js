const images = [
    'images/slide1.png',
    'images/slide2.png',
    'images/slide3.png'
  ];
  
  let currentIndex = 0;
  const slideImg = document.getElementById('slide');
  
  // Tự động chuyển ảnh sau mỗi 3 giây
  setInterval(() => {
    nextImage();
  }, 3000);
  
  function showImage(index) {
    slideImg.src = images[index];
  }
  
  function nextImage() {
    currentIndex = (currentIndex + 1) % images.length;
    showImage(currentIndex);
  }
  
  function prevImage() {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    showImage(currentIndex);
  }
  