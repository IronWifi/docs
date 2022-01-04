# **Walled Garden List Guide**

---

If your Captive Portal uses **external means of authentication** (Twitter, Google, Facebook, Okta...etc.), the **walled garden list**, or the **pre-authorisation list** on your access point needs to include domain names required for the authentication to be completed successfully. To find out what list of domains you need, follow the below instructions.

1. Open the **splash page URL** on your computer in Chrome.
2. **Right click** anywhere on the page and choose **Inspect**.
3. Switch to the **Network** tab and check **Preserve log**.
4. Now complete the authentication process.
5. Expand the **web developer toolbar** and find the **Domain** column.
6. Save these domains and include them in your walled garden list.
