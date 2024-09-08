import React, { useState } from "react";
import styles from "./Login.module.scss";
import { Link, useNavigate } from "react-router-dom";
import api from "../lib/api";

function Login() {
  const navigate = useNavigate();

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

    try {
      api
        .post("/auth/login", {
          email,
          password,
        })
        .then(function (response) {
          navigate("/");
        })
        .catch(function (error) {
          setError(
            error?.response?.data?.error ||
              "Something went wrong, please try again."
          );
        });
    } catch (error) {
      setError(error);
    }
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
