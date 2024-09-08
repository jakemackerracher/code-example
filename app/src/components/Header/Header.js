import React from "react";
import styles from "./Header.module.scss";
import { Link } from "react-router-dom";

function Header() {
  return (
    <div className={styles.wrapper}>
      <div className={styles.title}>
        <Link to="/">code-example</Link>
      </div>
      <nav className={styles.links}>
        <Link to="/login">Login</Link>
        <Link to="/register">Register</Link>
      </nav>
    </div>
  );
}

export default Header;
