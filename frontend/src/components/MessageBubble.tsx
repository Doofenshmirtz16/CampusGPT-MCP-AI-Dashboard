type Props = {
  role: "user" | "assistant";
  content: string;
};

import ReactMarkdown from "react-markdown";

export default function MessageBubble({
  role,
  content,
}: Props) {
  const isUser = role === "user";

  return (
    <div
      className={`flex ${
        isUser ? "justify-end" : "justify-start"
      }`}
    >
      <div
        className={`
          max-w-[80%]
          px-4
          py-3
          rounded-2xl
          shadow-sm
          whitespace-pre-wrap
          ${
            isUser
              ? "bg-blue-500 text-white"
              : "bg-gray-100 text-black"
          }
        `}
      >
        <ReactMarkdown>{content}</ReactMarkdown>
      </div>
    </div>
  );
}