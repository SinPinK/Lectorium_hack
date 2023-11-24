/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        'white': '#FFFFFF',
        'black': '#000000',
        'light-grey': '#f4f7fe',
        'secondary': '#2B3674',
        'text-prim': '#A3AED0',
        'secondary-grey': '#FAFCFE',
        'dark-grey': '#8F9BBA',
        'primary': '#4318FF'
      },
      maxWidth: {
        nv:'290px',
        card:'590px',
        drop:'268px'
      },
      maxHeight: {
        card:'305px'
      },
      spacing: {
        nx:'76px',
        nxs:'33px',
        ny:'52px'
      },
      borderRadius: {
        20:'20px'
      }
    },
    fontFamily: {
      DMSansRegular: ['DMSans-regular', 'sans-serif'],
      DMSansMedium: ['DMSans-medium','sans-serif'],
      DMSansBold: ['DMSans-bold','sans-serif'],
    },
  },
  plugins: [],
}
