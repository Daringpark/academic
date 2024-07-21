import React, { useEffect } from 'react'

const {kakao} = window;

function Kakao() {
  useEffect(() => {
      const container = document.getElementById('KakaoMap');
      const options = {
        center: new kakao.maps.LatLng(35.205580, 126.811458),
        level: 3
      };
      const map = new kakao.maps.Map(container, options);
  }, [])

  return (
    <div id="KakaoMap" style={{width: '600px', height: '600px'}}>
    </div>
  )
}

export default Kakao