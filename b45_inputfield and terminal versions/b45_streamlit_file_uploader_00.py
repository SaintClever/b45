import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(layout="wide")


st.header('🐝 {B45}')
st.write('---')


data = ''
file_name = ''


# streamlit sidebar
with st.sidebar:
    with st.form('key', clear_on_submit=False):
        file = st.file_uploader('Choose a file')
        versions = st.text_input('Versions')
        links = st.text_area('Links')
        submit_button = st.form_submit_button('Build file')


links = links.split(', ')
versions = versions.split(', ')


# Get file name and file data
if file is not None:
    file_name = file.name.replace('.html', '')  # .name is a streamlit method
    print(file.getvalue())
    file = file.getvalue()



try:
    if submit_button == True:
        try:
            for i in range(len(links)):
                data = file.decode('utf-8').replace('{B45}', links[i]) # {B45} is what we replace
                
                with open(f'{file_name} - {versions[i]}.html', 'w') as f:
                    f.write(data)
                    components.html(data, height=350, scrolling=True)
                    st.write(f'{file_name} - {versions[i]}.html')
                    st.markdown(f'```html{data}```') # Display html with markdown
                    st.write('---')

            # streamlit success notification
            with st.sidebar:
                st.success('Files built!')

        # streamlit error notification
        except IndexError:
            with st.sidebar:
                st.error('version and link count don\'t match')

# streamlit success notification
except AttributeError:
    with st.sidebar:
        st.error('No file found')