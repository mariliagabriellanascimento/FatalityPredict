document.getElementById('formulario').addEventListener('submit', function(event) {
    event.preventDefault();

    // Checar se todos os campos obrigatórios estão preenchidos
    const camposObrigatorios = document.querySelectorAll('select[required]');
    let formularioValido = true;

    camposObrigatorios.forEach(function(campo) {
      if (campo.value === "") {
        formularioValido = false;
        campo.style.borderColor = "red"; 
      } else {
        campo.style.borderColor = ""; 
      }
    });

    // Se houver campos não preenchidos, exibe a mensagem de erro
    if (!formularioValido) {
      document.getElementById('mensagemErro').style.display = 'block';
    } else {
      document.getElementById('mensagemErro').style.display = 'none';
      alert('Formulário enviado com sucesso!');
      
    }
  });