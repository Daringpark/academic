import React, { useState } from 'react'
import NaverLogo from './../assets/images/naver_logo.png'
import { FaSearch, FaSun, FaMoon } from "react-icons/fa";


function Header() {
  const [toggle, setToggle] = useState(false)


  return (
    <div id='header' className='flex items-center p-3 w-full'>
      {/* Logo Section */}
      <div>
        <p className='text-green-600 text-3xl w-40'>React Com.</p>
      {/* <img src={NaverLogo} alt="naver_logo" width = {120} /> */}
      </div>
      {/* Search Bar */}
      <div className='flex bg-slate-200 p-2 w-full mx-5 rounded-full items-center'>
        <FaSearch className='mx-3' />
        <input type="text" placeholder='Search Your Products' className='bg-transparent outline-none w-full'/>
      </div>
      {/* Dark Mode Button */}
      <div className='text-[32px] bg-slate-200 text-black rounded-full p-2' onClick={() => {
        setToggle(!toggle)
      }}>
        {toggle? <FaMoon/> : <FaSun/>}
      </div>
    </div>
  )
}

export default Header