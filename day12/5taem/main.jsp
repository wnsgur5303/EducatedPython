<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script type="text/javascript"
src="https://cdn.iamport.kr/js/iamport.payment-1.1.5.js"></script>
<script type="text/javascript"
src="https://code.jquery.com/jquery-1.12.4.min.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
</head>

<script>
$(function(){
	$('#pay').on('click',function(){
	       var IMP = window.IMP; // 생략가능
//	        IMP.init('TC0ONETIME'); // 'iamport' 대신 부여받은 "가맹점 식별코드"를 사용
	       IMP.init('imp23418340'); // 'iamport' 대신 부여받은 "가맹점 식별코드"를 사용
	       var msg;
	       
	       IMP.request_pay({
	        pg : 'kakaopay',
	           pay_method : 'card',
	           merchant_uid : 'merchant_' + new Date().getTime(),
	           name : '회원권 결제',
	           amount : 100,
	           buyer_email : 'yoonkibabo@naver.com',
	           buyer_name : '강감찬',
	           buyer_tel : '010-3751-7710',
	           buyer_addr : '대전 ',
	           buyer_postcode : '123-456',
	           //m_redirect_url : 'http://www.naver.com'
	       }, function(rsp) {
	           if ( rsp.success ) {
	               //[1] 서버단에서 결제정보 조회를 위해 jQuery ajax로 imp_uid 전달하기
	               jQuery.ajax({
	                   url: "/payments/complete", //cross-domain error가 발생하지 않도록 주의해주세요
	                   type: 'POST',
	                   dataType: 'json',
	                   data: {
	                       imp_uid : rsp.imp_uid,
	                       //기타 필요한 데이터가 있으면 추가 전달
	                   }
	               })
	               //성공시 이동할 페이지
	               msg = '결제가 완료되었습니다.';
	               alert(msg);
	               location.href="Payment.jsp";// 결제성공 페이지 경로 달아주기
	           } else {
	               msg = '결제에 실패하였습니다.  : ';
	               //실패시 이동할 페이지
	               location.href="PayFail.jsp";// 결제성공 페이지 경로 달아주기
	               alert(msg);
	           }
	       })
	       
	   })
	   })


</script>
<body>
<h2>카카오페이 결제</h2>
<input id="pay" type="button" value="결제하기">

</body>
</html>