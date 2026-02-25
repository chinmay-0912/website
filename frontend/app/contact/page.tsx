import Link from "next/link";

export default function ContactPage() {
  return (
    <section className="max-w-4xl mx-auto py-24 px-6 text-white">

      {/* Header */}
      <div className="mb-16">
        <h1 className="text-4xl font-semibold mb-4">
          Contact
        </h1>
        <p className="text-gray-300 max-w-2xl">
          Open to discussing data engineering roles, system design,
          optimization challenges, and scalable architecture problems.
        </p>
      </div>

      {/* Contact Cards */}
      <div className="grid md:grid-cols-2 gap-8 mb-20">

        {/* Email */}
        <div className="border border-gray-700 rounded-xl p-8 hover:border-gray-500 transition duration-300">
          <h2 className="text-lg font-medium mb-3">
            Email
          </h2>
          <p className="text-gray-400 mb-4">
            For professional inquiries or collaborations.
          </p>
          <a
            href="mailto:chinmayagarwal123@gmail.com"
            className="text-gray-200 underline underline-offset-4 hover:text-white transition"
          >
            Chinmay_Agarwal
          </a>
        </div>

        {/* LinkedIn */}
        <div className="border border-gray-700 rounded-xl p-8 hover:border-gray-500 transition duration-300">
          <h2 className="text-lg font-medium mb-3">
            LinkedIn
          </h2>
          <p className="text-gray-400 mb-4">
            Connect with me professionally.
          </p>
          <Link
            href="https://www.linkedin.com/in/chinmay-agarwal-0912/"
            target="_blank"
            className="text-gray-200 underline underline-offset-4 hover:text-white transition"
          >
            LinkedIN_Profile_Chinmay_Agarwal
          </Link>
        </div>

      </div>

      {/* Minimal Contact Form */}
      <div className="border border-gray-700 rounded-xl p-10">
        <h2 className="text-xl font-medium mb-8">
          Send a Message
        </h2>

        <form className="space-y-6">

          <div>
            <label className="block text-sm text-gray-400 mb-2">
              Name
            </label>
            <input
              type="text"
              className="w-full bg-transparent border border-gray-600 rounded-md px-4 py-3 focus:outline-none focus:border-white transition"
            />
          </div>

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
              Message
            </label>
            <textarea
              rows={5}
              className="w-full bg-transparent border border-gray-600 rounded-md px-4 py-3 focus:outline-none focus:border-white transition"
            />
          </div>

          <button
            type="submit"
            className="border border-gray-500 px-6 py-3 rounded-md hover:bg-white hover:text-black transition duration-300"
          >
            Send Message
          </button>

        </form>
      </div>

    </section>
  );
}