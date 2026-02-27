import { projects } from "@/data/projectsData";
import ProjectCard from "@/components/ProjectCard";

export default function ProjectsPage() {
  return (
    <section className="max-w-6xl mx-auto py-24 px-6">

      {/* Hero */}
      <div className="mb-16">
        <h1 className="text-4xl font-semibold text-white mb-4">
          Projects
        </h1>
        <p className="text-gray-300 max-w-2xl">
          Selected systems and engineering work focused on scalability,
          performance optimization, and data reliability.
        </p>
      </div>

      {/* Grid */}
      <div className="grid md:grid-cols-2 gap-10">
        {projects.map((project) => (
          <ProjectCard key={project.slug} project={project} />
        ))}
      </div>

    </section>
  );
}