import { useEffect, useState } from "react";
import axios from "axios";

type SettingsPayload = {
  app_name: string;
  cors_origins: string[];
  environment: string;
  s3_bucket: string;
  s3_endpoint_url: string | null;
  version: string;
};

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8000";

const HomePage = () => {
  const [settings, setSettings] = useState<SettingsPayload | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    axios
      .get<SettingsPayload>(`${API_BASE_URL}/api/settings`)
      .then((response) => setSettings(response.data))
      .catch((err) => {
        setError(err.message);
      });
  }, []);

  return (
    <section className="space-y-6">
      <div className="rounded-lg border border-slate-800 bg-slate-900/70 p-6 shadow-lg">
        <h2 className="text-lg font-semibold text-white">Platform Bootstrap Checklist</h2>
        <p className="mt-2 text-sm text-slate-300">
          Cluster 1 establishes the foundations for DatasetForge. The checklist updates in real time
          as services respond.
        </p>
      </div>

      <div className="grid gap-4 lg:grid-cols-3">
        <ChecklistCard
          title="FastAPI + PostgreSQL"
          description="Backend container runs with database connectivity check on startup."
          status={settings ? "Ready" : error ? "Error" : "Pending"}
        />
        <ChecklistCard
          title="React + Tailwind"
          description="Frontend served via Vite with Tailwind styling."
          status="Ready"
        />
        <ChecklistCard
          title="S3/MinIO"
          description="Object store connectivity configured via environment variables."
          status={settings?.s3_endpoint_url ? "Ready" : "Pending"}
        />
      </div>

      <div className="rounded-lg border border-slate-800 bg-slate-900/70 p-6 shadow-lg">
        <h3 className="text-base font-semibold text-white">Runtime Settings Snapshot</h3>
        {error && <p className="mt-2 text-sm text-red-400">Failed to load settings: {error}</p>}
        {settings ? (
          <dl className="mt-4 grid gap-3 sm:grid-cols-2">
            <Entry label="App Name" value={settings.app_name} />
            <Entry label="Environment" value={settings.environment} />
            <Entry label="Version" value={settings.version} />
            <Entry label="CORS Origins" value={settings.cors_origins.join(", ")} />
            <Entry label="S3 Bucket" value={settings.s3_bucket} />
            <Entry
              label="S3 Endpoint"
              value={settings.s3_endpoint_url ?? "Configured via IAM/Default Endpoint"}
            />
          </dl>
        ) : (
          !error && <p className="mt-2 text-sm text-slate-400">Loading settings...</p>
        )}
      </div>
    </section>
  );
};

type ChecklistCardProps = {
  title: string;
  description: string;
  status: "Ready" | "Pending" | "Error";
};

const STATUS_STYLES: Record<ChecklistCardProps["status"], string> = {
  Ready: "bg-emerald-500/10 text-emerald-300 border-emerald-500/40",
  Pending: "bg-amber-500/10 text-amber-300 border-amber-500/40",
  Error: "bg-rose-500/10 text-rose-300 border-rose-500/40",
};

const ChecklistCard = ({ title, description, status }: ChecklistCardProps) => {
  return (
    <article className="rounded-lg border border-slate-800 bg-slate-900/70 p-5 shadow">
      <div className="flex items-center justify-between">
        <h4 className="text-base font-semibold text-white">{title}</h4>
        <span
          className={`rounded-full border px-2 py-0.5 text-xs font-semibold uppercase tracking-wide ${STATUS_STYLES[status]}`}
        >
          {status}
        </span>
      </div>
      <p className="mt-3 text-sm text-slate-300">{description}</p>
    </article>
  );
};

const Entry = ({ label, value }: { label: string; value: string }) => {
  return (
    <div>
      <dt className="text-xs uppercase tracking-widest text-slate-500">{label}</dt>
      <dd className="text-sm font-medium text-slate-200">{value}</dd>
    </div>
  );
};

export default HomePage;
