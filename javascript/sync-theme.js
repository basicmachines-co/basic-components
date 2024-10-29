// Sync theme from MkDocs to all iframes
document.addEventListener('DOMContentLoaded', () => {
  const iframes = document.querySelectorAll('iframe'); // Select all iframes

  const sendThemeToIframes = () => {
    const theme = document.body.getAttribute('data-md-color-scheme') || 'default';
    iframes.forEach((iframe) => {
      if (iframe.contentWindow) {
        iframe.contentWindow.postMessage({ type: 'theme-change', theme }, '*');
      }
    });
  };

  // Detect theme changes in MkDocs
  const observer = new MutationObserver(sendThemeToIframes);
  observer.observe(document.body, { attributes: true, attributeFilter: ['data-md-color-scheme'] });

  // Sync theme with iframes on load
  iframes.forEach((iframe) => {
    iframe.addEventListener('load', sendThemeToIframes);
  });
});
