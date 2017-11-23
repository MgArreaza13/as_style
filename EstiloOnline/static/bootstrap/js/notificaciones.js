//ajax para las notificaciones 

      setInterval(function () {
         $.ajax({
        url: '/api/notificaciones/',
        dataType: 'json',
        success: function (data) {
          if (data) {
            
           var cont = data.length;
            $("#contadorNotificaciones").html(cont);
            $("#headerNotificaciones").html('tienes '+cont+' Reservas Nuevas');
            var html = "";
            for (var i=0 ; i < cont ; i++) {

            html+='<li><a class="notificacion" value="'+data[i].id+'" href="javascript:void(0);"><div class="pull-left"<i class="fa fa-shopping-cart text-green"></i></div><h4>Nueva Reserva   <small><i class="fa fa-clock-o"></i> '+ data[i].HoraTurn +' </small></h4><p>'+data[i].nombre + ' reserva para '+ data[i].dateTurn +'</p></a></li>'

                


                }
                $('#MenuNotificaciones').html(html);
            
            
          }
        }
      });
      }, 300);



      $('#MenuNotificaciones').on('click', '.notificacion', function() {
        
        var pk = $(this).attr('value');
       
        
        

        $.ajax({
        url: '/notificaciones/vista/',
        data: {
          'pk': pk
      },
       dataType: 'json',
       success: function (data) {
          if (data){
            
        var modal = '<div class="col-lg-12">'+
          '<div  class="modal modal-primary" id="myModal" role="dialog">'+
            '<div class="modal-dialog">'+
              '<div style="margin-left: 7em;" class="modal-content">'+
                '<div class="modal-header">'+
                  '<button type="button" class="close" data-dismiss="modal" aria-label="'+
                  'Close">'+
                    '<span aria-hidden="true">×</span></button>'+
                  '<h4 class="modal-title">Notificacion</h4>'+
                '</div>'+
                '<div class="modal-body">'+
                  '<p>Tienes una nueva notificacion de una reserva de parte de '+ data.nombre +' para el dia '+ data.fecha +'   </p>'+
                '</div>'+
               '<div class="modal-footer">'+
                  '<button type="button" class="btn btn-outline pull-left"'+
                  'data-dismiss="'+
                  'modal">Cerrar</button>'+
                '</div>'+
              '</div>'+
              
            '</div>'+
            
          '</div>'+
           
         '</div>';

         $('#miguel').html(modal);
          $("#myModal").modal("show");
          }
    }
});

});
