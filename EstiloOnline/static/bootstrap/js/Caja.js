function withClient() {
	$('#withClient').children().addClass('active');
	$('#withoutClient').children().removeClass('active');
	$('#SelectClient').removeClass('hidden');
	$('#TypeIngreso').val('Con_Cliente');
}


function withoutClient() {
	$('#withClient').children().removeClass('active');
	$('#withoutClient').children().addClass('active');
	$('#SelectClient').addClass('hidden');
	$('#TypeIngreso').val('Sin_Cliente');

}