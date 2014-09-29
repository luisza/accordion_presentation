{% load proportion %} 
  if($ == undefined){
    JQ = CMS.$;
  }else{
     JQ = $;
    }
 (function($) {
 	$(document).ready(function(){
    activeItem = $("#accordion-{{ accordion.pk }} li:first");
    $(activeItem).addClass('active');
    
    {% if accordion.custom_min_width %} ap_min_collapse = "{{accordion.custom_min_width}}px";
    {%else%} ap_min_collapse = "{{device_info.width|proportion_resize:7 }}px";
    {%endif%}

    {% if accordion.custom_max_width %} ap_max_collapse = "{{accordion.custom_max_width}}px";
    {%else%} ap_max_collapse = "{{device_info.width|proportion_resize:80}}px";
    {%endif%}
 	
    {% if accordion.custom_duration %} ap_duration = {{accordion.custom_duration}};
    {%else%} ap_duration=300;
    {%endif%} 	
 	
    $("#accordion-{{ accordion.pk }} li").hover(function(){
        $(activeItem).animate({width: ap_min_collapse}, {duration:ap_duration, queue:false});
        $(this).animate({width: ap_max_collapse}, {duration:ap_duration, queue:false});
        activeItem = this;
    });
    	$("#accordion-{{ accordion.pk }} li").each(function(key, value){
    		console.log( ap_min_collapse+"; overflow: hidden;");
    		$(value).attr('style', "width: "+ap_min_collapse+"; overflow: hidden;");
    	});
 		$("#accordion-{{ accordion.pk }} li:first").animate(
 			{width: ap_max_collapse}, {duration:ap_duration, queue:false});
 	});
})(JQ);
