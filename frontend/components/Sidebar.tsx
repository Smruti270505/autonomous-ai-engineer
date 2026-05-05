import { Folder, MessageSquare, Settings } from "lucide-react";

export default function Sidebar() {
  return (
    <div className="w-16 h-screen bg-zinc-900 border-r border-zinc-800 flex flex-col items-center py-4 gap-6 text-white">
      <Folder />
      <MessageSquare />
      <Settings />
    </div>
  );
}