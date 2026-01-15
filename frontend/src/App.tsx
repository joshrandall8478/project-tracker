import { useState } from 'react'
import Index from "./Index.tsx"
import './App.css'
import { BrowserRouter, Routes, Route } from "react-router-dom";

function App() {
  // This is a frontend solution to a backend problem, and should not be used in production.....
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Index />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
