// frontend/components/Footer.tsx
import React from "react";

const Footer = () => {
  return (
    <footer className="bg-gray-900 text-white py-6 text-center">
      <p className="text-sm">
        &copy; {new Date().getFullYear()} MyPortfolio. All rights reserved.
      </p>
      <p className="text-sm mt-2">
        Built with <span className="font-bold">Next.js</span> & <span className="font-bold">Tailwind CSS</span>
      </p>
    </footer>
  );
};

export default Footer;