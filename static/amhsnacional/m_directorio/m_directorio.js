diru = new Vue({
  el: '#diru',
  delimiters: ['[[%', '%]]'],
  mounted(){
    this.getDirUs(),
    this.getDirGrupos()
  },
  data(){
    return{
      personass:[
      ],
      grupos:[
      ]
    }
  },
  methods:{
    tabla(){
      this.$nextTick(() => {
        $('#dir__usuarios__add').DataTable({
          language:{
            "sProcessing":	"Procesando...",
            "sLengthMenu":	"Mostrar _MENU_ registros",
            "sZeroRecords":	"No se encontraron resultados",
            "sEmptyTable":	"Ningún dato disponible en esta tabla",
            "sInfo":	"Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
            "sInfoEmpty":	"Mostrando registros del 0 al 0 de un total de 0 registros",
            "sInfoFiltered":	"(filtrado de un total de _MAX_ registros)",
            "sSearch":	"Buscar:",
            "sInfoThousands":	",",
            "sLoadingRecords":	"Cargando...",
            "oPaginate":{
              "sFirst":	"Primero",
              "sLast":	"Último",
              "sNext":	"Siguiente",
              "sPrevious":	"Anterior"
            },
            "oAria":{

              "sSortAscending":	": Activar para ordenar la columna de manera ascendente",
              "sSortDescending":	": Activar para ordenar la columna de manera descendente"
            },	
            "buttons":{
              "copy":	"Copiar",
              "colvis":	"Visibilidad"
            }	
          }
        });
      });
    },
    getDirUs(){
      const path = 'http://ezpin.aasana.ga/amhs/dependencias'
      axios.get(path).then((respuesta) => {
        this.personass = respuesta.data.lista_usuarios
        this.tabla()
      }).catch((error) => {
        console.log(error)
      });
    },
    tabla_grupos(){
      this.$nextTick(() => {
        $('#dir__grupos__add').DataTable({
          language:{
            "sProcessing":	"Procesando...",
            "sLengthMenu":	"Mostrar _MENU_ registros",
            "sZeroRecords":	"No se encontraron resultados",
            "sEmptyTable":	"Ningún dato disponible en esta tabla",
            "sInfo":	"Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
            "sInfoEmpty":	"Mostrando registros del 0 al 0 de un total de 0 registros",
            "sInfoFiltered":	"(filtrado de un total de _MAX_ registros)",
            "sSearch":	"Buscar:",
            "sInfoThousands":	",",
            "sLoadingRecords":	"Cargando...",
            "oPaginate":{
              "sFirst":	"Primero",
              "sLast":	"Último",
              "sNext":	"Siguiente",
              "sPrevious":	"Anterior"
            },
            "oAria":{

              "sSortAscending":	": Activar para ordenar la columna de manera ascendente",
              "sSortDescending":	": Activar para ordenar la columna de manera descendente"
            },	
            "buttons":{
              "copy":	"Copiar",
              "colvis":	"Visibilidad"
            }	
          }
        });
      });
    },
    getDirGrupos(){
      const path = 'http://ezpin.aasana.ga/amhs/grupos'
      axios.get(path).then((respuesta) => {
        this.grupos = respuesta.data.lista_grupos
        this.tabla_grupos()
      }).catch((error) => {
        console.log(error)
      });
    }
  }
});

$(document).ready(function(){
  /* Grupos */
  $('.btn__usuarios').click(function(e){
    e.preventDefault();
    $(".m__usuario").css({display: "block"});
    $(".m__grupos").css({display: "none"});
    $('.m__new__grupo').css({display: "none"});
  });

  /* modal */
  /* let modal_grupo = document.getElementById('dir__grupo');

  $('.add__grupo').click(function(){
    modal_grupo.style.display = 'block';
  });
  $('#close__addgrupo').click(function(){
    modal_grupo.style.display = 'none';
  }); */


  /* Usuarios */
  $('.btn__grupos').click(function(e){
    e.preventDefault();
    $(".m__usuario").css({display: "none"});
    $(".m__grupos").css({display: "block"});
    $('.m__new__grupo').css({display: "none"});
  });

  /* Cartas 3D directorio grupo*/
  /* $("#card__dirgrupo").flip({
    trigger: 'manual'
  });
  $('.btn-dirgroup-guardar').click(function(){
    $("#card__dirgrupo").flip(true);
  });
  $('.btn-dirgroup-end').click(function(){
    $("#card__dirgrupo").flip(false);
    modal_grupo.style.display = 'none';
  }); */

  /* Dato del Modal de Eliminar */
  let modal_grupo_del = document.getElementById('dir__grupo_del');

  /* Modal para Eliminar del Directorio su grupo  */
  $('.btn-dir-group-del').click(function(){
    modal_grupo_del.style.display = 'block';
  });
  $('#close__dir_group_del').click(function(){
    modal_grupo_del.style.display = 'none';
  });

  /* Carta 3D para Eliminar el Grupo */
  $("#card__dirgrupodel").flip({
    trigger: 'manual'
  });
  $('.btn-dirgrupo-del').click(function(){
    $("#card__dirgrupodel").flip(true);

    setTimeout(function(){
      $("#card__dirgrupodel").flip(false);
      modal_grupo_del.style.display = 'none';
    },5000);
  });
  $('.btn-dirgrupo-del-can').click(function(){
    modal_grupo_del.style.display = 'none';
  });

  $('.btn-dirgrupo-del-con2').click(function(){
    $("#card__dirgrupodel").flip(false);
    modal_grupo_del.style.display = 'none';
  });


  /* ------------------------------ */
  /* Agregar Nuevo Grupo */
  /* ------------------------------ */

  /* ----- -----  select2  ----- ----- */
  $('.menu__tres').select2();

  /* ----- -----  Contenido new grupo  ----- ----- */
  $('.btn__add__grupo').click(function(){
    $(".m__usuario").css({display: "none"});
    $(".m__grupos").css({display: "none"});
    $('.m__new__grupo').css({display: "block"});
  });



  let modal_group_add = document.getElementById('dir__grupo_add');
  $('.btn_guardar_group_add').click(function(){
    modal_group_add.style.display = 'block';
  });
  $('#close__dir_group_add').click(function(){
    modal_group_add.style.display = 'none';
  });

  /* CArtas 3D directorio usuario */
  $("#card__dirgrupoadd").flip({
    trigger: 'manual'
  });
  $('.btn-dirgrupo-add').click(function(){
    $("#card__dirgrupoadd").flip(true);
    setTimeout(function(){
      $("#card__dirgrupoadd").flip(false);
      modal_group_add.style.display = 'none';
    },5000);
  });
  $('.btn-dirgrupo-del-add').click(function(){
    $("#card__dirgrupoadd").flip(false);
    modal_group_add.style.display = 'none';
  });
});