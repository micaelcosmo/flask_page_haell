document.addEventListener("DOMContentLoaded", function() {
    let carousels = document.querySelectorAll('.carousel');

    carousels.forEach(function(carousel, index) {
        let images = carousel.getElementsByTagName('img');
        let currentImageIndex = 0;

        function changeImage() {
            images[currentImageIndex].style.display = 'none';
            currentImageIndex = (currentImageIndex + 1) % images.length;
            images[currentImageIndex].style.display = 'block';
        }

        setInterval(changeImage, 3000);

        // Configurando os eventos para os modais dinâmicos
        let modal = document.getElementById(`videoModal${index + 1}`);
        let btn = document.getElementById(`openModal${index + 1}`);
        let span = document.getElementsByClassName(`close${index + 1}`)[0];

        if (btn && modal) {
            // Quando o usuário clica no botão, abre o modal
            btn.onclick = function() {
                modal.style.display = "block";
            }

            // Quando o usuário clica em <span> (x), fecha o modal
            if (span) {
                span.onclick = function() {
                    modal.style.display = "none";
                }
            }
        }
    });
});

document.addEventListener("DOMContentLoaded", function() {
    // Função para verificar e fechar o modal clicado fora
    window.onclick = function(event) {
        document.querySelectorAll('.modal').forEach(function(modal) {
            if (modal && event.target == modal) {
                modal.style.display = "none";
            }
        });
    }
});
