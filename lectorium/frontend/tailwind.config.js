/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        'white': '#FFFFFF',
        'black': '#000000',
        'light-gray': '#f4f7fe',
        'secondary': '#2B3674',
        'text-prim': '#A3AED0',
      },
    },
    fontFamily: {
      DMSansRegular: ['DMSans-regular', 'sans-serif'],
      DMSansMedium: ['DMSans-medium','sans-serif'],
      DMSansBold: ['DMSans-bold','sans-serif'],
    },
  },
  plugins: [],
}
