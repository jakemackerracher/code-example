import React from "react";
import { Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Register from "./pages/Register";
import NotFound from "./pages/NotFound";
import Header from "./components/Header/Header";
import Footer from "./components/Footer/Footer";
import styles from "./App.module.scss";
import { AuthProvider } from "./authContext";

function App() {
  // TODO: add unit tests for entire react application

  return (
    <AuthProvider>
      <div className={styles.wrapper}>
        <Header />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
        <Footer />
      </div>
    </AuthProvider>
  );
}

export default App;
