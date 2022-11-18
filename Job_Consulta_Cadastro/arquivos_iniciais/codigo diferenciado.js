
let formValidation = (function() { // variavel auto contida 
	function init(seletor) {

		var element = document.querySelector(seletor) 
		if (!element) {
			return false
		} 
		var fields = element.querySelectorAll("input, select")

		console.log(fields)
	}
	return {
	init: init
	 //esquerda - chave
	 //direita - valor
	}

	cadastrarDespesa
})() 

document.addEventListener("DOMContentLoaded", function() {
	formValidation.init('.despesasForm')
})



