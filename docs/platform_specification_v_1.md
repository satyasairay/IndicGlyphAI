# IndicGlyph AI and OCR Platform Specification (Powered by Taapset Technologies)
**Version:** 1.0  
**Owner:** [Satyasai Ray]  
**Date:** [22-10-2025]  

---

IndicGlyph AI and OCR is a full-stack, mobile-first platform for curating multilingual OCR datasets, powered by Taapset Technologies.
Admins upload and slice scanned pages; reviewers annotate text, translation, phonetics, and meaning.  
Data routes through multiple reviewers, gaining “gold” or “reviewed” status and feeding exportable training datasets.

---

## 🧱 System Overview  

| Layer           | Tech                                         |
|------------------|-----------------------------------------------|
| **Frontend**     | React, Tailwind CSS, Konva.js, React Router   |
| **Backend**      | FastAPI, PostgreSQL, Celery/RQ, S3/Minio      |
| **Deployment**   | Docker, NGINX, GitHub Actions                 |
| **OCR Engine**   | Tesseract, EasyOCR, PaddleOCR                 |
| **Optional AI**  | OpenAI API / local LLM                        |
| **Storage**      | S3 or compatible object store                 |
| **Scaling**      | Container-based horizontal scaling            |

---

## ⚙️ Admin Config Panel (Cluster 0)

Editable in UI; persisted in `AppConfig`.

| Setting                        | Default | Editable From Admin? |
|-------------------------------|---------|-----------------------|
| Reviews to "verified"         | 5       | ✅                    |
| Skips to "gold"               | 5       | ✅                    |
| ₹ per 200 reviews             | 200 ₹   | ✅                    |
| XP per review                 | 1       | ✅                    |
| Bonus for full annotation     | 2       | ✅                    |
| Max reviews/day per user      | ∞       | ✅                    |
| Skip ratio ban threshold      | 80%     | ✅                    |
| OCR engine                    | tesseract | ✅                  |

### QA Checklist
- [ ] Config editable from admin panel  
- [ ] Updated values apply in real time  
- [ ] Secure access (admin only)  
- [ ] Fallback to defaults if unset  
- [ ] Invalid inputs rejected  

---

## 🧩 Development Clusters  

Each cluster is modular and scoped for sprint planning.

---

### Cluster 1 – Foundation & Infrastructure  
**Deliverables:**
- Repo with CI/CD  
- FastAPI + PostgreSQL  
- Tailwind + React scaffold  
- Docker setup for local/dev/prod  
- S3/Minio connectivity  
- HTTPS setup  

**QA Checklist:**
- [ ] Containers build and deploy *(blocked: local Docker CLI unavailable)*  
- [x] CI tests run on PR  
- [x] DB migrations apply cleanly  
- [x] .env loads per env  
- [x] HTTPS enforced in staging/prod  

---

### Cluster 2 – Admin Upload & Slicing  
**Deliverables:**
- Upload module (JPG, PNG, PDF)  
- Image slicer (Konva.js)  
- Admin dashboard to view files  
- Box draw, drag, delete, undo  
- Save to backend + coordinate tracking  

**QA Checklist:**
- [ ] File uploads saved and visible  
- [ ] Slice coordinates stored per image  
- [ ] Reslicing works  
- [ ] Slicer usable on tablet and mobile  
- [ ] Error handling for large/invalid files  

---

### Cluster 3 – OCR Integration  
**Deliverables:**
- OCR endpoint `/ocr/slice`  
- Auto-trigger on slice  
- Return text, confidence, language  

**QA Checklist:**
- [ ] OCR triggers on slice submission  
- [ ] OCR errors caught and logged  
- [ ] Confidence < 0.6 flagged visually  
- [ ] OCR retry safe  
- [ ] Support multiple OCR backends  

---

### Cluster 4 – Review Workflow  
**Deliverables:**
- `/tasks/next`, `/submit`, `/skip`  
- Mobile-first annotation UI  
- Fields: OCR text (edit), translation, phonetics, explanation, tags  
- Task routing logic (rotation, gold/verified flags)

**QA Checklist:**
- [ ] Task routing honors skip/review thresholds  
- [ ] Same slice never reassigned to same reviewer  
- [ ] All fields save correctly  
- [ ] Skipped task count increments  
- [ ] UI works on small phones  

---

### Cluster 5 – Gamification & Payouts  
**Deliverables:**
- XP/level system  
- Earnings tracked every 200 reviews  
- Leaderboard (all-time, daily)  
- Reviewer restrictions based on behavior  

**QA Checklist:**
- [ ] XP increases on valid review  
- [ ] Bonus XP for full annotation  
- [ ] Skips give no XP  
- [ ] 200 reviews triggers payout  
- [ ] Skip ratio ban works  

---

### Cluster 6 – Export & Dataset Delivery  
**Deliverables:**
- Admin panel: export filters  
- Export formats: JSON, CSV, ZIP  
- Download system for dataset buyers  

**QA Checklist:**
- [ ] Export filters apply correctly  
- [ ] Schema matches gold/reviewed logic  
- [ ] Exported slices include all metadata  
- [ ] Image ZIP links valid  
- [ ] Export handles large sets  

---

### Cluster 7 – QA & Testing  
**Deliverables:**
- Pytest for backend  
- Cypress or Playwright for E2E  
- Jest for frontend  
- Load test config  
- A11y test pass  

**QA Checklist:**
- [ ] >80% coverage  
- [ ] All tests pass on CI  
- [ ] Mobile UX validated  
- [ ] OCR queue load test runs  
- [ ] Edge cases (timeouts, failures) simulated  

---

### Cluster 8 – Admin Tools & Control Panel  
**Deliverables:**
- Dashboard with stats  
- Slice moderation (force gold, reassign, delete)  
- Audit logs per slice  
- Manual XP override  

**QA Checklist:**
- [ ] Admin actions persist  
- [ ] Audit logs show change history  
- [ ] Slice reassignment works  
- [ ] Non-admins cannot access dashboard  

---

### Cluster 9 – AI Assist (Optional)  
**Deliverables:**
- GPT-based suggest buttons for fields  
- Accept/reject UX  
- AI-assisted flag on review  

**QA Checklist:**
- [ ] Suggestion appears on demand only  
- [ ] Suggestions are not auto-saved  
- [ ] Rejected suggestions discarded  
- [ ] Prompt usage logged  

---

### Cluster 10 – Dataset Access API  
**Deliverables:**
- `/api/gold`, `/api/reviewed`  
- Token-based download access  
- Buyer dashboard (optional)  

**QA Checklist:**
- [ ] Dataset access requires valid token  
- [ ] Filters paginate correctly  
- [ ] Download streams ZIP/JSON  
- [ ] 401/403 handled cleanly  

---

## 🔒 User Roles & Permissions  

### Roles

| Role         | Capabilities                                                   |
|--------------|----------------------------------------------------------------|
| Admin        | All access: upload, slice, config, user mgmt, export           |
| Moderator    | Review override, warnings, view earnings                       |
| Reviewer     | Review tasks, earn rewards                                     |
| Client       | Read-only dataset download                                     |

### Auth & Access
- Default registration = Reviewer  
- JWT-based auth  
- Token refresh  
- Role-based route protection  

---

## 👤 Admin User Management Dashboard  

| Feature              | Purpose                                        |
|----------------------|------------------------------------------------|
| View users           | Name, role, join date, task stats, earnings    |
| Promote/demote       | Change roles                                   |
| Ban/unban            | Disable user temporarily or permanently        |
| Warning log          | Track behavioral issues                        |
| Manual XP edit       | Reward or punish manually                      |
| Reviewer reset       | Wipe task history for debugging/training       |

---

## 🧹 Admin Slice Management Dashboard  

| Feature              | Purpose                                        |
|----------------------|------------------------------------------------|
| Search slices        | By file, status, tags, content                 |
| Audit view           | View all 5 reviews + timestamps                |
| Bulk actions         | Reassign, delete, mark as gold, export         |
| Reopen review        | Send slice back into task queue                |
| Tag manager          | Add/remove slice labels                        |

---

## 🎓 Reviewer Trust System  

| Metric           | Description                                          |
|------------------|------------------------------------------------------|
| XP               | Progress and tier system                             |
| Accuracy         | % alignment with consensus on reviewed slices        |
| Trust Score      | Calculated from accuracy, streak, skip ratio         |
| Tiers            | Novice → Trusted Reviewer → QA Annotator            |
| Auto-flagging    | System bans users with poor scores after threshold   |

---

## 🔐 Audit Logs  

Each admin/mod action logged with:
- User ID  
- Timestamp  
- Action type  
- Target ID (slice, user, config)  
- Old → New value

---

## 🗃️ Data Models (Simplified)

```python
class File(BaseModel):
    id: int
    name: str
    lang: str
    source: str
    path: str

class Slice(BaseModel):
    id: int
    file_id: int
    x: int
    y: int
    w: int
    h: int
    ocr_text: str
    confidence: float
    status: str  # pending / reviewed / gold
    review_count: int
    skip_count: int

class Review(BaseModel):
    id: int
    slice_id: int
    reviewer_id: int
    translation: str
    phonetics: str
    explanation: str
    tags: List[str]
    skipped: bool

class User(BaseModel):
    id: int
    name: str
    role: str
    xp: int
    earnings: float

class Config(BaseModel):
    key: str
    value: Any
```

---

## 🚀 Deployment Pipeline

1. Dev commit → CI → staging auto-deploy
2. Staging approval → production deploy
3. DB migration runs automatically
4. Logs + metrics flow to dashboard
5. Daily backup of DB + S3
6. Rollback via tagged image and Alembic downgrade

---

## ✅ Release Criteria

* [ ] All QA checklists cleared
* [ ] 1000+ reviewed slices tested end-to-end
* [ ] Config panel secured
* [ ] Review routing operates on live thresholds
* [ ] Mobile UX stable
* [ ] Data export validated against buyer schema
* [ ] Admin can fully manage users, config, and slices

---

## 🧠 Glossary

| Term           | Definition                                        |
| -------------- | ------------------------------------------------- |
| Slice          | Cropped image region of text                      |
| Gold Slice     | Skipped ≥ N times (configurable)                  |
| Verified Slice | Reviewed ≥ N times (configurable)                 |
| Reviewer       | Task doer, earns XP and money                     |
| Moderator      | Review manager, not uploader                      |
| Admin          | Full system access                                |
| Task Rotation  | Sending same slice to multiple users sequentially |
| Audit Log      | Record of all sensitive changes/actions           |
| Trust Score    | Measure of reviewer reliability                   |

---

## 🧩 Optional Future Add-ons

* Payment processor integration
* WebSocket task updates
* Reviewer-to-reviewer chat/comments
* Dataset versioning and license tagging
* Semantic search of annotated slices
* OCR model fine-tuning dashboard

---

End of Markdown Document.
