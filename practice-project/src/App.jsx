import { useState } from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import './App.css'
import Home from './pages/Home'
import Header from './components/Header'
import Product from './pages/Product'

function App() {

  return (
    <div className='App flex flex-col items-center'>
      <Header/>
      <Home/>
      <Product/>
    </div>
  )
}

export default App
