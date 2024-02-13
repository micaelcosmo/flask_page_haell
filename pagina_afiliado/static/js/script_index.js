// Aqui você pode adicionar qualquer JavaScript necessário para sua página
document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById('myForm');
    
    form.addEventListener('submit', function (event) {
        event.preventDefault();

        // Aqui você pode adicionar a lógica para exibir a janela pop-up animada
                
        // Capturando os dados do formulário
        const formData = {
            nome: form.elements['nome'].value,
            email: form.elements['email'].value,
            telefone: form.elements['telefone'].value,
            mensagem: form.elements['mensagem'].value,
        };

        // Enviando os dados para o servidor usando Fetch API
        fetch('/submit_form', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        })
        .then(response => response.json())
        .then(data => {
            // Exibindo a janela pop-up após o envio bem-sucedido
            alert('Enviado com sucesso!');
            
            // Limpar o formulário
            form.reset();
            // Aqui você pode adicionar qualquer lógica adicional após o envio bem-sucedido
        })
        .catch(error => {
            console.error('Erro durante o envio do formulário:', error);
        });
    });
});
