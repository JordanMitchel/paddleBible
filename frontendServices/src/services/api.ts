import axios, { AxiosRequestConfig, AxiosResponse } from "axios";
import { useEffect, useState } from "react";

const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL || "http://localhost:8002"; // your backend port


export const apiGetRequest= (route : string) =>{
  try {
    return axios.get(`${API_BASE_URL}${route}`)
    .then((response: AxiosResponse) => response.data)
    .catch((error) => {
      console.error("API GET request error:", error);
      throw error;
    });
  } catch (error) {
    console.error("API GET request exception:", error);
    throw error;
  }
}



