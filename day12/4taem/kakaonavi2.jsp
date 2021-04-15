<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<%-- <script src="<%=request.getContextPath()%>/js/kakao.js"></script> --%>
<script src="//developers.kakao.com/sdk/js/kakao.min.js"></script>

<!--개발자도구인 sdk를 다운받는다  -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
</head>
<!--js파일을 구글에서 다운받는다  -->
<body>

	<a id="navi" href="#" onclick="navi();"> <img
		src="https://developers.kakao.com/assets/img/about/buttons/navi/kakaonavi_btn_medium.png" />
	</a>
	<!-- 인터넷에서 제공한 카카오 이미지를 넣는다 -->
	
	<script type="text/javascript">
	// 스크립트를 호출해서 위에서 부른 카카오 sdk에 init 키값을 설정
    // 사용할 앱의 JavaScript 키를 설정
    Kakao.init('9e9d66edc5721d9f24c88c29065ae0ac');
    // 카카오 내비 버튼을 생성합니다.
    // 키값이 승인이되면 function navi()가 실행이되면서, 지정된 시작위치 name: 아작스로 들어감 검색이 됨
  function navi() {
    Kakao.Navi.start({
      name: '유성온천역',
      x: 127.34155026922662,
      y: 36.35383823126957,
      coordType: 'wgs84',
    })
  }
</script>
</body>
</html>