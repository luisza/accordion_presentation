switch_acordion =true;
$=($ || CMS.$);
function get_proportion(real_size, proportion){
	return parseInt(real_size*proportion/100);
}
    

function resize_image_max_width(element, height, width, maxCol){
	$(element).removeClass('ap_height');
	$(element).removeClass('ap_height_min');
	if(width<700){
			$(element).addClass('ap_width_min');
	}else{
	$(element).addClass('ap_width');		
	}

	switch_acordion = true;
	var colS = (width - 10) / (maxCol+4);
	
	var c = get_proportion(height, 100);
	$(element).find('.ap_slide').css('width', (colS*4)+'px');
	$(element).find('.ap_img').each(function(e,i){
		$(i).css('width', (colS*4)+'px');
		$(i).css('height', c+'px');
	});
	$(element).find('.ap_plug').each(function(e,i){
		$(i).css('width', colS+'px');
		$(i).css('height', c+'px');
	});	

}

function resize_image_max_height(element, height, width, maxCol){
	$(element).removeClass('ap_width_min');
	$(element).removeClass('ap_width');
	if (width<1024){
		$(element).addClass('ap_height_min');
	}else{
			$(element).addClass('ap_height');
	}
	$('.cycle-slideshow').insertAfter($('.ap_col_first')); 
	switch_acordion = false;
	
	var colS = (width - 10) / (maxCol);
	var p = get_proportion(height, 60);
	$(element).find('.ap_slide').css('height', ((p/4)*3)+'px');
	$(element).find('.ap_img').each(function(e,i){
		$(i).css('height', ((p/4)*2)+'px');
		$(i).css('width', width+'px');
	});
	$(element).find('.ap_plug').each(function(e,i){
		$(i).css('width', colS+'px');
		$(i).css('height', (p/4)+'px');
	});	

}

function resize_image(element){
		
	var height =  $(element).height() || $(window).height();
	var width = $(element).width() || $(window).width();
	var maxCol = $(element).data( "maxcol");

	if(height > width){
		resize_image_max_height(element, height, width, maxCol);
	}else{
		resize_image_max_width(element, height, width, maxCol);
	}
	
	$('.cycle-overlay').each(function(e,i){
		$(i).css('width', $(i).parent().width()-30);
	});
}


