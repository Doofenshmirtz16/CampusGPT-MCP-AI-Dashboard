type Props = {
  tool: string;
};

export default function ToolBadge({
  tool,
}: Props) {
  return (
    <span
      className="
      bg-blue-50
      text-blue-700
      border
      border-blue-200
      px-3
      py-1
      rounded-full
      text-sm
      "
    >
      {tool.charAt(0).toUpperCase() + tool.slice(1)}
    </span>
  );
}