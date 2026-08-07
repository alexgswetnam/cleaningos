---
title: "Use Zapier to Connect BookingKoala & Website"
type: source
source_type: course lesson
course: What is Harvest CRM
date_translated: unknown
retrieved: 2026-08-06
origin: Google Drive — Markdown / What is Harvest CRM (md/) — a thinner .txt export of the
  same lesson also exists at
  `99 Scratchpad/_extract/harvest-crm/txt/What is Harvest CRM/Use Zapier to Connect BookingKoala & Website.txt`,
  not separately archived. The .txt reads as a closer verbatim transcript for the first
  portion (Zapier setup, the two BookingKoala zaps) but this .md AI-summary export is kept
  as the source of record per the ingestion brief; it also carries the "Best For / Problems
  This Solves / Key Principles / Step-by-Step Process" structure this vault's other course
  lesson sources use, and covers the website-lead Zap and testing step the excerpt read from
  the .txt did not reach.
note: |
  IMMUTABLE. AI lesson summary pulled from Drive, verbatim. This lesson is distinct from
  "Zapier The Software Glue" (cleaning biz 101 course) — different course, different depth.
  That earlier lesson is a ~120-word overview naming three example zaps in passing. This
  lesson is the actual setup walkthrough for two of those zaps (new quote, new booking with
  paths) plus a third (website lead), with field-level mapping, pipeline-stage targets, and
  the LeadConnector/Harvest CRM connector name. Same defect pattern as other Drive-summary
  sources in this vault: several sections repeat the lesson body near-verbatim (Quick
  Summary, Core Teaching, Cleaned Lesson Notes); "Key Principles," "Best For," and "Related
  Tags" are the summarizer's own extraction, not direct lesson quotation.
---

# Use Zapier to Connect BookingKoala and Your Website to Harvest CRM

## Module
Use Zapier to Connect BookingKoala & Website

## Course
What is Harvest CRM

## Skool URL
Not provided.

## Best For
Students setting up Harvest CRM who need Booking Koala, their website, and other lead or booking sources to automatically connect into the CRM pipeline.

## Problems This Solves
- They have Booking Koala or another scheduling platform but it is not connected to Harvest CRM.
- New quotes and bookings are not automatically creating contacts or opportunities in the CRM.
- One-time bookings and recurring bookings are not being sorted into the right pipeline stages.
- Website leads are not automatically flowing into Harvest CRM.
- They do not understand why Zapier is needed between Booking Koala and Harvest CRM.

## Quick Summary
This lesson explains how Zapier acts as the middle point between Booking Koala, Harvest CRM, and the business website. Harvest CRM needs to connect with the scheduling and payment system so new quotes, new bookings, and website leads land in the right CRM stages automatically. The lesson recommends Booking Koala because it is what the business uses, but the same idea can apply to Jobber, Housecall Pro, or other platforms. The most important Zaps are a new quote Zap, a new booking Zap, and a website lead Zap if website leads are not coming through the booking platform. The new booking Zap should split one-time bookings and recurring bookings into different paths so they land in the correct stages. Zapier is presented as crucial because most softwares do not naturally play nicely together. The goal is to make Harvest CRM receive the right information automatically instead of manually updating everything.

## Core Teaching
Harvest CRM needs to be connected to the system where bookings, quotes, scheduling, and payments happen. For this business, that system is Booking Koala, though the lesson also mentions Jobber, Housecall Pro, and other scheduling systems. The tool that makes the connection happen is Zapier.

Zapier is described as the handshake between platforms. Booking Koala can connect to Zapier, Harvest CRM can connect to Zapier, and other tools like Google Sheets, Discord, Twilio, Gmail, Stripe, and Notion can also connect through it.

The most important setup is three Zaps. The first Zap sends new quotes from Booking Koala into Harvest CRM as opportunities in the quoted stage. The second Zap sends new bookings into Harvest CRM and separates one-time bookings from recurring bookings using paths. One-time bookings go to the booked one-time stage. Recurring bookings go to the booked recurring stage. The third Zap sends website leads into Harvest CRM if the website is not already using the native lead form from the scheduling software.

The student should test each Zap after setup, especially one-time bookings, recurring bookings, and website leads.

## Key Principles
- Zapier is the handshake between Booking Koala and Harvest CRM.
- Booking and scheduling software should not live disconnected from the CRM.
- New quotes should create or update opportunities in the quoted stage.
- New bookings should create or update opportunities in the correct booked stage.
- One-time and recurring bookings need to be separated because they trigger different CRM logic.
- Website leads should flow automatically into the new lead stage.
- The $30/month Zapier version is worth it if paths are needed.
- Always test the Zaps after setup.

## Step-by-Step Process
- Create or open a Zapier account.
- Create the new quote Zap with Booking Koala as the trigger and New Quote as the event.
- Use LeadConnector as the Harvest CRM connector.
- Map the quote information into Harvest CRM, including first name, last name, full name, phone number, email, lead status, booking date, service category, frequency, pricing parameters, square footage, extras, adjusted price, and special notes.
- Place the opportunity into the marketing pipeline under the quoted stage.
- Create the new booking Zap with Booking Koala as the trigger and New Booking as the event.
- Use Zapier paths to split bookings based on frequency.
- If the frequency contains "one time," create or update the opportunity and place it in the booked one-time stage.
- If the frequency does not contain "one time," create or update the opportunity and place it in the booked recurring stage.
- Create a website lead Zap if website leads are not coming through the scheduling platform's native lead form.
- For a website Zap, connect the website form or form notification email into Zapier, extract the contact information, and create the contact and opportunity in Harvest CRM.
- Test the quote Zap, one-time booking path, recurring booking path, and website lead Zap.

## Scripts, Examples, or Phrases to Keep
Key phrases and setup language to keep:

- "Zapier is the middle point that everyone can come to."
- "Booking Koala can connect there, Harvest CRM can connect there, Google Sheets can connect there, Discord can connect there, Twilio, Gmail, everything can connect there."
- "Zapier is wonderful, you should definitely use it for the rest of your life."
- "There is no other way to get around this."
- "Unfortunately, most softwares do not play nice and don't allow their API to be open."

Important Zap structure:

**New Quote Zap**
- Trigger: Booking Koala → New Quote
- Action: LeadConnector / Harvest CRM
- Pipeline Stage: Quoted

**New Booking Zap**
- Trigger: Booking Koala → New Booking
- Path 1: Frequency contains "one time" → Booked One Time
- Path 2: Frequency does not contain "one time" → Booked Recurring

**Website Lead Zap**
- Trigger: website form submission or email notification
- Action: create contact and opportunity in Harvest CRM
- Pipeline Stage: New Lead

## Common Mistakes / Warnings
- Leaving Booking Koala or another scheduling system disconnected from Harvest CRM.
- Not separating one-time and recurring bookings into different paths.
- Using the wrong capitalization or wording for the frequency filter, causing paths not to match.
- Forgetting to map core contact fields like first name, last name, phone, and email.
- Forgetting to include booking notes, pricing parameters, special notes, and service category.
- Not testing the Zaps after building them.
- Assuming all software will connect cleanly without Zapier.
- Trying to skip the paid Zapier plan when paths are needed.

## When the Bot Should Recommend This
Recommend this lesson when a student is setting up Harvest CRM and needs their booking software or website leads to automatically enter the CRM. It should also be recommended when quotes, one-time bookings, recurring bookings, or website leads are not landing in the correct Harvest CRM pipeline stage.

## Related Tags
- Harvest CRM setup
- Zapier
- Booking Koala
- LeadConnector
- website leads
- new quote Zap
- new booking Zap
- CRM automation
- booked one time
- booked recurring
- quoted stage
- new lead stage
- scheduling software
- Jobber
- Housecall Pro
- Google Sheets
- Discord
- Twilio
- Gmail
- automation paths

## Resource Recommendation Description
Use this lesson when connecting Booking Koala, website forms, or other scheduling tools to Harvest CRM through Zapier. It explains the core Zaps needed for quotes, bookings, and website leads.

## Cleaned Lesson Notes
When setting up Harvest CRM, the scheduling and booking system needs to connect to the CRM. This could be Booking Koala, Jobber, Housecall Pro, or a similar platform. The recommendation in the lesson is Booking Koala because that is what the business uses.

Zapier is the tool that lets the systems handshake. Booking Koala can connect to Zapier, Harvest CRM can connect to Zapier, and so can Google Sheets, Discord, Twilio, Gmail, Stripe, Notion, and other tools.

The first important Zap is for new quotes. The trigger is Booking Koala with the event set to new quote. The action uses LeadConnector, which is the Harvest CRM connector. Map the contact information, including first name, last name, full name, phone number, and email address. Mark the person as a lead. In the notes, include the booking date, service category, frequency, pricing parameters, square footage, extras, adjusted price, and special notes. Put the opportunity into the marketing pipeline under the quoted stage.

The second important Zap is for new bookings. The trigger is Booking Koala with the event set to new booking. This Zap should split into paths. One path is for bookings where the frequency contains "one time," matching the exact capitalization and wording in the scheduling software. That path creates or updates the opportunity and places it in the booked one-time stage. The other path is for bookings where the frequency does not contain "one time." That path places the opportunity into the booked recurring stage.

The lesson says the $30/month Zapier version is needed for paths and that it is worth it because Zapier is crucial to the business.

The third important Zap is for website leads if they do not come through Booking Koala or the scheduling platform's native lead form. Depending on the website, this can be done by connecting the form directly to Zapier or by using an email parser-style setup. For example, with WordPress, a plugin can send an email, Zapier can look for that email title, and a small JavaScript step can pull the information from the email. Then the Zap creates a contact, creates an opportunity, and puts that person into the new lead stage.

After building the Zaps, test all of them. Test a new quote, a one-time booking, a recurring booking, and a website lead. The point is not to build every possible automation on day one. The crucial setup is getting quotes, bookings, and website leads into Harvest CRM correctly.
