import Sidebar from "@/components/Sidebar";
import FileExplorer from "@/components/FileExplorer";
import EditorPanel from "@/components/EditorPanel";
import ChatPanel from "@/components/ChatPanel";

export default function Home() {
  return (
    <main className="flex h-screen bg-black">
      <Sidebar />
      <FileExplorer />
      <EditorPanel />
      <ChatPanel />
    </main>
  );
}