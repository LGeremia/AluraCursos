<meta charset="UTF-8">
<script>
    function pulaLinha(){
        document.write("<br><hr><br>");
    }

    function escreva(texto){
        document.write("<big>"+texto+"</big>");
        pulaLinha();
    }
    function calculaIMC(primeiroNumero, segundoNumero){
        var laranja = segundoNumero*segundoNumero;
        return primeiroNumero/laranja;
        }

    var peso = prompt("Digite seu peso: ");
    var altura = prompt("Digite sua altura: ");

    escreva("o meu IMC é: " + calculaIMC(peso, altura));

</script>