import streamlit as st


st.header('{B45}')
st.write('Replacement keyword: {B45}')
st.write('---')

data = ''
file_name = ''
file = st.file_uploader('Choose a file')
versions = st.text_input('Versions')
links = st.text_area('Links')
button = st.button('Build File')


links = links.split(', ')
versions = versions.split(', ')


if file is not None:
    file_name = file.name  # .name is a streamlit method
    file = file.getvalue()


try:
    if button == True:
        # print(data, links, versions)
        for i in range(len(links)):
            data = file.decode('utf-8').replace('{B45}', links[i]) # B$% is what we replace
            
            with open(f'{file_name} - {versions[i]}.html', 'w') as f:
                f.write(data)

        st.success('Files built!')
except AttributeError:
    st.error('No file found')