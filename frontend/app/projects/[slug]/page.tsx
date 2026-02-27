import { projects } from "@/data/projectsData";
import { notFound } from "next/navigation";

export default async function ProjectDetail({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;

  const project = projects.find((p) => p.slug === slug);

  if (!project) return notFound();

  return (
    <section className="max-w-4xl mx-auto py-24 px-6 text-white">
      <h1 className="text-3xl font-semibold mb-6">
        {project.title}
      </h1>

      <div className="space-y-10 text-gray-300">

        <Section title="Problem">
          {project.problem}
        </Section>

        <Section title="Architecture">
          {project.architecture}
        </Section>

        <Section title="Your Contribution">
          {project.role}
        </Section>

        <Section title="Impact">
          {project.impact}
        </Section>

        <Section title="Key Learnings">
          {project.lessons}
        </Section>

      </div>
    </section>
  );
}

function Section({
  title,
  children,
}: {
  title: string;
  children: React.ReactNode;
}) {
  return (
    <div>
      <h2 className="text-xl font-medium mb-2 text-white">
        {title}
      </h2>
      <p className="leading-relaxed">
        {children}
      </p>
    </div>
  );
}