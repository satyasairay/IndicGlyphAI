import { PropsWithChildren } from "react";

const Layout = ({ children }: PropsWithChildren) => {
  return (
    <div className="min-h-screen bg-slate-950 text-slate-100">
      <header className="border-b border-slate-800 bg-slate-900">
        <div className="mx-auto flex max-w-6xl items-center justify-between px-6 py-4">
          <div>
            <p className="text-xs uppercase tracking-widest text-slate-400">DatasetForge</p>
            <h1 className="text-xl font-semibold text-white">OCR & Annotation Console</h1>
          </div>
          <span className="rounded-full border border-primary-500 px-3 py-1 text-xs font-semibold text-primary-500">
            Cluster 1 Foundation
          </span>
        </div>
      </header>
      <main className="mx-auto max-w-6xl px-6 py-10">{children}</main>
    </div>
  );
};

export default Layout;
