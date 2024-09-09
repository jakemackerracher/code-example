import React, { useState } from "react";
import styles from "./Login.module.scss";
import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../authContext";

function Login() {
  const { login, authState, onLoginRedirectUrl } = useAuth();
  const navigate = useNavigate();

  // Redirect if already logged in
  if (authState) {
    navigate(onLoginRedirectUrl);
  }

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    // Clear previous error
    setError("");

    // Ensure we have the required fields
    if (!email && !password) {
      setError("Email and password required");
      return;
    }

    login({
      email,
      password,
      onError: (error) => {
        setError(error);
      },
    });
  };

  return (
    <div className={styles.wrapper}>
      <h2>Login</h2>
      {error && <p>{error}</p>}
      <form onSubmit={handleSubmit} className={styles.form}>
        <input
          type="email"
          id="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="Email"
          required={true}
        />
        <input
          type="password"
          id="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="Password"
          required={true}
        />
        <button type="submit">Login</button>
        <div className={styles.register_here}>
          Don't have an account yet? Create one <Link to="/register">here</Link>
          .
        </div>
      </form>
    </div>
  );
}

export default Login;
