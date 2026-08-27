/** @type {import('tailwindcss').Config} */
export default {
	content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
	theme: {
		extend: {
			colors: {
				brand: {
					50: '#f0fdf4',
					100: '#dcfce7',
					500: '#22c55e',
					600: '#16a34a',
					700: '#15803d',
					800: '#166534',
					900: '#14532d',
				},
				dark: {
					DEFAULT: '#1D1D1F',
					surface: '#2D2D30',
					card: '#121214',
				},
				grayLight: '#F5F5F7',
				grayMuted: '#6E6E73',
			},
			fontFamily: {
				sans: ['Inter', 'system-ui', 'sans-serif'],
				heading: ['Plus Jakarta Sans', 'Inter', 'sans-serif'],
			},
		},
	},
	plugins: [],
};
