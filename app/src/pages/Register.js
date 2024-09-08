import React, { useState } from "react";
import styles from "./Register.module.scss";
import { Link } from "react-router-dom";

function Register() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    // Ensure we have the required fields
    if (!name && !email && !password) {
      setError("Name, email and password required");
      return;
    }

    // TODO: connect submit to api
    console.log("Name:", name);
    console.log("Email:", email);
    console.log("Password:", password);

    // Clear form
    setName("");
    setEmail("");
    setPassword("");
    setError("");
  };

  return (
    <div className={styles.wrapper}>
      <h2>Register</h2>
      {error && <p>{error}</p>}
      <form onSubmit={handleSubmit} className={styles.form}>
        <input
          type="text"
          id="name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="Name"
          required={true}
        />
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
        <button type="submit">Register</button>
        <div className={styles.login_here}>
          Already have an account? Login <Link to="/login">here</Link>.
        </div>
      </form>
    </div>
  );
}

export default Register;
