import { useState } from 'react'
import Index from "./Index.tsx"
import Title from "../components/Title.tsx"
import SignUp from "./signup.tsx"
import Login from "./login.tsx"
import { BrowserRouter, Routes, Route } from "react-router-dom";

// Contains browser routes for the frontend
function App() {
  // This is a frontend solution to a backend problem, and should not be used in production...
  return (
    <BrowserRouter>
      <Title />
      <Routes>
        <Route path="/" element={<Index />} />
        <Route path="/signup" element={<SignUp />} />
        <Route path="/login" element={<Login />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
