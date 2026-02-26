"use client";

import { useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { apiFetch } from "../../lib/api";

export default function AuthPage() {
  const [isLogin, setIsLogin] = useState(true);
  const router = useRouter();

  // 1. Add state for inputs and feedback
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    password: "",
    confirmPassword: "",
  });
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  // 2. Handle form submission
  const handleSubmit = async (e: React.FormEvent) => {
  e.preventDefault();
  setError("");
  setLoading(true);

  try {
    const { email, password, name } = formData;

    if (isLogin) {
      // LOGIN: Query String Params (e.g., /auth/login?email=...)
      const endpoint = `/auth/login?email=${encodeURIComponent(email)}&password=${encodeURIComponent(password)}`;

      await apiFetch(endpoint, {
        method: "POST"
        // No body here
      });

      router.push("/dashboard");
    } else {
      // REGISTER: JSON Body (e.g., /auth/register with payload)
      await apiFetch("/auth/register", {
        method: "POST",
        body: JSON.stringify({
          email: email,
          password: password,
          name: name || "New User"
        }),
      });

      // After successful registration, switch to login view
      setIsLogin(true);
      alert("Registration successful! Please login.");
    }
  } catch (err: any) {
    setError(err.message);
  } finally {
    setLoading(false);
  }
};

  return (
    <section className="min-h-screen flex items-center justify-center px-6 text-white">
      <div className="w-full max-w-md border border-gray-700 rounded-xl p-10">

        {/* Header */}
        <div className="mb-8 text-center">
          <h1 className="text-3xl font-semibold mb-2">
            {isLogin ? "Login" : "Create Account"}
          </h1>
          <p className="text-gray-400 text-sm">
            {isLogin ? "Access your account" : "Sign up to create an account"}
          </p>
          {error && <p className="text-red-500 text-xs mt-2">{error}</p>}
        </div>

        {/* Form - Added onSubmit */}
        <form className="space-y-6" onSubmit={handleSubmit}>

          {!isLogin && (
            <div>
              <label className="block text-sm text-gray-400 mb-2">Full Name</label>
              <input
                type="text"
                required
                value={formData.name}
                onChange={(e) => setFormData({...formData, name: e.target.value})}
                className="w-full bg-transparent border border-gray-600 rounded-md px-4 py-3 focus:outline-none focus:border-white transition"
              />
            </div>
          )}

          <div>
            <label className="block text-sm text-gray-400 mb-2">Email</label>
            <input
              type="email"
              required
              value={formData.email}
              onChange={(e) => setFormData({...formData, email: e.target.value})}
              className="w-full bg-transparent border border-gray-600 rounded-md px-4 py-3 focus:outline-none focus:border-white transition"
            />
          </div>

          <div>
            <label className="block text-sm text-gray-400 mb-2">Password</label>
            <input
              type="password"
              required
              value={formData.password}
              onChange={(e) => setFormData({...formData, password: e.target.value})}
              className="w-full bg-transparent border border-gray-600 rounded-md px-4 py-3 focus:outline-none focus:border-white transition"
            />
          </div>

          {!isLogin && (
            <div>
              <label className="block text-sm text-gray-400 mb-2">Confirm Password</label>
              <input
                type="password"
                required
                value={formData.confirmPassword}
                onChange={(e) => setFormData({...formData, confirmPassword: e.target.value})}
                className="w-full bg-transparent border border-gray-600 rounded-md px-4 py-3 focus:outline-none focus:border-white transition"
              />
            </div>
          )}

          {isLogin && (
            <div className="text-right">
              <Link
                  href="/forgot-password"
                  className="text-sm text-gray-400 hover:text-white transition"
                >
                  Forgot password?
              </Link>
            </div>
          )}

          <button
            type="submit"
            disabled={loading}
            className="w-full border border-gray-500 py-3 rounded-md hover:bg-white hover:text-black transition duration-300 disabled:opacity-50"
          >
            {loading ? "Processing..." : isLogin ? "Login" : "Sign Up"}
          </button>
        </form>

        {/* Toggle */}
        <div className="mt-8 text-center text-sm text-gray-400">
          {isLogin ? (
            <>
              Don’t have an account?{" "}
              <button onClick={() => { setIsLogin(false); setError(""); }} className="text-white hover:underline">
                Sign up
              </button>
            </>
          ) : (
            <>
              Already registered?{" "}
              <button onClick={() => { setIsLogin(true); setError(""); }} className="text-white hover:underline">
                Sign in
              </button>
            </>
          )}
        </div>
      </div>
    </section>
  );
}