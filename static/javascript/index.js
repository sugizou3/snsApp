// 画面が小さいときにサイドバーを表示させる
const menu = document.querySelector('#menu');
const sidebar = document.querySelector('.sidebar');

menu.addEventListener('click', function () {
  sidebar.classList.toggle('show-sidebar');
});
// END






// Scroll and Hide filters

var beforePos = 0;//スクロールの値の比較用の設定

//スクロール途中でヘッダーが消え、上にスクロールすると復活する設定を関数にまとめる
function ScrollAnime() {
	var scroll = $(window).scrollTop();
    //ヘッダーの出し入れをする
    if(scroll == beforePos) {
		//IE11対策で処理を入れない
    }else if( 0 > scroll - beforePos){
		//ヘッダーが上から出現する
		$('#filters').removeClass('UpMove');	//#filtersにUpMoveというクラス名を除き
		$('#filters').addClass('DownMove');//#filtersにDownMoveのクラス名を追加
    }else {
		//ヘッダーが上に消える
        $('#filters').removeClass('DownMove');//#filtersにDownMoveというクラス名を除き
		$('#filters').addClass('UpMove');//#filtersにUpMoveのクラス名を追加
    }
    
    beforePos = scroll;//現在のスクロール値を比較用のbeforePosに格納
}


// 画面をスクロールをしたら動かしたい場合の記述
$(window).scroll(function () {
	ScrollAnime();//スクロール途中でヘッダーが消え、上にスクロールすると復活する関数を呼ぶ
});






$(".search").click(function () {
    $(this).toggleClass('btnactive');//.open-btnは、クリックごとにbtnactiveクラスを付与＆除去。1回目のクリック時は付与
    $("#search-wrap").css({'width':'100%' ,'height' : '100vh'})
    $("#search-wrap").toggleClass('panelactive');//#search-wrapへpanelactiveクラスを付与
    $('#search-text').focus();//テキスト入力のinputにフォーカス
    });

$(".close-btn").click(function () {
    $("#search-wrap").removeClass('panelactive');//#search-wrapからpanelactiveクラスを除去
});


function flexTextarea(el) {
  const dummy = el.querySelector('.FlexTextarea__dummy')
  el.querySelector('.FlexTextarea__textarea').addEventListener('input', e => {
    dummy.textContent = e.target.value + '\u200b'
  })
}

document.querySelectorAll('.FlexTextarea').forEach(flexTextarea)









