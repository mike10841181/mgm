var idImage = '';
$(document).ready(function()
{
	
    $('#logoCalzadoGloria a').fadeIn('slow');

    //login
    /*$("#LoginCalzadoGloria a").fancybox({
        'overlayShow'	: true,
        'transitionIn'	: 'elastic',
        'transitionOut'	: 'elastic',
        'padding'           : '4',
        'centerOnScroll'    : true,
        'overlayColor'      : '#000',
        'type'				: 'iframe'
        
    });*/
    //fancy de los productos en el catalogo        
    $('[name="fancyClientsInfoPreview"]').fancybox({
        'overlayShow'	: true,
        'transitionIn'	: 'elastic',
        'transitionOut'	: 'elastic',
        'padding'           : '4',
        'centerOnScroll'    : true,
        'overlayColor'      : '#000',
		'cyclic'		: true
    });
	//self client registration
	/*$('#fancyClientForm').fancybox({
        'overlayShow'	: true,
        'transitionIn'	: 'elastic',
        'transitionOut'	: 'elastic',
        'padding'           : '4',
        'centerOnScroll'    : true,
        'overlayColor'      : '#000'
    });*/
	/*$('[name="popUpsParams"]').fancybox({
        'overlayShow'	: true,
        'transitionIn'	: 'elastic',
        'transitionOut'	: 'elastic',
        'padding'           : '4',
        'centerOnScroll'    : true,
        'overlayColor'      : '#000',
		'type'			:	'iframe'
    });*/
});
function toolTipPos(elem, pos) {
//gravity : S, W, N, E
    $(elem).tipsy(
    {
        gravity : pos
    });
}
function diplayClientForm(id)
{
    alert(id);
    $('#fancybox-close').trigger('click');
/*$('#' + id).fancybox({
        'overlayShow'	: true,
        'transitionIn'	: 'elastic',
        'transitionOut'	: 'elastic',
        'padding'       : '4',
        'centerOnScroll': true,
        'overlayColor'  : '#000'
    });*/
}
function selectSubmenu(id_subMenu)
{
    var file = '';

    if( id_subMenu.split('_')[0] == 'submenuEmpleado')
    {
        if(id_subMenu.split('_')[1] == '4')
        {
            file = 'eliminarEmpleado.php';
        }
        else
        if(id_subMenu.split('_')[1] == '3')
        {
            file = 'modificarEmpleado.php';
        }
        else
        if(id_subMenu.split('_')[1] == '2')
        {
            file = 'registrarEmpleado.php';
        }else
        {
            file = 'perfilEmpleado.php';
        }        
        count = 1;        
        for(i = 0; i < $('#submenuEmpleado > span').size(); i++)
        {
            $('#submenuEmpleado_' + (count).toString()).removeClass('selectedSubmenu');
            count++;
        }        
        $('#' + id_subMenu).addClass('selectedSubmenu');
    }
    else
    if( id_subMenu.split('_')[0] == 'submenuPedido')
    {
        if(id_subMenu.split('_')[1] == '5')
        {
            file = 'actDesactivarPedido.php';
        }
        else
        if(id_subMenu.split('_')[1] == '4')
        {
            file = 'autorizarCancelarPedido.php';
        }
        else
        if(id_subMenu.split('_')[1] == '3')
        {
            file = 'modificarPedido.php';
        }
        else
        if(id_subMenu.split('_')[1] == '2')
        {
            file = 'estatusPedido.php';
        }
        else
        {
            file = 'ingresarPedido.php';
        }        
        count = 1;        
        for(i = 0; i < $('#submenuPedido > span').size(); i++)
        {
            $('#submenuPedido_' + (count).toString()).removeClass('selectedSubmenu');
            count++;
        }        
        $('#' + id_subMenu).addClass('selectedSubmenu');
    }
    else
    if( id_subMenu.split('_')[0] == 'submenuCotizacion')
    {
        if(id_subMenu.split('_')[1] == '3')
        {
            file = 'consultarCotizacion.php';
        }
        else
        if(id_subMenu.split('_')[1] == '2')
        {
            file = 'modificarCotizacion.php';
        }
        else
        {
            file = 'ingresarCotizacion.php';
        }        
        count = 1;        
        for(i = 0; i < $('#submenuCotizacion > span').size(); i++)
        {
            $('#submenuCotizacion_' + (count).toString()).removeClass('selectedSubmenu');
            count++;
        }        
        $('#' + id_subMenu).addClass('selectedSubmenu');
    }
    else
    if( id_subMenu.split('_')[0] == 'submenuParametrizacion')
    {
        if(id_subMenu.split('_')[1] == '3')
        {
            file = 'eliminarDataParam.php';
        }
        else
        if(id_subMenu.split('_')[1] == '2')
        {
            file = 'modificarDataParam.php';
        }
        else
        {
            file = 'ingresarDataParam.php';
        }        
        count = 1;        
        for(i = 0; i < $('#submenuParametrizacion > span').size(); i++)
        {
            $('#submenuParametrizacion_' + (count).toString()).removeClass('selectedSubmenu');
            count++;
        }        
        $('#' + id_subMenu).addClass('selectedSubmenu');
    }
    else
    if( id_subMenu.split('_')[0] == 'submenuInventario')
    {
        if(id_subMenu.split('_')[1] == '3')
        {
            file = 'eliminarInventario.php';
        }
        else
        if(id_subMenu.split('_')[1] == '2')
        {
            file = 'ingresarInventario.php';
        }
        else
        {
            file = 'existenciasInventario.php';
        }        
        count = 1;        
        for(i = 0; i < $('#submenuInventario > span').size(); i++)
        {
            $('#submenuInventario_' + (count).toString()).removeClass('selectedSubmenu');
            count++;
        }        
        $('#' + id_subMenu).addClass('selectedSubmenu');
    }
    else
    if( id_subMenu.split('_')[0] == 'submenuCatalogo')
    {
		file = '/catalogo/'
		
        if(id_subMenu.split('_')[1] == '3')
        {
            categoria = '3';
        }
        else
        if(id_subMenu.split('_')[1] == '2')
        {
            categoria = '2';
        }
        else
        {
            categoria = '1';
        }        
        count = 1;        
        for(i = 0; i < $('#submenuCatalogo > span').size(); i++)
        {
            $('#submenuCatalogo_' + (count).toString()).removeClass('selectedSubmenu');
            count++;
        }        
        $('#' + id_subMenu).addClass('selectedSubmenu');
        
        $.ajax({
			type: "GET",
			data: {
				data: 'catalogo_categoria',
				id: categoria
			},
			url: "/ajax/ajax",
			success : function(msg)
				{
					$("#ContentPaneSubsites").html(msg);
				},
			error : function()
 				{
					alert('error');
				}
		});
    }
    else
    if( id_subMenu.split('_')[0] == 'submenuProduccion')
    {
        if(id_subMenu.split('_')[1] == '2')
        {
            file = 'crearReporteProduccion.php';
        }
        else
        {
            file = 'verReporteProduccion.php';
        }        
        count = 1;        
        for(i = 0; i < $('#submenuProduccion > span').size(); i++)
        {
            $('#submenuProduccion_' + (count).toString()).removeClass('selectedSubmenu');
            count++;
        }        
        $('#' + id_subMenu).addClass('selectedSubmenu');
    }
    else
    if( id_subMenu.split('_')[0] == 'submenuFactura')
    {
        if(id_subMenu.split('_')[1] == '2')
        {
            file = 'verFactura.php';
        }
        else
        {
            file = 'verFactura.php';
        }        
        count = 1;        
        for(i = 0; i < $('#submenuFactura > span').size(); i++)
        {
            $('#submenuFactura_' + (count).toString()).removeClass('selectedSubmenu');
            count++;
        }        
        $('#' + id_subMenu).addClass('selectedSubmenu');
    }
    
    var xmlhttp; 
    if (window.XMLHttpRequest)
    {// code for IE7+, Firefox, Chrome, Opera, Safari
        xmlhttp=new XMLHttpRequest();
    }
    else
    {// code for IE6, IE5
        xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    /*xmlhttp.onreadystatechange=function()
    {
        if (xmlhttp.readyState===4 && xmlhttp.status===200)
        {                
            $('#ContentPaneSubsites').html(xmlhttp.responseText);          
        }
    }
    xmlhttp.open("GET", file, true);
    xmlhttp.send(null);*/
}
function selectTDato(value)
{
    if(value === 'Personas')
    {
        $("#selectProductos").fadeOut('fast');
        $("#tableProductos").fadeOut("fast");
        t = setTimeout('$("#selectPersonas").fadeIn("fast");$("#tablePersonas").fadeIn("fast");', 170);
    }
    if(value === 'Productos')
    {
        $("#selectPersonas").fadeOut('fast');
        $("#tablePersonas").fadeOut("fast");
        t = setTimeout('$("#selectProductos").fadeIn("fast");$("#tableProductos").fadeIn("fast");', 170);
    }
}
function selectTDato2(value)
{
    if(value === 'Personas')
    {
        $("#selectProductos").fadeOut('fast');
        $("#selectAreasDeptos").fadeOut('fast');
        t = setTimeout('$("#selectPersonas").fadeIn("fast");', 170);
    }
    if(value === 'Productos')
    {
        $("#selectPersonas").fadeOut('fast');
        $("#selectAreasDeptos").fadeOut('fast');
        t = setTimeout('$("#selectProductos").fadeIn("fast");', 170);
    }
    if(value === 'AreasDeptos')
    {
        $("#selectPersonas").fadeOut('fast');
        $("#selectProductos").fadeOut('fast');
        t = setTimeout('$("#selectAreasDeptos").fadeIn("fast");', 170);
    }
}
function filtrarPorFamiliaDeModelo(idFamilia)
{
	if (idFamilia == "fam_0"){
		$("#ListaDeModelos li").fadeIn('slow');
	}else{
		$('#ListaDeModelos li').css('display', 'none');
		$('#ListaDeModelos [idFamilia="'+ idFamilia+'"]').fadeIn('slow');
	}
		
}
function filtroDeClientes(str, idTipoCliente)
{
	$('#listaClientes li').css('display', 'none');
	str = str.trim()
	
	if (idTipoCliente == 'tCl_0')
	{
		if (str == "")
		{
			$('#listaClientes li').fadeIn('fast');
		}
		else
		{
			$('#listaClientes [primerNombre*="'+ str +'"]').fadeIn('fast');
		}
	}
	else
	{
		if (str == "")
		{
			$('#listaClientes [idTipoDeCliente="'+ idTipoCliente+'"]').fadeIn('fast');
		}
		else
		{
			$('#listaClientes [primerNombre*="'+ str +'"][idTipoDeCliente="'+ idTipoCliente+'"]').fadeIn('fast');
		}
	}
}
function filtroDeEmpleados(str, idTipoEmpleado)
{
	$('#listaClientes li').css('display', 'none');
	str = str.trim()
	
	if (idTipoEmpleado == 'tEm_0')
	{
		if (str == "")
		{
			$('#listaClientes li').fadeIn('fast');
		}
		else
		{
			$('#listaClientes [primerNombre*="'+ str +'"]').fadeIn('fast');
		}
	}
	else
	{
		if (str == "")
		{
			$('#listaClientes [idTipoDeEmpleado="'+ idTipoEmpleado +'"]').fadeIn('fast');
		}
		else
		{
			$('#listaClientes [primerNombre*="'+ str +'"][idTipoDeEmpleado="'+ idTipoEmpleado+'"]').fadeIn('fast');
		}
	}
}
function ClientProfileViewPaneDisplay(val)
{
	if (val == 0)
	{
		$('#ClientProfileViewPane').css({overflow : 'hidden'});
		$('#ClientProfileViewPane').animate({
			height : '4px'
		}, 500,
		function(){
			$('#ClientProfileViewPane').fadeOut('300');
		});
		var t = setTimeout("$('#ClientProfileViewPane').html('')", 850);
	}
	else
	{
		$('#ClientProfileViewPane').css({height : 'auto'});
		$('#ClientProfileViewPane').fadeIn('slow');
	}
}
function id_to_windownameMgm(text) {
	text = text.replace(/\./g, '__dot__');
	text = text.replace(/\-/g, '__dash__');
	return text;
} 
function showAddAnotherPopupMgm(triggeringLink, h, w) {
	var name = triggeringLink.id.replace(/^add_/, '');
	name = id_to_windownameMgm(name);
	href = triggeringLink.href
	
	if (href.indexOf('?') == -1) {
		href += '?_popup=1';
	} else {
		href += '&_popup=1';
	}
	
	var win = window.open(href, name, 'height='+h+',width='+w+',resizable=no,scrollbars=yes,location=no,directories=no');
	win.focus();
	return false;
} 

function prueba(csrftoken)
{
	$.ajax({
			type: "GET",
			data: {
				data: 'd',
				id: 'dsd'
			},
			url: "inscripcion/",
			success : function(msg)
				{
					alert('todo bien');
				},
			error : function()
 				{
					alert('error');
				}
		});

}


