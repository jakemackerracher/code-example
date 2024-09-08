import axios from "axios";

export default axios.create({
  // TODO: fix env variables not working
  baseURL: "http://127.0.0.1:5000/",
  withCredentials: true,
});
