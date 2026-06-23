- **Context** — Resume Factory is a highly interactive, authenticated-first application focused on resume creation and account-specific workflows. There are no public, SEO-critical pages in the current scope, and the value is in responsive client-side editing, preview, and user-specific data flows.

- **Decision** — Use Client-Side Rendering (CSR) for the main frontend experience. Keep the app as a Vite-powered React SPA that fetches authenticated data from the backend and renders UI interactions in the browser.

- **Alternatives considered** —
  - Server-Side Rendering (SSR): considered for better first-byte rendering and SEO. Rejected because the app is mostly login-gated, content is personalized, and the overhead of SSR would add complexity without meaningful benefit for the current product scope.
  - Static site generation / pre-rendering: considered for any landing pages or marketing content, but not applicable to the core resume-builder experience, which is dynamic and user-specific.
  - Hybrid SSR only for select pages: considered as a future option, but not worth the additional architecture and operational complexity at this stage.

- **Consequences** —
  - Gained: simpler frontend architecture, faster development iteration, lower runtime complexity, and a UI optimized for interactive editing and authenticated user flows.
  - Gave up: native server-rendered SEO benefits, initial server-side page generation, and some first-load performance advantages on slow networks.
  - Revisit if: the product adds public-facing marketing or resume-sharing pages that need SEO, the app must support better first-load performance for non-authenticated visitors, or if server-rendered previews become a compelling business requirement.