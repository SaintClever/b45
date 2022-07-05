import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(layout="wide")
st.header('🐝 {B45}')
st.write('---')
data = []


# sidebar:
with st.sidebar:
    with st.form('key', clear_on_submit=False):
        file = st.file_uploader('file')
        versions = st.text_input('versions').split(', ')
        links = st.text_area('links').split(', ')
        submit_button = st.form_submit_button('submit')

        if submit_button:
            if file != None and versions != [''] and links != ['']:
                st.success('success')
                data.append({
                    'file': file,
                    'versions': versions,
                    'links': links,
                    'submit_button': submit_button
                })
            
            if file == None:
                st.error('no file found')
            
            if versions == ['']:
                st.error('no versions found')

            if links == ['']:
                st.error('no links found')


# main:
for i in data:
    # print(i['file'].getvalue(), i['links'], i['versions'])
    file_name = file.name.replace('.html', '')
    html_binary = i['file'].getvalue() # html binary
    html_decoded = html_binary.decode('utf-8') # html decoded
    
    for j in range(len(versions)):
        try:
            with open(f'{file_name} - {versions[j]}.html', 'w') as f:
                html = html_decoded.replace('{B45}', links[j])
    
                st.write(f'{file_name} - {versions[j]}.html')
                components.html(html, height=350, scrolling=True)
                st.code(html)
                st.write('---')

                f.write(html)
        except IndexError:
            st.error('index error')