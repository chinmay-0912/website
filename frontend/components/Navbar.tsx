"use client";

import React, { useState, useRef, useEffect } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation"; // ⭐ added
import { useAuth } from "@/context/AuthContext";

const Navbar = () => {
  const { user, loading, logout } = useAuth(); // ⭐ single destructure
  const router = useRouter(); // ⭐ moved up

  const [isOpen, setIsOpen] = useState(false);
  const dropdownRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const handleClickOutside = (e: MouseEvent) => {
      if (
        dropdownRef.current &&
        !dropdownRef.current.contains(e.target as Node)
      ) {
        setIsOpen(false);
      }
    };

    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  return (
    <nav className="bg-gray-900 text-white px-6 py-4 flex justify-between items-center relative">
      <div className="text-xl font-bold">
        <Link href="/">MyPortfolio</Link>
      </div>

      <div className="space-x-4 flex items-center">
        <Link href="/about" className="hover:text-gray-300">About</Link>
        <Link href="/projects" className="hover:text-gray-300">Projects</Link>
        <Link href="/blog" className="hover:text-gray-300">Blog</Link>
        <Link href="/contact" className="hover:text-gray-300">Contact</Link>

        {loading ? (
          <span className="text-gray-400 animate-pulse">...</span>
        ) : user ? (
          <div className="relative" ref={dropdownRef}>
            <button
              onClick={() => setIsOpen(!isOpen)}
              className="text-gray-300 hover:text-white focus:outline-none transition-colors"
            >
              {user.name} ▾
            </button>

            {isOpen && (
              <div className="absolute right-0 mt-2 w-40 bg-white text-gray-900 rounded shadow-lg py-2 z-50">
                <Link
                  href="/dashboard"
                  className="block px-4 py-2 hover:bg-gray-100"
                  onClick={() => setIsOpen(false)}
                >
                  Dashboard
                </Link>

                <button
                  onClick={async () => {
                    await logout();     // ⭐ backend + state reset
                    setIsOpen(false);
                    router.push("/");
                  }}
                  className="block w-full text-left px-4 py-2 hover:bg-gray-100 text-red-600"
                >
                  Logout
                </button>
              </div>
            )}
          </div>
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