// frontend/app/page.tsx
import React from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

const HomePage = () => {
  return (
    <div className="flex flex-col min-h-screen">


      {/* Main content */}
      <main className="flex-grow container mx-auto px-4 py-10">
        <h1 className="text-4xl font-bold mb-4">Welcome to My Portfolio</h1>
        <p className="text-lg text-gray-700">
          Hi! I am Chinmay. Explore my projects, blog, and contact me through this site.
        </p>
      </main>

    </div>
  );
};

export default HomePage;