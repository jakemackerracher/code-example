import React from "react";
import { useAuth } from "../authContext";
import styles from "./Home.module.scss";

function Home() {
  const { authState } = useAuth();

  return (
    <div className={styles.wrapper}>
      <h2 className={styles.welcome}>
        Hello {authState?.name || "Guest"}, welcome to my code-example.
      </h2>
      {authState && (
        <div className={styles.user_attributes}>
          <h3>User Attributes</h3>
          <div>
            Name: {authState?.name}
            {authState?.is_admin ? " [ADMIN]" : null}
          </div>
          <div>Email: {authState?.email}</div>
          <div>Created: {authState?.created_at}</div>
        </div>
      )}
    </div>
  );
}

export default Home;
