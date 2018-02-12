function reajusteServicio() {
	
      swal.setDefaults({
          input: 'text',
          confirmButtonText: 'Siguiente &rarr;',
          showCancelButton: true,
          progressSteps: ['1',]
        })
        var steps = [
        
          {
            title: 'Ingrese el porcentaje que desea aumentar a sus precios de servicios ',
            text: 'Porcentaje'
          },


          
        ]

        swal.queue(steps).then(function (result) {
          porcentaje = parseFloat(result[0]);
         
               swal.resetDefaults()
                $.ajax({
                    url: '/servicios/reajuste/precio',
                    data: {
                      'porcentaje':porcentaje,
                      
                  },
                  dataType: 'json',
                  success: function (status) {
                     swal({
                        title: 'Hemos Cargado de manera exitosa su reajuste!',
                        confirmButtonText: 'Aceptar!'
                      })
                     location.reload(); 
                }
            });

        }, function () {
          swal.resetDefaults()
        })
}


function reajusteProductos() {
	swal.setDefaults({
          input: 'text',
          confirmButtonText: 'Siguiente &rarr;',
          showCancelButton: true,
          progressSteps: ['1',]
        })
        var steps = [
        
          {
            title: 'Ingrese el porcentaje que desea aumentar a sus precios de promociociones ',
            text: 'Porcentaje'
          },


          
        ]

        swal.queue(steps).then(function (result) {
          porcentaje = parseFloat(result[0]);
         
               swal.resetDefaults()
                $.ajax({
                    url: '/promociones/reajuste/precio',
                    data: {
                      'porcentaje':porcentaje,
                      
                  },
                  dataType: 'json',
                  success: function (status) {
                     swal({
                        title: 'Hemos Cargado de manera exitosa su reajuste!',
                        confirmButtonText: 'Aceptar!'
                      })
                     location.reload(); 
                }
            });

        }, function () {
          swal.resetDefaults()
        })
}