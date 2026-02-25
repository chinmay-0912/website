"use client";

import Link from "next/link";
import Image from "next/image";

interface Project {
  slug: string;
  title: string;
  description: string;
  tech: string[];
  year: string;
  imageUrl: string;
}

export default function ProjectCard({ project }: { project: Project }) {
  return (
    <Link href={`/projects/${project.slug}`}>
      <div className="group border border-gray-200 rounded-xl overflow-hidden transition-all duration-300 hover:shadow-md hover:-translate-y-1">

        {/* Image */}
        <div className="relative w-full h-52">
          <Image
            src={project.imageUrl}
            alt={project.title}
            fill
            className="object-cover transition duration-500 group-hover:scale-105"
          />
        </div>

        {/* Content */}
        <div className="p-6 bg-white">
          <div className="flex justify-between items-center mb-2">
            <h3 className="text-lg font-semibold text-gray-900">
              {project.title}
            </h3>
            <span className="text-sm text-gray-400">
              {project.year}
            </span>
          </div>

          <p className="text-gray-600 text-sm mb-4">
            {project.description}
          </p>

          {/* Tech Stack */}
          <div className="flex flex-wrap gap-2">
            {project.tech.map((item) => (
              <span
                key={item}
                className="text-xs bg-gray-100 text-gray-700 px-2 py-1 rounded-md"
              >
                {item}
              </span>
            ))}
          </div>
        </div>
      </div>
    </Link>
  );
}