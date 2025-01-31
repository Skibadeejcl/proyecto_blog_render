// fetch('https://mindicador.cl/api').then(function(response) {
//    return response.json();
// }).then(function(dailyIndicators) {
//   document.getElementById("UF").innerHTML = 'UF Actual $' + dailyIndicators.uf.valor;
//   document.getElementById("DolarO").innerHTML = 'Dólar obs $' + dailyIndicators.dolar.valor;
//   document.getElementById("DolarA").innerHTML = 'El valor actual del Dólar acuerdo es $' + dailyIndicators.dolar_intercambio.valor;
//   document.getElementById("Euro").innerHTML = 'El valor actual del Euro es $' + dailyIndicators.euro.valor;
//   document.getElementById("IPC").innerHTML = 'El valor actual del IPC es ' + dailyIndicators.ipc.valor + '%';
//   document.getElementById("UTM").innerHTML = 'UTM $' + dailyIndicators.utm.valor;
//   document.getElementById("IVP").innerHTML = 'El valor actual del IVP es $' + dailyIndicators.ivp.valor;
//   document.getElementById("Imacec").innerHTML = 'El valor actual del Imacec es ' + dailyIndicators.imacec.valor + '%';
// }).catch(function(error) {
//   console.log('Requestfailed', error);
// });

$('.number').each(function() {
  let text = $(this).text().trim(); // Elimina espacios en blanco adicionales
  let sanitizedText = text.replace(/[^0-9]/g, ''); // Mantiene solo números

  if (sanitizedText) { // Si hay algo después de sanitizar
      let number = parseInt(sanitizedText, 10); // Convierte a número entero

      if (!isNaN(number)) { // Si es un número válido
          $(this).text("$" + number.toLocaleString('es-ES')); // Formatea como moneda
      } else {
          $(this).text("No válido"); // Si no es un número válido
      }
  } else {
      $(this).text("No válido"); // Si el texto está vacío o no tiene números
  }
});


// function checkRut(rut) {
//   // Despejar Puntos
//   var valor = rut.value.replace('.','');
//   // Despejar Guión
//   valor = valor.replace('-','');
  
//   // Aislar Cuerpo y Dígito Verificador
//   cuerpo = valor.slice(0,-1);
//   dv = valor.slice(-1).toUpperCase();
  
//   // Formatear RUN
//   rut.value = cuerpo + '-'+ dv
  
//   // Si no cumple con el mínimo ej. (n.nnn.nnn)
//   if(cuerpo.length < 7) { rut.setCustomValidity("RUT Incompleto"); return false;}
  
//   // Calcular Dígito Verificador
//   suma = 0;
//   multiplo = 2;
  
//   // Para cada dígito del Cuerpo
//   for(i=1;i<=cuerpo.length;i++) {
  
//       // Obtener su Producto con el Múltiplo Correspondiente
//       index = multiplo * valor.charAt(cuerpo.length - i);
      
//       // Sumar al Contador General
//       suma = suma + index;
      
//       // Consolidar Múltiplo dentro del rango [2,7]
//       if(multiplo < 7) { multiplo = multiplo + 1; } else { multiplo = 2; }

//   }
  
//   // Calcular Dígito Verificador en base al Módulo 11
//   dvEsperado = 11 - (suma % 11);
  
//   // Casos Especiales (0 y K)
//   dv = (dv == 'K')?10:dv;
//   dv = (dv == 0)?11:dv;
  
//   // Validar que el Cuerpo coincide con su Dígito Verificador
//   if(dvEsperado != dv) { rut.setCustomValidity("RUT Inválido"); return false; }
  
//   // Si todo sale bien, eliminar errores (decretar que es válido)
//   rut.setCustomValidity('');
// }




/*eliminacion*/
const btnsEliminacion = document.querySelectorAll(".btnEliminacion");

(function () {
    
    btnsEliminacion.forEach((btn) => {
      // console.log(btn);
        btn.addEventListener("click", function (e) {
            let confirmacion = confirm("¿Desea eliminar la publicación?");
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });
    

      // btnsEliminacion.forEach((btn) => {
      //     console.log(btn);
      // });

})();
/*fin eliminacion*/





// Carousell multiple portada

// $('.carousel .carousel-item').each(function () {
//   var minPerSlide = 4;
//   var next = $(this).next();
//   if (!next.length) {
//   next = $(this).siblings(':first');
//   }
//   next.children(':first-child').clone().appendTo($(this));
  
//   for (var i = 0; i < minPerSlide; i++) { next=next.next(); if (!next.length) { next=$(this).siblings(':first'); } next.children(':first-child').clone().appendTo($(this)); } });

  // Fin carousell multiple portada


 
  /* slogan effect */
  // window.addEventListener("scroll", function() {showFunction()});

  //   function showFunction() {
  //       if (document.body.scrollTop > 900 || document.documentElement.scrollTop > 900) {
  //           document.getElementById("toptexts2").style.display = "block";
  //       } else {
  //           document.getElementById("toptexts2").style.display = "none";
  //       }
  //   }
  /*fin slogan effect */


// Reveal effect
  // function reveal() {
  //   var reveals = document.querySelectorAll(".reveal");
  
  //   for (var i = 0; i < reveals.length; i++) {
  //     var windowHeight = window.innerHeight;
  //     var elementTop = reveals[i].getBoundingClientRect().top;
  //     var elementVisible = 150;
  
  //     if (elementTop < windowHeight - elementVisible) {
  //       reveals[i].classList.add("active");
  //     } else {
  //       reveals[i].classList.remove("active");
  //     }
  //   }
  // }
  
  // window.addEventListener("scroll", reveal);
  // fin Reveal effect

  // tooltip
  const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
  const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

  // navbar appear
  // $(function () {
  //   $(document).scroll(function () {
  //     var $nav = $(".fixed-top");
  //     $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
  //   });
  // });



// efecto cartas 3d
  // $(document).ready(function() {
  //   var front = document.getElementsByClassName("front");
  //   var back = document.getElementsByClassName("back");
  
  //   var highest = 0;
  //   var absoluteSide = "";
  
  //   for (var i = 0; i < front.length; i++) {
  //     if (front[i].offsetHeight > back[i].offsetHeight) {
  //       if (front[i].offsetHeight > highest) {
  //         highest = front[i].offsetHeight;
  //         absoluteSide = ".front";
  //       }
  //     } else if (back[i].offsetHeight > highest) {
  //       highest = back[i].offsetHeight;
  //       absoluteSide = ".back";
  //     }
  //   }
  //   $(".front").css("height", highest);
  //   $(".back").css("height", highest);
  //   $(absoluteSide).css("position", "absolute");
  // });



  