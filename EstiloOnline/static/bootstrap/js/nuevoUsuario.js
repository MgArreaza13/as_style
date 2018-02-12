 //$('#EnviarDatos').attr("disabled", true);



 setInterval(function(){ Guardar(); }, 300);

    function Guardar(){
      if ($('#id_username').val() != "" && $('#id_password1').val() != "" && $('#id_password2').val() != ""  && $('#id_nameUser').val() != ""  && $('#id_mailUser').val() != ""  && $('#id_image').val() != ""  && $('#fechadecumpleamos').val() != ""   ){
        
         $('#EnviarDatos').attr("disabled", false);
      }
      else{
        
         $('#EnviarDatos').attr("disabled", true);
      }
    }