import React, { createContext, useContext, useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import api from "./lib/api";

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const onLoginRedirectUrl = "/";
  const onLogoutRedirectUrl = "/login";

  const [authState, setAuthState] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    checkAuth();
  }, []);

  const checkAuth = async () => {
    try {
      api
        .get("/auth/user")
        .then(function (response) {
          const user = response?.data;
          setAuthState(user || null);
        })
        .catch(function (error) {
          setAuthState(null);
        });
    } catch (error) {
      setAuthState(null);
    }
  };

  const getAPIError = (error) => {
    const defaultError = "Something went wrong, please try again.";
    return error?.response?.data?.error || defaultError;
  };

  const login = async ({ email, password, onSuccess, onError }) => {
    try {
      api
        .post("/auth/login", {
          email,
          password,
        })
        .then(async function (response) {
          await checkAuth();
          onSuccess ? onSuccess?.() : navigate(onLoginRedirectUrl);
        })
        .catch(async function (response) {
          await checkAuth();
          onError?.(getAPIError(response));
        });
    } catch (error) {
      await checkAuth();
      onError?.(error);
    }
  };

  const register = async ({ name, email, password, onSuccess, onError }) => {
    try {
      api
        .post("/auth/register", {
          name,
          email,
          password,
        })
        .then(async function (response) {
          await checkAuth();
          onSuccess ? onSuccess?.() : navigate(onLoginRedirectUrl);
        })
        .catch(async function (response) {
          await checkAuth();
          onError?.(getAPIError(response));
        });
    } catch (error) {
      await checkAuth();
      onError?.(error);
    }
  };

  const logout = async ({ onSuccess, onError }) => {
    try {
      api
        .get("/auth/logout")
        .then(async function (response) {
          await checkAuth();
          onSuccess ? onSuccess?.() : navigate(onLogoutRedirectUrl);
        })
        .catch(async function (response) {
          await checkAuth();
          onError?.(getAPIError(response));
        });
    } catch (error) {
      await checkAuth();
      onError?.(error);
    }
  };

  return (
    <AuthContext.Provider
      value={{
        authState,
        login,
        register,
        logout,
        onLoginRedirectUrl,
        onLogoutRedirectUrl,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
