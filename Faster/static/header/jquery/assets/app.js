$(document).ready(function() {

    $('body').on('click', "#accounts-button", function (e){
		$(".item-list").show();
		e.stopPropagation();
		$('body').one("click",function(){
			$(".item-list").hide();
		});
	});

    	$('body').on('click', ".darkmode", function (e){
		$(".darkmode .switch").toggleClass("on");
		if(Cookies.get('darkmode')){
			Cookies.remove('darkmode');
		}
		else{
			Cookies.set('darkmode', 'on');
		}
		$('body').toggleClass("dark");
		e.stopPropagation();
	});

	if($(".nano").length>0){
		$(".nano").nanoScroller();
	}

	$('body').on('click', '.Ib-T', function (){
		var nodeid = $(this).attr("nodeid");
		var isfollow = $(this).attr("isfollow");
		var $this = $(this);
		$.post("/do", { c: "node", t: (isfollow==1?"unfollow":"follow"), nodeid:nodeid },function(data){
			if(!data.error){
				$this.attr("isfollow",(isfollow==1?"0":"1"));
				$this.removeClass("Ib-T-"+(isfollow==1?"xc":"yc")).addClass("Ib-T-"+(isfollow==1?"yc":"xc"));

				if($this.hasClass("popover")){
					$this.text(isfollow==1?"璁㈤槄":"宸茶闃�");
					$("#node-"+nodeid).find(".i-o").attr("isfollow",(isfollow==1?"0":"1"));
				}

				if(isfollow==1 && $(document).find(".bc-tc-tb").text()=='鎴戠殑璁㈤槄'){
					$('.i-o').webuiPopover('destroy');
					$("#node-"+nodeid).fadeOut('normal',function(){
						$("#node-"+nodeid).remove();
					});
				}

			}
			else{
				layer.msg(data.msg);
			}
		});

	});


	$('body').on('click', "a[itemid]", function (e){
		var itemid = $(this).attr("itemid");
		$.post("/do", { c: "item", t: "view", itemid:itemid },function(data){});
	});


	$('body').on('click', ".i-o", function (e){
		$(this).webuiPopover('destroy').webuiPopover({
							trigger:'manual',
							title:'鑺傜偣',
							content:'<a class="Ib-T popover" nodeid="'+$(this).attr("nodeid")+'" isfollow="'+$(this).attr("isfollow")+'">'+($(this).attr("isfollow")==1?'宸�':'')+'璁㈤槄</a><a href="/n/'+$(this).attr("hashid")+'">璁块棶鑺傜偣</a><a href="'+$(this).attr("homepage")+'" target="_blank">璁块棶婧愮綉绔�</a>',
							width:'auto',
							multi:false,
							closeable:true,
							style:(Cookies.get('darkmode')?'inverse':''),
							padding:true,
							backdrop:false,
							dismissible:true,
							cache:false,
							animation:'pop'
					}).webuiPopover('show');

	});


});