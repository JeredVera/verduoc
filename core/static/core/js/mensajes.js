function deleteProducto(id) {
    Swal.fire({
        title: 'Confimar',
        text: 'Está seguro que desea eliminar?',
        icon: 'info',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Confirmar'
      }).then((result) => {
        if (result.isConfirmed) {
          Swal.fire('Eliminado!','Producto Eliminado Correctamente','success').then(function() {
              window.location.href = "/delete_product/"+id+"/";
          })
        }
      })
}

function logiarse() {
  Swal.fire ({
    title: 'No Tienes Cuenta',
    text: 'No puedes ingresar sin tener una cuenta , iniciar sesion para saber mas',
    icon: 'info',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Iniciar Sesion'
  }) .then((result) => {
    if (result.isConfirmed){
      window.location.href = "/accounts/login/";
    }
  })
}

function suscrito(){
  Swal.fire({
    title: 'Felicitaciones',
        text: 'Suscrito Correctamente',
        icon: 'success',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Confirmar'
  }) .then ((result) =>{
    if (result.isConfirmed){
      window.location.href = "/";
    }
  })
}