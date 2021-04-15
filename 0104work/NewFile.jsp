<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<a id="navi" href="#" onclick="navi();">
  <img
    src="https://developers.kakao.com/assets/img/about/buttons/navi/kakaonavi_btn_medium.png"
  />
</a>
<script type="text/javascript">
  function navi() {
    Kakao.Navi.start({
      name: '현대백화점 판교점',
      x: 127.11205203011632,
      y: 37.39279717586919,
      coordType: 'wgs84',
    })
  }
</script>

</body>
</html>