/** @type {import('tailwindcss').Config} */
export default {
  content: [    
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      animation:{
        'menu-open': 'menu-open 150ms ease-in-out forwards'
      },
      keyframes:{
        'menu-open':{
          "from":{
            opacity:0,
            top:80,
          },
          "to":{
            opacity:1,
            top:84,
          }

        }
      },
      gridTemplateColumns:{
        'shopBlock':'280px 1fr',
        'profileBlock':'1fr 2fr'
      }
    },
  },
  plugins: [],
}

