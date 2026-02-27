import { blogs } from "@/data/blogData";
// const res = await fetch(`${API_URL}/blogs`); -- when changing source to backend API, use this instead of importing from data file
import { notFound } from "next/navigation";

export default async function BlogDetail({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;

  const blog = blogs.find((b) => b.slug === slug);

  if (!blog) return notFound();

  return (
    <section className="max-w-3xl mx-auto py-24 px-6 text-white">

      <div className="mb-10">
        <div className="text-sm text-gray-400 mb-4">
          {blog.date} • {blog.readTime}
        </div>

        <h1 className="text-3xl font-semibold">
          {blog.title}
        </h1>
      </div>

      <article className="prose prose-invert max-w-none text-gray-300 whitespace-pre-line leading-relaxed">
        {blog.content}
      </article>

    </section>
  );
}