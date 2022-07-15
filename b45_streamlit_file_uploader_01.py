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
        copy = st.text_area('copy').split(', ')
        submit_button = st.form_submit_button('submit')

        if submit_button:
            if file != None and versions != ['']:
                st.success('success')
                data.append({
                    'file': file,
                    'versions': versions,
                    'links': links,
                    'copy': copy,
                    'submit_button': submit_button
                })
            
            if file == None:
                st.error('no file found')
            
            if versions == ['']:
                st.error('no versions found')



# main:
# for i in data:
#     # print(i['file'].getvalue(), i['links'], i['versions'])
#     file_name = file.name.replace('.html', '')
#     html_binary = i['file'].getvalue() # html binary
#     html_decoded = html_binary.decode('utf-8') # html decoded
    
#     for j in range(len(versions)):
#         try:
#             version_index = versions.index(versions[j])
#             with open(f'{version_index} - {versions[j]}.html', 'w') as f:
#                 html = html_decoded.replace('{B45}', links[j])
    
#                 st.write(f'{version_index} - {versions[j]}.html')
#                 components.html(html, height=350, scrolling=True)
#                 st.code(html)
#                 st.write('---')

#                 f.write(html)
#         except IndexError:
#             st.error('index error')


# main:
if data:
    versions = data[0]['versions']
    links = data[0]['links']
    copy = data[0]['copy']
    file = data[0]['file']

    file_name = file.name.replace('.html', '')
    html_binary = data[0]['file'].getvalue()
    html_decoded = html_binary.decode('utf-8')


    if copy[0] != '' and links[0] != '':
        for i in copy:
            copy_index = copy.index(i)
            html_decoded = html_decoded.replace(f'{{B45_{str(copy_index)}}}', i)

        for i in links:
            links_index = links.index(i)

            try:
                with open(f'{links_index} - {versions[links_index]}.html', 'w') as f:
                    html = html_decoded.replace('{B45}', links[links_index])
                    st.write(f'{links_index} - {versions[links_index]}.html')
                    components.html(html, height=350, scrolling=True)
                    st.code(html)
                    st.write('---')
                    f.write(html)
            except IndexError:
                # st.warning('version count is not equivalent to link count')
                pass


    elif links[0] != '':
        for i in links:
            links_index = links.index(i)
            with open(f'{links_index} - {versions[links_index]}.html', 'w') as f:
                html = html_decoded.replace('{B45}', links[links_index])
                st.write(f'{links_index} - {versions[links_index]}.html')
                components.html(html, height=350, scrolling=True)
                st.code(html)
                st.write('---')
                f.write(html)

                
    elif copy[0] != '':
        for i in copy:
            copy_index = copy.index(i)
            html_decoded = html_decoded.replace(f'{{B45_{str(copy_index)}}}', i)

        with open(f'{copy_index} - {versions[copy_index]}.html', 'w') as f:
            st.write(f'{copy_index} - {versions[copy_index]}.html')
            components.html(html_decoded, height=350, scrolling=True)
            st.code(html_decoded)
            st.write('---')
            f.write(html_decoded)