export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { name, email, phone, page } = req.body;

  // Log the lead (in production, send to email/CRM)
  console.log('New lead:', { name, email, phone, page, timestamp: new Date().toISOString() });

  // TODO: Integrate with email service or CRM
  // For now, just acknowledge receipt

  return res.status(200).json({ success: true, message: 'Lead captured' });
}
