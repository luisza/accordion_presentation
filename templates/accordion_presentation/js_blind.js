{% load proportion %} 
  if($ == undefined){
    JQ = CMS.$;
  }else{
     JQ = $;
    }
    function ap_resize(real_size, proportion){
    	return parseInt(real_size*proportion/100)
    }
 (function($) {
 	$(document).ready(function(){
    activeItem = $("#accordion-{{ accordion.pk }} li:first");
    $(activeItem).addClass('active');
    
    {% if accordion.custom_min_width %} ap_min_collapse = "{{accordion.custom_min_width}}px";
    {%else%} ap_min_collapse = "{{device_info.width|proportion_resize:9 }}px";
    {%endif%}

    {% if accordion.custom_max_width %} ap_max_collapse = "{{accordion.custom_max_width}}px";
    {%else%} ap_max_collapse = "{{device_info.width|proportion_resize:70}}px";
    {%endif%}
 	
    {% if accordion.custom_duration %} ap_duration = {{accordion.custom_duration}};
    {%else%} ap_duration=300;
    {%endif%} 	
 	
    $("#accordion-{{ accordion.pk }} li").hover(function(){
    	if(activeItem != this){
	        $(activeItem).animate({width: ap_resize($(".ap_accordion").width(), 9)}, {duration:ap_duration, queue:false});
	        $(this).animate({width: ap_resize($(".ap_accordion").width(), 70)}, {duration:ap_duration, queue:false});
	        activeItem = this;
       }
    });
    	$("#accordion-{{ accordion.pk }} li").each(function(key, value){
    		$(value).attr('style', "width: "+ap_min_collapse+"; overflow: hidden;");
    	});
 		$("#accordion-{{ accordion.pk }} li:first").animate(
 			{width: ap_max_collapse}, {duration:ap_duration, queue:false});
 	});
 	
 	
 	$( window ).resize(function() {
		ap_max_collapse = $( window ).width();
		 
		});
})(JQ);
