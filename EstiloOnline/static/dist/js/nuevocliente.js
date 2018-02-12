function NuevoCliente() {
	var nombre = $('#nombre').val();
	var correo = $('#correo').val();
	var telefono = $('#telefono').val();

	swal({
	  title: 'Procesando!',
	  text: 'Estamos realizando el registro',
	  timer: 5000,
	  onOpen: () => {
	    swal.showLoading()
	  }
	}).then((result) => {
	  if (result.dismiss === 'timer') {
	    
	  }
	})


	$.ajax({
        url: '/clientes/procesar/web/nuevo',
        data: {
          'nombre': nombre,
          'correo': correo,
          'telefono':telefono,
      },
      dataType: 'json',
      success: function (data) {
          if (data == 200) {
        	swal(
		  'Buen Trabajo !',
		  'Hemos Cargado exitosamente el registro!',
		  'success'
		)
        window.location.replace("/clientes/web");
        }
        else{
        	swal(
			  'Oops...',
			  'Correo Ya registrado, intente nuevamente!',
			  'error'
			)
        }

    }
});

	
}

setInterval(function(){ Guardar(); }, 300);

    function Guardar(){
      if ($('#nombre').val() != "" && $('#correo').val() != "" && $('#telefono').val() != ""){
        
        $('#guardar').attr("disabled", false);
      }
      else{
        
        $('#guardar').attr("disabled", true);
      }
    }