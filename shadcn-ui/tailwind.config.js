/** @type {import("tailwindcss").Config} */
module.exports = {
  darkMode: ["class"],
  content: [
    "index.html",
    "../templates/*.html",
    "../components/**/*.jinja",
    "../examples/**/*.jinja",
    "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      borderRadius: {
        lg: "var(--radius)",
        md: "calc(var(--radius) - 2px)",
        sm: "calc(var(--radius) - 4px)"
      },
      colors: {}
    }
  },
  plugins: [require("tailwindcss-animate"), require("tailwind-forms")]
};
