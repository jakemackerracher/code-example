import React from "react";
import styles from "./Footer.module.scss";
import { Link } from "react-router-dom";

function Footer() {
  return (
    <div className={styles.wrapper}>
      GitHub:
      <Link
        to="https://github.com/jakemackerracher/code-example"
        target="_blank"
      >
        jakemackerracher/code-example
      </Link>
    </div>
  );
}

export default Footer;
