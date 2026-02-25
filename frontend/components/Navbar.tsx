// frontend/components/Navbar.tsx
"use client";

import React from "react";
import Link from "next/link";
import { useAuth } from "@/context/AuthContext";

const Navbar = () => {
  const { user, loading } = useAuth();

  return (
    <nav className="bg-gray-900 text-white px-6 py-4 flex justify-between items-center">
      <div className="text-xl font-bold">
        <Link href="/">MyPortfolio</Link>
      </div>

      <div className="space-x-4">
        <Link href="/about" className="hover:text-gray-300">About</Link>
        <Link href="/projects" className="hover:text-gray-300">Projects</Link>
        <Link href="/blog" className="hover:text-gray-300">Blog</Link>
        <Link href="/contact" className="hover:text-gray-300">Contact</Link>

        {loading ? (
          <span className="text-gray-400 animate-pulse">...</span>
        ) : user ? (
          <span className="text-gray-300">{user.name}</span>
        ) : (
          <Link href="/login" className="hover:text-gray-300">
            Login
          </Link>
        )}
      </div>
    </nav>
  );
};

export default Navbar;