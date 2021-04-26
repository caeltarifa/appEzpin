appr = new Vue({
  el: '#appr',
  delimiters: ['[[%', '%]]'],
  mounted(){
    this.getMsj()
  },
  data(){
    return{
      usuarios:[]
    }
  },
  methods:{
    tabla(){
      this.$nextTick(() => {
        $('#m_recibidos').DataTable({
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
          },
          order:[[ 5, "desc" ]],
        });
      });
    },
    getMsj(){
      const path = 'http://ezpin.aasana.ga/amhs/get_msjs/'
      axios.get(path).then((respuesta) => {
        this.usuarios = respuesta.data.lista_recibidos
        this.tabla()
        console.log(this.tabla)
      }).catch((error) => {
        console.log(error)
      });
    }
  }
});

$(document).ready(function(){
  $('.btn_mr_refrescar').click(function(){
    location.reload();
    /* window.location.href = window.location.href; */
  });
});