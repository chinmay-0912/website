import Link from "next/link";
import { blogs } from "@/data/blogData";

export default function BlogPage() {
  return (
    <section className="max-w-4xl mx-auto py-24 px-6 text-white">

      {/* Header */}
      <div className="mb-16">
        <h1 className="text-4xl font-semibold mb-4">
          Blog
        </h1>
        <p className="text-gray-300 max-w-2xl">
          Thoughts on data engineering, architecture, system design,
          and career growth.
        </p>
      </div>

      {/* Stacked Blog Cards */}
      <div className="flex flex-col space-y-8">

        {blogs.map((blog) => (
          <Link
            key={blog.slug}
            href={`/blog/${blog.slug}`}
            className="
              border border-gray-700
              rounded-xl
              p-8
              hover:border-gray-500
              transition duration-300
              group
            "
          >

            <div className="flex justify-between items-center mb-4 text-sm text-gray-400">
              <span>{blog.date}</span>
              <span>{blog.readTime}</span>
            </div>

            <h2 className="text-2xl font-semibold mb-4 group-hover:text-gray-200 transition">
              {blog.title}
            </h2>

            <p className="text-gray-300 leading-relaxed">
              {blog.excerpt}
            </p>

          </Link>
        ))}

      </div>

    </section>
  );
}