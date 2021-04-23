$(document).ready(function(){
  /* ------------------------------ */
  /* Selectores con Busqueda */
  /* ------------------------------ */
  $('.menu__uno').select2();
  $('.menu__dos').select2();

  /* ------------------------------ */
  /* Modal de enviar mensaje */
  /* ------------------------------ */

  /* ----- -----  Boton Enviar Mensaje  ----- ----- */
  let modal_new_msg = document.getElementById('env__mensaje');
  $('.btn__new__msj').click(function(){
    modal_new_msg.style.display = 'block';
    $('.tarjeta-titulo').css({display:'block'});
  });

  /* ----- -----  Cerrar Modal fuera del modal  ----- ----- */
  window.addEventListener('click', function(e){
    if(e.target == flex){
      modal_new_msg.style.display = 'none';
    }
  });

  /* ----- -----  Cerrar modal con la X  ----- ----- */
  $('.close').click(function(){
    modal_new_msg.style.display = 'none';
  });

  /* ------------------------------ */
  /* Tarjetas 3D Modal enviar mensaje */
  /* ------------------------------ */

  /* ----- -----  Tarjetas 3D  ----- ----- */
  $("#card__msjenviar").flip({
    axis: 'x',
    trigger: 'manual',
    reverse: true
  });
  let cerrar;
  /* ----- -----  Parte Frontal  ----- ----- */
  $('.btn-msj-env').click(function(){
    $("#card__msjenviar").flip(true);
    cerrar = setTimeout(() => {
      modal_new_msg.style.display = 'none';
      $("#card__msjenviar").flip(false);
    },5000);
  });

  /* ----- -----  Cancelar Modal de mensaje  ----- ----- */
  $('.btn-msj-enviar-can').click(function(){
    modal_new_msg.style.display = 'none';
    $("#card__msjenviar").flip(false);
    clearInterval(cerrar);
  });


  /* ------------------------------ */
  /* Modal de guardar mensaje */
  /* ------------------------------ */

  /* ----- -----  Boton guardar Mensaje  ----- ----- */
  let modal_gua_msg = document.getElementById('guardar__mensaje');
  $('.btn__save__msj').click(function(){
    modal_gua_msg.style.display = 'block';
    $('.tarjeta-titulo').css({display:'block'});
  });

  /* ----- -----  Cerrar Modal fuera del modal  ----- ----- */
  window.addEventListener('click', function(e){
    if(e.target == flex){
      modal_gua_msg.style.display = 'none';
    }
  });

  /* ----- -----  Cerrar modal con la X  ----- ----- */
  $('.close').click(function(){
    modal_gua_msg.style.display = 'none';
  });

  /* ------------------------------ */
  /* Tarjetas 3D Modal enviar mensaje */
  /* ------------------------------ */

  /* ----- -----  Tarjetas 3D  ----- ----- */
  $("#card__msjguardar").flip({
    axis: 'x',
    trigger: 'manual',
    reverse: true
  });
  let cerrar2;
  /* ----- -----  Parte Frontal  ----- ----- */
  $('.btn-msj-guar').click(function(){
    $("#card__msjguardar").flip(true);
    cerrar2 = setTimeout(() => {
      modal_gua_msg.style.display = 'none';
      $("#card__msjguardar").flip(false);
    },5000);
  });

  /* ----- -----  Cancelar Modal de mensaje  ----- ----- */
  $('.btn-msj-guardar-can').click(function(){
    modal_gua_msg.style.display = 'none';
    $("#card__msjguardar").flip(false);
    clearInterval(cerrar2);
  });
});