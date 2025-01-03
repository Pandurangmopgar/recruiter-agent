import streamlit as st

def init_theme():
    if 'theme' not in st.session_state:
        st.session_state.theme = 'light'

def toggle_theme():
    if st.session_state.theme == 'light':
        st.session_state.theme = 'dark'
    else:
        st.session_state.theme = 'light'

def render_theme_toggle():
    init_theme()
    
    theme_icon = '🌙' if st.session_state.theme == 'light' else '☀️'
    
    st.markdown(f"""
        <div class="theme-toggle" onclick="toggleTheme()" title="Toggle theme">
            {theme_icon}
        </div>
        
        <script>
        function toggleTheme() {{
            const doc = document.documentElement;
            const currentTheme = doc.getAttribute('data-theme');
            const newTheme = currentTheme === 'light' ? 'dark' : 'light';
            doc.setAttribute('data-theme', newTheme);
            
            // Update session state via Streamlit
            window.parent.postMessage({{
                type: 'streamlit:setComponentValue',
                theme: newTheme
            }}, '*');
        }}
        
        // Initialize theme
        document.documentElement.setAttribute('data-theme', '{st.session_state.theme}');
        </script>
    """, unsafe_allow_html=True)
    
    # Hidden button to handle theme toggle from JavaScript
    if st.button('Toggle Theme', key='theme_toggle'):
        if 'theme' not in st.session_state:
            st.session_state.theme = 'light'
        
        # Toggle theme
        st.session_state.theme = 'dark' if st.session_state.theme == 'light' else 'light'
        
    # Use custom CSS to style the button instead
    st.markdown("""
        <style>
        /* Hide the default button */
        [data-testid="baseButton-secondary"] {
            position: fixed;
            top: 0.5rem;
            right: 0.5rem;
            z-index: 999;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            background: var(--primary-color);
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)
