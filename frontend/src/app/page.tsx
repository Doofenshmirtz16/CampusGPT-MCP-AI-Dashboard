import ChatBox from "@/components/ChatBox";

<footer className="mt-12 text-center text-gray-500 text-sm">
  CampusGPT • MCP + Gemini + RAG + Neon PostgreSQL
</footer>

export default function Home() {
  return (
    <main className="min-h-screen p-10 max-w-4xl mx-auto">

      <div className="mb-8">
        <h1 className="text-5xl font-bold">
          CampusGPT
        </h1>

        <p className="text-gray-500 mt-2">
          AI-powered Campus Assistant using MCP and RAG
        </p>
      </div>

      <ChatBox />

    </main>
  );
}