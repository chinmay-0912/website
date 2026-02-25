"use client";

import { useState } from "react";
import Link from "next/link";

export default function AuthPage() {
  const [isLogin, setIsLogin] = useState(true);

  return (
    <section className="min-h-screen flex items-center justify-center px-6 text-white">

      <div className="w-full max-w-md border border-gray-700 rounded-xl p-10">

        {/* Header */}
        <div className="mb-8 text-center">
          <h1 className="text-3xl font-semibold mb-2">
            {isLogin ? "Login" : "Create Account"}
          </h1>
          <p className="text-gray-400 text-sm">
            {isLogin
              ? "Access your account"
              : "Sign up to create an account"}
          </p>
        </div>

        {/* Form */}
        <form className="space-y-6">

          {!isLogin && (
            <div>
              <label className="block text-sm text-gray-400 mb-2">
                Full Name
              </label>
              <input
                type="text"
                className="w-full bg-transparent border border-gray-600 rounded-md px-4 py-3 focus:outline-none focus:border-white transition"
              />
            </div>
          )}

          <div>
            <label className="block text-sm text-gray-400 mb-2">
              Email
            </label>
            <input
              type="email"
              className="w-full bg-transparent border border-gray-600 rounded-md px-4 py-3 focus:outline-none focus:border-white transition"
            />
          </div>

          <div>
            <label className="block text-sm text-gray-400 mb-2">
              Password
            </label>
            <input
              type="password"
              className="w-full bg-transparent border border-gray-600 rounded-md px-4 py-3 focus:outline-none focus:border-white transition"
            />
          </div>

          {!isLogin && (
            <div>
              <label className="block text-sm text-gray-400 mb-2">
                Confirm Password
              </label>
              <input
                type="password"
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
            className="w-full border border-gray-500 py-3 rounded-md hover:bg-white hover:text-black transition duration-300"
          >
            {isLogin ? "Login" : "Sign Up"}
          </button>
        </form>

        {/* Toggle */}
        <div className="mt-8 text-center text-sm text-gray-400">
          {isLogin ? (
            <>
              Don’t have an account?{" "}
              <button
                onClick={() => setIsLogin(false)}
                className="text-white hover:underline"
              >
                Sign up
              </button>
            </>
          ) : (
            <>
              Already registered?{" "}
              <button
                onClick={() => setIsLogin(true)}
                className="text-white hover:underline"
              >
                Sign in
              </button>
            </>
          )}
        </div>

      </div>
    </section>
  );
}