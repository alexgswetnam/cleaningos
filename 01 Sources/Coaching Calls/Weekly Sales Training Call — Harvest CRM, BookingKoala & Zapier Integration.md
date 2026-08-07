---
title: "Weekly Sales Training Call — Harvest CRM, BookingKoala & Zapier Integration"
type: source
source_type: sales training call
course: Weekly Sales Training Calls
original_filename: Court_Harvest_CRM_BK_and_Zap_integration.md
date_translated: unknown
retrieved: 2026-08-06
origin: Google Drive — Markdown / Weekly Sales Training Calls
note: |
  IMMUTABLE. AI lesson summary pulled from Drive, verbatim. Markdown escape characters
  from the Drive export were removed; no wording was changed.

  A thinner plain-text export of the same call exists at
  `99 Scratchpad/_extract/sales-training/txt/Weekly Sales Training Calls/Court Harvest
  CRM BK and Zap integration.txt` — not separately archived; this markdown version is
  the richer of the two and is treated as the record.

  DATE IS NOT ESTABLISHED. No date appears anywhere in the module title, filename, or
  transcript. "Court" in the filename is Courtney (the member on the call). Per
  CONSTITUTION §X, undated material defaults to Type 3 (Contested) if it conflicts with
  anything, and cannot supersede. It is not used to date-settle anything on this
  ingestion pass.
---

# Connecting Harvest CRM, BookingKoala, and Zapier: Full Integration Setup Walkthrough

## Module
Court Harvest CRM BK and Zap integration

## Course
Weekly Sales Training Calls

## Skool URL
Not provided.

## Best For
Cleaning business owners who need to connect their website forms (Wix or other), BookingKoala, and Harvest CRM through Zapier so leads and bookings automatically flow into the pipeline, and who want to understand how the quote feature works for leads who don't book on the call.

## Problems This Solves
- Website form submissions not flowing into the CRM automatically.
- Having to manually move leads through the pipeline when they book or get quoted.
- Not knowing how to use the BookingKoala quote feature to capture leads who don't book.
- Losing leads who say "just send me the quote" because there's no system to follow up.
- Not getting emails from prospects (and losing the ability to re-engage them).
- Not knowing what Zapier plan or setup is needed to connect everything.

## Quick Summary
This is a live technical walkthrough where Alex helps Courtney connect her Wix website forms, BookingKoala, and Harvest CRM through Zapier. They set up two integrations: website form submissions (both the pop-up quote form and the contact form) auto-create contacts in Harvest CRM with immediate text notifications, and BookingKoala bookings auto-move leads through the CRM pipeline stages. Alex also walks through how to use BookingKoala's quote feature for leads who don't book on the call — save as a draft/quote, send it to their email, and it moves them to the "quoted" stage in Harvest so they get higher-priority follow-up. The key insight: getting the prospect's email by offering to "send everything over" gives you another channel to re-engage them and re-enter the sales conversation. Courtney's one-time follow-up results continue to grow — three bookings plus three interested from sending 20 messages per day to old contacts. The Zapier $30/month plan is needed for the split-into-paths feature that routes one-time vs. recurring bookings differently.

## Core Teaching

### The Integration Architecture
The goal: every lead and booking flows automatically into Harvest CRM without manual data entry. Three connection points:

**Website form → Harvest CRM (via Zapier).** When someone fills out a form on the website (pop-up quote form or contact form), Zapier detects the submission, parses the data (name, phone, optional message), and creates a contact in Harvest CRM. The contact immediately gets an automated text. A notification goes to the owner/VA. Each form gets its own Zap so you can identify the source (e.g., "Wix pop-up" vs. "Wix contact form").

**BookingKoala booking → Harvest CRM (via Zapier).** When someone is booked in BookingKoala, Zapier recognizes the existing lead in Harvest and moves them from the new lead or follow-up stage to the appropriate booked stage (booked one-time or booked recurring). This triggers the automated welcome sequence — expectations email, "welcome to the family" text, etc. The Zapier setup uses a "split into paths" feature to route one-time bookings differently from recurring bookings. This feature requires the $30/month Zapier plan.

**BookingKoala quote → Harvest CRM (via Zapier).** When you save a quote in BookingKoala (instead of a booking), it moves the contact from the new lead or follow-up stage to the "quoted" stage. This flags them as higher-priority follow-up — they've been given a price and are close to booking.

Data that flows with each booking: booking date, service category, frequency, pricing (square foot adjusted price), special notes, and provider notes.

### The BookingKoala Quote Feature (For Leads Who Don't Book)
When a lead calls, you have a conversation, but they don't book — "I need to think about it," "I'm shopping around," "let me talk to my wife." Instead of just hanging up:

1. Go into BookingKoala as if you're creating a booking (enter their info, service type, pricing).
2. Instead of saving as a booking, save as a **draft** (if no email) or a **quote** (if you have their email).
3. If saved as a quote, BookingKoala asks if you want to email it to the client. Say yes.
4. The client receives an email with the full quote. They can open it and enter their card info to book themselves — whenever they're ready.
5. In Harvest CRM, the contact moves to the "quoted" stage, flagging them for higher-priority follow-up.

This is powerful for three reasons: the client has your quote in their inbox (not lost in a phone conversation), they can self-checkout without calling back, and you know they're in the "quoted" stage so you follow up more aggressively.

Alex's team has had two to three people who were quoted, never responded to follow-up calls, but then completed the booking through the emailed quote days later.

### Getting the Email (Re-Entering the Sale)
When someone says "just send me the quote" or "I'm going to shop around," this is your opening to get their email:

"Great, I'd love to send you an email with everything. What's your email?"

Once you have it, you can re-enter the sale: "What information are you looking for in that email? What's important to you when choosing a cleaning company — reliability? Consistency?" You're back to selling through the act of customizing their quote email.

Even if you can't close them, you now have their email for future follow-up, the one-time follow-up sequence, and email marketing.

### One-Time Follow-Up Results Update
Courtney is sending 20 messages per day to past clients through the CRM's one-time follow-up sequence. Results so far: three bookings, plus three more interested — and some are responding after the third automated text. This validates the system: set it, let it run, and old contacts who cleaned with you years ago start rebooking.

One person tried to get the credit refunded to their card instead of using it as store credit — answer is no, it's store credit.

### Pricing and Capacity Notes
Courtney sends one cleaner per job. Standard cleans go up to 2,500 square feet maximum. Anything larger requires discussion — for a deep clean on a bigger home, two cleaners are needed. For recurring on a larger home (e.g., 3,500 sqft), one cleaner can do it if the client doesn't mind the extra time, sometimes at a price drop. Move-in/move-out cleans are always one-time.

Pricing is in the middle of the market — only franchises are higher. Most quotes don't get price objections.

## Key Principles
- Every lead and booking should auto-flow into the CRM — no manual data entry.
- Each website form gets its own Zap so you can identify the source.
- When a lead doesn't book, save as a quote in BookingKoala and send it to their email.
- The quote feature lets clients self-checkout later without calling back.
- "Quoted" contacts are higher-priority follow-up — they're close to booking.
- Getting the email is the key to re-engaging leads who don't close on the call.
- The one-time follow-up sequence works — old contacts rebook when prompted.
- Zapier's $30/month plan is needed for the split-into-paths feature.

## Step-by-Step Process

### Connecting Website Forms to Harvest CRM (Zapier)
1. Log into Zapier. Create a new Zap.
2. Trigger: select your website platform (Wix, WordPress, etc.) → select the specific form (e.g., "Request Quote Form").
3. Action: create/update a contact in Harvest CRM (Go High Level).
4. Map the fields: name, phone number, optional message/notes.
5. Add a tag or source label (e.g., "Wix pop-up" or "Wix contact form") so you know where the lead came from.
6. Test: submit the form yourself. Confirm the contact appears in Harvest CRM and you get a notification.
7. Repeat for each form (pop-up quote form + contact form = two separate Zaps).

### Connecting BookingKoala Bookings to Harvest CRM (Zapier)
1. In BookingKoala: go to Settings → Apps & Integrations → Zapier. Get your API credentials.
2. In Zapier: create a new Zap. Trigger: BookingKoala → new booking.
3. Use "split into paths" to route one-time bookings differently from recurring (requires $30/month Zapier plan).
4. Action for each path: update the contact in Harvest CRM → move to the appropriate pipeline stage (booked one-time or booked recurring).
5. Map the data: booking date, service category, frequency, adjusted price, special notes, provider notes.
6. Test: create a test booking in BookingKoala. Confirm it moves the contact in Harvest CRM and triggers the welcome sequence.

### Using the BookingKoala Quote Feature
1. On a call, the lead doesn't book. Enter their info in BookingKoala as if creating a booking.
2. Instead of "Save Booking," click "Save as Draft" (no email) or "Save as Quote" (has email).
3. If saved as a quote: BookingKoala asks "Send this to the client's email?" → Yes.
4. The client receives the quote via email and can enter card info to self-checkout.
5. In Harvest CRM, the contact moves to the "Quoted" stage automatically (via Zapier).
6. Follow up with quoted contacts as higher priority — they're close to booking.

## Scripts, Examples, or Phrases to Keep
- Getting the email: "Great, I'd love to send you an email with everything. What's your email?"
- Re-entering the sale: "What information are you looking for in that email? What's important to you — reliability? Consistency?"
- On quoting: "Even if we can't close them, sending the quote to their email means they have it and can check out whenever they're ready."
- Quote success: "We've had two or three people that we quoted, didn't talk to them again, and then days later they put in their stuff through the email and were on our calendar."
- One-time follow-up results: "Three bookings, three more interested, and some are responding after the third text. I'm doing 20 a day."
- Cleaner capacity: "One person, up to 2,500 square feet. Anything bigger needs discussion."

## Common Mistakes / Warnings
- Not connecting website forms to the CRM — leads come in and nobody gets notified.
- Having multiple forms with unclear names in Zapier — label each one distinctly.
- Not using the BookingKoala quote feature for leads who don't book — you lose re-engagement ability.
- Hanging up without getting the prospect's email when they say "send me the quote."
- Leaving contacts in the "new lead" stage when they've been quoted — they need higher-priority follow-up in the "quoted" stage.
- Not testing integrations after setup — submit a form yourself to confirm it flows through.
- Using the free Zapier plan when the split-into-paths feature (needed for routing one-time vs. recurring) requires the $30/month plan.
- The GBP verification video in the Skool module is blurry — follow the written instructions or ask for help.

## When the Bot Should Recommend This
Recommend this lesson when a student needs to connect their website forms to Harvest CRM through Zapier, wants to set up the BookingKoala-to-Harvest integration, doesn't know how to use the BookingKoala quote feature, wants to capture emails from leads who don't book, needs to understand the pipeline stages (new lead → follow-up → quoted → booked), or wants to see one-time follow-up sequence results.

## Related Tags
Harvest CRM, BookingKoala, Zapier, integration, website form, Wix, pop-up form, contact form, pipeline stages, new lead, quoted, booked, one-time follow-up, quote feature, self-checkout, email capture, re-engagement, automation, split into paths, API, notifications, welcome sequence, technical setup, cleaning business systems

## Resource Recommendation Description
A live technical walkthrough connecting Wix website forms, BookingKoala, and Harvest CRM through Zapier — including the BookingKoala quote feature for leads who don't book and how to use email capture to re-enter the sale. Point students here when they need to set up their CRM integrations or want to use the quote feature for better follow-up.

## Cleaned Lesson Notes

**Context.** Alex helps Courtney connect her systems live on a call. She has Wix (website), BookingKoala (scheduling/quoting), Harvest CRM (Go High Level — lead management), and Zapier (connecting them). All brand new — Zapier was signed up the previous week.

**Integration 1: Wix forms → Harvest CRM.** Two forms: a pop-up quote request form and a contact form. Each gets its own Zap in Zapier. When someone submits a form, Zapier creates a contact in Harvest CRM with name, phone, and optional message. Tags the source (e.g., "Wix pop-up" or "Wix contact form"). The contact immediately gets an automated text and the owner gets a notification. Tested live — worked on both forms.

**Integration 2: BookingKoala bookings → Harvest CRM.** When someone is booked in BookingKoala, Zapier updates the contact in Harvest and moves them to the correct pipeline stage (booked one-time or booked recurring). Uses "split into paths" in Zapier to route differently — requires the $30/month Zapier plan (seven-day free trial available). Data that flows: booking date, service category, frequency, adjusted price, special notes, provider notes. When booked, the welcome sequence fires automatically — expectations email, "welcome to the family" text.

**Integration 3: BookingKoala quotes → Harvest CRM.** When a lead doesn't book, save their info as a draft (no email) or a quote (has email). Saving as a quote sends it to the client's email — they can open it and self-checkout by entering their card info whenever ready. In Harvest, the contact moves to the "quoted" stage for higher-priority follow-up. Alex's team has had 2–3 people who completed bookings days later through the emailed quote without any follow-up call.

**How to use quotes to re-enter the sale.** When someone says "just send me the quote" or "I'm shopping around": "Great, I'd love to send you an email with everything. What's your email?" Then: "What information are you looking for in that email? What's important to you?" You're back to selling through the act of customizing the email. Even if you can't close, you now have their email for future sequences.

**One-time follow-up update.** Courtney sending 20 messages/day to past clients. Three bookings + three interested so far. Some responding after the third automated text. One person tried to refund the credit to their card — answer is store credit only. System auto-stops for people who opt out or moved.

**Pricing and capacity.** One cleaner per job, up to 2,500 sqft standard. Larger homes: two cleaners for deep clean, or one cleaner for recurring if client doesn't mind extra time (sometimes at a price drop). Move-in/move-out always one-time. Pricing in the middle of the market — only franchises higher.

**Cleaner happiness.** Courtney shared that one of her cleaners told someone: "I love my clients, I love my boss, I love my job." Courtney: "That's all I want — for them to love what they do."

**Tech notes.** Wix has a native Zapier integration. Each form needs a distinct name in Wix for Zapier to identify it. The school video on Zapier setup is blurry — this live walkthrough replaces it for Wix users. Pop-up form set to 4-second delay, should appear on all pages (not just homepage). Remove the country field from the form — not user-friendly.
