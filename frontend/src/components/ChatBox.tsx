"use client";

import { useState, useRef, useEffect } from "react";

import MessageBubble from "./MessageBubble";
import ToolBadge from "./ToolBadge";

import { askCampusGPT } from "@/services/api";

type Message = {
  role: "user" | "assistant";
  content: string;
};

export default function ChatBox() {
  const [query, setQuery] = useState("");

  const [messages, setMessages] = useState<Message[]>([]);

  const [tools, setTools] = useState<string[]>([]);

  const [loading, setLoading] = useState(false);

  const messagesEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages]);

  async function handleSend() {
    if (!query.trim()) return;

    const currentQuery = query;

    setMessages((prev) => [
      ...prev,
      {
        role: "user",
        content: currentQuery,
      },
    ]);

    setQuery("");
    setLoading(true);
    setTools([]);

    try {
      const result = await askCampusGPT(currentQuery);

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: result.answer,
        },
      ]);

      setTools(result.tools_used || []);
    } catch (error) {
      console.error(error);

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content:
            "Sorry, something went wrong while processing your request.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="space-y-4">
      <label
        htmlFor="query"
        className="block text-sm font-medium"
      >
        Ask CampusGPT
      </label>

      <textarea
        id="query"
        placeholder="Ask about books, events, cafeteria, academic policies, placements..."
        className="w-full border rounded-lg p-3"
        rows={3}
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            handleSend();
          }
        }}
      />

      {/* Suggested Queries */}

      <div className="flex flex-wrap gap-2">
        <button
          onClick={() =>
            setQuery(
              "What AI books are available?"
            )
          }
          className="border rounded-full px-3 py-1 text-sm hover:bg-gray-100"
        >
          📚 AI Books
        </button>

        <button
          onClick={() =>
            setQuery(
              "What workshops are happening this month?"
            )
          }
          className="border rounded-full px-3 py-1 text-sm hover:bg-gray-100"
        >
          📅 Upcoming Events
        </button>

        <button
          onClick={() =>
            setQuery(
              "What is today's lunch menu?"
            )
          }
          className="border rounded-full px-3 py-1 text-sm hover:bg-gray-100"
        >
          🍽 Lunch Menu
        </button>

        <button
          onClick={() =>
            setQuery(
              "What is the placement policy?"
            )
          }
          className="border rounded-full px-3 py-1 text-sm hover:bg-gray-100"
        >
          📖 Placement Policy
        </button>

        <button
          onClick={() =>
            setQuery(
              "What are the internship eligibility rules?"
            )
          }
          className="border rounded-full px-3 py-1 text-sm hover:bg-gray-100"
        >
          🎓 Internship Rules
        </button>
      </div>

      <button
        onClick={handleSend}
        disabled={loading}
        className="bg-black text-white px-4 py-2 rounded-lg disabled:opacity-50"
      >
        {loading ? "Thinking..." : "Send"}
      </button>

      {/* Chat Messages */}

      <div className="space-y-4">
        {messages.map((msg, index) => (
          <MessageBubble
            key={index}
            role={msg.role}
            content={msg.content}
          />
        ))}

        {loading && (
          <MessageBubble
            role="assistant"
            content="Thinking..."
          />
        )}

        <div ref={messagesEndRef}></div>
      </div>

      {/* Tool Badges */}

      {tools.length > 0 && (
        <div className="flex flex-wrap gap-2">
          {tools.map((tool) => (
            <ToolBadge
              key={tool}
              tool={tool}
            />
          ))}
        </div>
      )}
    </div>
  );
}