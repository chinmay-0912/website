"use client";

import { createContext, useContext, useEffect, useState } from "react";
import { apiFetch } from "@/lib/api";

type User = {
  id: string;
  name: string;
  email: string;
};

type AuthContextType = {
  user: User | null;
  loading: boolean;
  refreshUser: () => Promise<void>;
  logout: () => Promise<void>;
};

const AuthContext = createContext<AuthContextType | null>(null);

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  async function fetchUser() {
    try {
      const data = await apiFetch<User>("/auth/me");
      setUser(data);
    } catch {
      setUser(null);
    } finally {
      setLoading(false);
    }
  }

  async function refreshUser() {
    setLoading(true);
    await fetchUser();
  }

  async function logout() {
    try {
      await apiFetch("/auth/logout", { method: "POST" });
    } catch {}

    setUser(null);
    setLoading(false); // ⭐ important
  }

  useEffect(() => {
    fetchUser(); // ⭐ initial load only
  }, []);

  return (
    <AuthContext.Provider value={{ user, loading, refreshUser, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (!context) throw new Error("useAuth must be used inside AuthProvider");
  return context;
}