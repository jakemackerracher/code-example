import React from "react";
import styles from "./Header.module.scss";
import { Link } from "react-router-dom";
import { useAuth } from "../../authContext";

function Header() {
  const { authState, logout } = useAuth();

  return (
    <div className={styles.wrapper}>
      <div className={styles.title}>
        <Link to="/">CODE-EXAMPLE</Link>
      </div>
      <nav className={styles.links}>
        {!authState ? (
          <>
            <Link to="/login">Login</Link>
            <Link to="/register">Register</Link>
          </>
        ) : (
          <>
            <Link onClick={logout}>Logout</Link>
          </>
        )}
      </nav>
    </div>
  );
}

export default Header;
