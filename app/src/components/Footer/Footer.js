import React from "react";
import styles from "./Footer.module.scss";
import { Link } from "react-router-dom";

function Footer() {
  return (
    <div className={styles.wrapper}>
      <Link
        to="https://github.com/jakemackerracher/code-example-python-react"
        target="_blank"
      >
        GitHub repository
      </Link>
    </div>
  );
}

export default Footer;
