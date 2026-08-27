/** @type {import('tailwindcss').Config} */
export default {
	content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
	theme: {
		extend: {
			colors: {
				brand: {
					50: '#ecfdf5',
					100: '#d1fae5',
					400: '#34d399',
					500: '#10b981',
					600: '#059669',
					700: '#047857',
					800: '#065f46',
					900: '#064e3b',
				},
				dark: {
					bg: '#0B0F19',
					surface: '#111827',
					card: '#1E293B',
					border: 'rgba(255, 255, 255, 0.08)',
				},
			},
			fontFamily: {
				sans: ['Inter', 'system-ui', 'sans-serif'],
				heading: ['Plus Jakarta Sans', 'Inter', 'sans-serif'],
			},
			boxShadow: {
				glow: '0 0 40px -10px rgba(16, 185, 129, 0.3)',
				'glow-lg': '0 0 60px -15px rgba(16, 185, 129, 0.4)',
			},
		},
	},
	plugins: [],
};
